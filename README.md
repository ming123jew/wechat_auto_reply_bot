# WeChatBot

WeChat was deprecated. this repo just myself auto reply bot.

## How to use?

```bash
# Install python and dependences
apt-get install python3 python3-pip --no-install-recommends
pip3 install itchat

# Upgrade all pip packages
pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U

# Run
python3 wechat.py

# Run in background
# nohup python3 wechat.py > log.txt 2>&1&
# nohup python3 wechat.py &
```

## TODO

1. 每隔 5 分钟 ~ 8 分钟之间向 filehelper 发送一段随机的文字比如时间戳来尝试保持登录状态
2. 每隔 23 小时 ~ 24 小时之间向特定账号发送一条 "i am live" 消息
