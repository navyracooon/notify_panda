# notify_panda

PandAをLINEで通知するためのライブラリです。<br>
`ParsePanda`には通知系とは関係なく、純粋にAPIを叩いているだけのプログラムが集まっているので、そこだけ利用したい方もどうぞ。

## 使い方1

1. `.env`を`notify_panda`ディレクトリに用意します
2. https://notify-bot.line.me/ から`ACCESS_TOKEN`を取得し、`.env`に環境変数として記述
3. ECSIDとパスワードをそれぞれ`USERNAME`、`PASSWORD`として`.env`に記述(`DEBUG=False`を記述するとメッセージ送信成功メッセージが出力されなくなります)
4. `main.py`するなり`ParsePanda.PandaParser`だけ利用するなりご自由に


## 使い方2

1. `.env`を`notify_panda`ディレクトリに用意します
2. `.env`に`DATABASE=sqlite`を指定
3. `python NotifyPanda/DBManager.py {ユーザー名} {パスワード} {アクセストークン}`を入力、ユーザー分用意
4. `main.py`で大人数に通知を送ることができます <br>
※ PandAとの兼ね合いによりパスワードを平文で保存しています。他の方に迷惑がかからないよう充分に注意しましょう
