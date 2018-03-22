import itchat
import requests
import threading
import time
import random

from itchat.content import *

reply_text = '''这条消息是自动回复的。

微信已经弃用了，如果你有急事，可以给我发电报或者邮件。

Telegram: @pexcn
E-mail: pexcn97@gmail.com'''

"""
weixin: 微信团队
filehelper: 文件传输助手
"""
ignore_list = ['weixin', 'filehelper']

# 回复好友消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO])
def chat_reply(msg):
    if msg['FromUserName'] not in ignore_list:
        itchat.send(reply_text, msg['FromUserName'])

# 回复群聊 @ 我的消息
@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
    if msg['IsAt']:
        group_reply_text = reply_text + '\n\n' + '@' + msg['ActualNickName'] + '\u2005'
        itchat.send(group_reply_text, msg['FromUserName'])

# 定时发送消息
def send_message_task(target, min_sec, max_sec):
    while True:
        delay = random.randint(min_sec, max_sec)
        time.sleep(delay)
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        msg = 'Delay: ' + str(delay) + 's\n' + 'Time: ' + time_str
        itchat.send(msg, toUserName=target)

# 添加忽略列表
def add_ignore_list(who=None):
    if who == None:
        info = itchat.search_friends()
        ignore_list.append(info['UserName'])
    else:
        info = itchat.search_friends(name=who)
        for i in range(len(info)):
            ignore_list.append(info[i]['UserName'])

# 微信登录
itchat.auto_login(hotReload=True, enableCmdQR=True)

# 开新线程随机发消息来尝试保持登录状态
task = threading.Thread(target=send_message_task, args=('filehelper', 300, 600))
task.setDaemon(True)
task.start()

# 把部分联系人添加到忽略列表
add_ignore_list()
add_ignore_list('妈妈')
add_ignore_list('陈家亮')

print('ignore list: ' + str(ignore_list))

# 阻塞线程，保持微信登录
itchat.run(debug=False)
