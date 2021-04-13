# bdg-bot

## How to start

1. generate project using `nb create` .
2. writing your plugins under `src/plugins` folder.
3. run your bot using `nb run` .

# 连接地址
HOST=127.0.0.1
PORT=2586

# 密钥
SECRET=
ACCESS_TOKEN=

# 超级用户(机器主人)
SUPERUSERS = [ 1364374624 ]

# 命令的前缀
COMMAND_START = ["", "/", "!"]

# 表示一条命令的超时（没有用户输入）时间。
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)

# 机器人昵称
NICKNAME = ["bdg","爆点哥","爆点机器人"]
# 最大命令长度，超过则无效
SHORT_MESSAGE_MAX_LENGTH = 100
# 用户取消命令
SESSION_CANCEL_EXPRESSION = (
    '好的',
    'Okey-Dokey',
    '啥 β',
    '那bdg-bot就先不打扰你啦',
)