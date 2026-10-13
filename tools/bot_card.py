"""
Render a live paper-trading summary card (SVG) for the GitHub profile.

Input:  the dashboard payload JSON (portfolio + bots with equity history).
Output: assets/bot-card.svg

Only aggregate numbers are shown: total return, bot count, trade count and
the combined equity curve. Bot names, instruments and signals stay private.

Usage:  python tools/bot_card.py payload.json assets/bot-card.svg
"""
import json
import sys
from datetime import datetime, timezone
from html import escape

W, H = 495, 195
PINK, PURPLE, GREEN, RED = "#ff2e88", "#7b5cff", "#2ee6a6", "#ff5370"
BG, FG, MUTED = "#141321", "#e6e6f0", "#a9a8c0"


def combined_curve(bots: list[dict]) -> list[float]:
    """Sum every bot's equity on a shared timeline, carrying the last value forward."""
    series = []
    for b in bots:
        hist = [(h["ts"], h["equity"]) for h in b.get("history") or [] if h.get("equity") is not None]
        if hist:
            series.append((sorted(hist), b.get("starting_balance") or hist[0][1]))
    stamps = sorted({ts for hist, _ in series for ts, _ in hist})
    curve, idx, last = [], [0] * len(series), [start for _, start in series]
    for ts in stamps:
        for i, (hist, _) in enumerate(series):
            while idx[i] < len(hist) and hist[idx[i]][0] <= ts:
                last[i] = hist[idx[i]][1]
                idx[i] += 1
        curve.append(sum(last))
    return curve


def sparkline(values: list[float], x0: int, y0: int, w: int, h: int) -> tuple[str, str]:
    if len(values) < 2:
        return "", ""
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1.0
    pts = [(x0 + w * i / (len(values) - 1), y0 + h - h * (v - lo) / span) for i, v in enumerate(values)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"{x0},{y0 + h} " + line + f" {x0 + w},{y0 + h}"
    return line, area


def render(payload: dict) -> str:
    bots = payload.get("bots") or []
    port = payload.get("portfolio") or {}
    equity = port.get("equity") or sum(b.get("equity") or 0 for b in bots)
    start = port.get("starting_balance") or sum(b.get("starting_balance") or 0 for b in bots) or 1
    pct = (equity / start - 1) * 100
    trades = sum(len(b.get("trades") or []) for b in bots)
    active = sum(1 for b in bots if b.get("available") and b.get("updated_ago") != "durduruldu")
    color = GREEN if pct >= 0 else RED
    line, area = sparkline(combined_curve(bots), 25, 105, W - 50, 60)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    def stat(x, label, value, fill=FG):
        return (f'<text x="{x}" y="72" class="v" fill="{fill}">{escape(value)}</text>'
                f'<text x="{x}" y="90" class="l">{escape(label)}</text>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Live paper trading: {pct:+.2f}%">
<style>
.t{{font:600 17px 'Segoe UI',Ubuntu,sans-serif;fill:{PINK}}}
.v{{font:700 22px 'Segoe UI',Ubuntu,sans-serif}}
.l{{font:400 11px 'Segoe UI',Ubuntu,sans-serif;fill:{MUTED}}}
.f{{font:400 10px 'Segoe UI',Ubuntu,sans-serif;fill:{MUTED}}}
.dot{{animation:p 1.6s ease-in-out infinite}}
@keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
</style>
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{color}" stop-opacity=".35"/><stop offset="1" stop-color="{color}" stop-opacity="0"/>
</linearGradient></defs>
<rect width="{W}" height="{H}" rx="6" fill="{BG}"/>
<circle class="dot" cx="31" cy="30" r="5" fill="{GREEN}"/>
<text x="44" y="36" class="t">Live paper trading · Raspberry Pi</text>
{stat(25, "total return", f"{pct:+.2f}%", color)}
{stat(165, "bots running", str(active))}
{stat(290, "recent trades", str(trades))}
{stat(405, "equity", f"${equity:,.0f}")}
<polygon points="{area}" fill="url(#g)"/>
<polyline points="{line}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>
<text x="25" y="183" class="f">updated {updated} · strategies private · paper account, not financial advice</text>
</svg>
'''


def main(src: str, dst: str) -> None:
    with open(src, encoding="utf-8") as f:
        payload = json.load(f)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(render(payload))


if __name__ == "__main__":
    main(*sys.argv[1:3])
