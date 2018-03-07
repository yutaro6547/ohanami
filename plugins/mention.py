from slackbot.bot import respond_to
from slackbot.bot import default_reply

@default_reply()
def default(message):
    message.reply("""
    2018年のお花見用のbotだよー！\n使い方が分からない時は僕にメンションして「help」って言ってね！
    """)

@respond_to("いつ")
@respond_to("何時")
def when(message):
    message.send("""
    ```
    楽しんごによるお花見案内～～\n
    2018年のお花見は以下の日程で開かれるよ！\n
    ・日時：４月１４日(土)　(仮)10:00 ~ 17:00\n
    ・場所：芝公園\n
    ※雨天の場合はAgoraでみんなで語り合うことになります\n
    ご家族でもペットも恋人もお友達も大歓迎です！\n

    ドドスコスコスコ！ドドスコスコスコ！\n
    ドドスコスコスコ！来てくれないと、ラブ注入！！
    ```
    """)

@respond_to("help")
@respond_to("ヘルプ")
def help(message):
    message.send("""
    このbotの使い方だよ！\n
    「いつ」で僕にメンションするとお花見の日時と場所を教えてくれるよ\n
    「持ち物」で僕にメンションすると当日の持ち物が分かるよ\n
    botで困ったことがあったり機能を追加したい場合は @zukkey にメンションを投げてね！
    """)

@respond_to("持ち物")
@respond_to("もちもの")
def have(message):
    message.send("""
    ```
    楽しんごによるお花見の持ち物案内～～\n
    ・各々好きなお酒！\n
    ・みんなで遊びたいボードゲームなどなど！自由です！\n
    ・楽しむ気持ち！！\n

    ドドスコスコスコ！ドドスコスコスコ！\n
    ドドスコスコスコ！持ってこないと、ラブ注入！！
    ```
    """)

@respond_to("フードアンケート")
def question(message):
    message.send("""
    ```
    楽しんごによるフードアンケート～～\n
    ・当日食べたい食べ物のアンケートにご協力ください
    1. オードブル
    2. 寿司
    3. ピッツァ
    4. その他
    反応してもらえると嬉しいです！

    何回か聞くかもしれません！

    ドドスコスコスコ！ドドスコスコスコ！\n
    ドドスコスコスコ！答えてくれないと、ラブ注入！！
    ```
    """)

@respond_to("ラブ注入！")
def love(message):
    message.reply("そんなあなたにラブ注入！")
