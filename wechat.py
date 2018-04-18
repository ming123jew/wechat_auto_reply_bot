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

"""
来自公众号自动回复的消息片段列表
主要用来处理某些公众号 (比如：微信支付) 给你发消息造成死循环的问题
"""
msg_snippet_list = [
    '/stop', '/Stop', '/STOP',
    '有什么可以帮到你', '需要咨询什么', '一句话描述',
    '你还有什么问题', '第一时间处理', '微信支付小助手',
    '小助手会继续努力', '零钱如何提现', '怎么绑定银行卡'
]

# 回复好友消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO])
def chat_reply(msg):
    if msg['FromUserName'] in ignore_list:
        return
    for i in range(len(msg_snippet_list)):
        if msg_snippet_list[i] in msg['Content']:
            ignore_list.append(msg['FromUserName'])
            print('current ignore list: ' + str(ignore_list))
            return
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
add_ignore_list('姜璇')

print('ignore list: ' + str(ignore_list))

# 阻塞线程，保持微信登录
itchat.run(debug=False)
