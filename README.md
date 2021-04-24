# 爆点机器人|bdg-bot

## 快速开始

1. 参考`go-cqhttp`项目文档，提前配置好反向ws客户端
2. 参考`nonebot2`项目文档，提前配置好`.env`相关文件
3. `git clone`本项目，在项目目录下`nb run`运行即可

## 功能清单
#### 1. 随机涩图
  - 使用命令`setu`、`涩图`、`色图`、`来份涩图`、`来份涩图`即可触发
  - 感谢 [墨天逸— 随机图片API](https://api.mtyqx.cn/)提供的API
#### 2. 爆点语录
  - 使用命令`*/bd语录`、`*/BD语录`、`*/爆点语录`即可触发随机发送爆点语录
  - 新增自助添加语录功能。使用命令如下：
 ```
*/add
<yourtext>
*/end
 ```
   将内容自动加入数据库中
  - 自助删除上一条语录。使用命令`*/del`
  - 新增“欢迎新人进裙功能”，检测到有人进群，@之并send`新人，来爆点吗？`
#### 3. 群表情包（群经典语录）
  - 使用命令前缀`*/`+`知名语录节选`或`关键词` 即可触发机器人发送对应的表情包
  - 例如：
  - ```*/说你是猪```
#### 5. 网易云点歌
  - 使用命令`点歌` + `歌名` 或者直接使用`点歌`，机器人会询问歌名。
  - 通过选择相应序号即可点歌成功
  - 本插件由 `nonebot-plugins-songpicker2` 贡献
#### 6. av/BV号转小程序
  - RT，发送正确格式的B站视频号，机器人会马上将其转换为QQ小程序发出。
  - 本插件由`nonebot-plugins-biliav`贡献
#### 7. 考研倒计时
  - RT，检测到群内发送含“研”字的消息后，自动返回考研时间倒计时（以天为单位）
