<p align="center">
  <img src="assets/header.svg" alt="Ali · lordinek, AI & Algorithmic Trading Developer" />
</p>

I'm Ali. I build trading bots and the tools to validate them. They run 24/7 on a Raspberry Pi, and I check them from Telegram.

The other half is LLM tooling: a desktop client and a terminal mod for Claude, and a Minecraft bot that takes orders in Turkish chat. My channel covers that side.

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,ts,nodejs,java,electron,linux,raspberrypi" alt="Python, TypeScript, Node.js, Java, Electron, Linux, Raspberry Pi" />
</p>

## Projects

**[quant-lab](https://github.com/lordinek/quant-lab)**: the validation scripts I run before trusting a backtest. They check for look-ahead bias, compare against random entries, sweep parameters and test out of sample, plus a prop-firm rule simulator. The strategy in the repo is one that failed. Its backtest looked great because of a stop on the wrong side of entry, and it lost on every market once that was fixed. I left it in as the example.

**[mina-desktop](https://github.com/lordinek/mina-desktop)**: an Electron app on the Claude Agent SDK. It puts Claude Code in its own window with a tray icon and a global hotkey. It has tool-permission prompts, session history and a side panel showing my bots.

**[minecraft-ai-companion](https://github.com/lordinek/minecraft-ai-companion)**: a Mineflayer bot you talk to in normal chat. Gemini only turns the sentence into a task list; mining, farming and building a house are plain code. LLM calls have a daily cap, and the right-click menu works without the model at all.

**[chatgpt-vs-gemini-sword-pvp](https://github.com/lordinek/chatgpt-vs-gemini-sword-pvp)**: a Paper plugin that puts ChatGPT and Gemini in a Minecraft sword duel. Every 2.5 seconds both models get the same state (health, distance, time left) and answer with one move as JSON; the plugin turns it into NPC fighting. It runs best-of-3 and best-of-5 series, tracks latency and API cost, and has a free mock mode. You can also fight one of the models yourself. [The video is on my channel.](https://www.youtube.com/watch?v=5Cq4LQryRHQ)

**[marin-kitagawa-mod](https://github.com/lordinek/marin-kitagawa-mod)**: a Claude Code mod that swaps the thinking spinner for an animated pixel-art Marin Kitagawa drawn in the terminal. She blinks, talks while Claude writes, and shows a thought bubble while it thinks. Each terminal cell is a 2x2 pixel block made of quarter-block characters, with the two colors picked per cell to keep the error lowest.

<p align="center">
  <img src="https://raw.githubusercontent.com/lordinek/marin-kitagawa-mod/main/assets/demo.gif" width="480" alt="Marin Kitagawa mod demo" />
</p>

## What's running

<p align="center">
  <img src="assets/moneyglitch.gif" width="720" alt="Trading dashboard" />
</p>
<p align="center"><sub>My trading dashboard with real numbers from the Pi. I renamed the bots and cut the parts that show what they trade.</sub></p>

The code behind this stays private. A morning report compares every fill with what the backtest would have done, and the first 312 trades matched exactly. The same Pi also runs a Telegram bot that can wake my PC, and the Discord bot for my community server.

## YouTube

<p align="center">
<!-- YOUTUBE:START --><a href="https://www.youtube.com/shorts/m-zhSXJWPJE"><img width="30%" src="https://i.ytimg.com/vi/m-zhSXJWPJE/mqdefault.jpg" alt="İki oyun nasıl birleştirilir? #reklamdeğildir #oyun #bilgilendirici #oyunbirleştirme #ai #minecraft" /></a><a href="https://www.youtube.com/shorts/fBvz_UabB9E"><img width="30%" src="https://i.ytimg.com/vi/fBvz_UabB9E/mqdefault.jpg" alt="Minecraft&#39;ta Yapay Zeka ile Saklambaç Oynamak! ⛏️ #minecraft #yapayzeka #ai #challenge" /></a><a href="https://www.youtube.com/shorts/qMxF6ShwBYo"><img width="30%" src="https://i.ytimg.com/vi/qMxF6ShwBYo/mqdefault.jpg" alt="MİNECRAFT ama YAPAY ZEKADAN KAÇIYORUM  #minecraft #yapayzeka #ai #gaming #challenge" /></a><!-- YOUTUBE:END -->
</p>

<p align="center"><a href="https://www.youtube.com/@lordinek">youtube.com/@lordinek</a></p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lordinek/lordinek/output/snake-dark.svg" />
    <img src="https://raw.githubusercontent.com/lordinek/lordinek/output/snake-light.svg" alt="contribution snake" />
  </picture>
</p>

<p align="center">
  <img src="assets/footer.svg" alt="" />
</p>
