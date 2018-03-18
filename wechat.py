import itchat
import requests

from itchat.content import *

reply_content = '''这条消息是自动回复的。

出于一些说了你也不懂你懂你也不会来问也懒得解释的原因。为了回归通信的本质，我花都陈冠希决定退出娱乐圈，微信已经很少用了。如果你有急事，可以给我发电报或邮件。

Telegram ID: @pexcn
E-mail: pexcn97@gmail.com'''

# 回复好友消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO])
def text_reply(msg):
    itchat.send(reply_content, msg['FromUserName'])

# 回复群聊 @ 我的消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['IsAt']:
        group_reply_content = reply_content + '\n\n' + '@' + msg['ActualNickName'] + '\u2005'
        itchat.send(group_reply_content, msg['FromUserName'])

itchat.auto_login(hotReload=True, enableCmdQR=True)
itchat.run(debug=True)
