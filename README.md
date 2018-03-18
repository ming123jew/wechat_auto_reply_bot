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
nohup python3 wechat.py > log.txt 2>&1&
# nohup python3 wechat.py &
```
