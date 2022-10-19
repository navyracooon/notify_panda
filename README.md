# notify_panda

PandAをLINEで通知するためのライブラリです。<br>
`ParsePanda`には通知系とは関係なく、純粋にAPIを叩いているだけのプログラムが集まっているので、そこだけ利用したい方もどうぞ。

## 使い方

1. `.env`を`notify_panda`ディレクトリに用意します
2. https://notify-bot.line.me/から`ACCESS_TOKEN`を取得し、`.env`に環境変数として記述
3. ECSIDとパスワードをそれぞれ`USERNAME`、`PASSWORD`として`.env`に記述
4. `main.py`するなり`ParsePanda.PandaParser`だけ利用するなりご自由に
