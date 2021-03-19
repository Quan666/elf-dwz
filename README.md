# ELF 短网址
一个简单的的 Python 短网址程序

使用 Redis 存储数据

Demo: https://oy.mk

## Docker 安装 Redis

```bash
docker pull redis:latest
docker run -itd --name redis -p 6379:6379 redis
# 查看 ip ,将对应 容器 IP 填入 config.py （如：172.17.0.2
docker network inspect bridge
```

## Docker 安装短链程序

```bash
# 下载代码，进入代码目录
docker build -t elfdwz:latest .

#启动方式一
docker run -itd --name elfdwz -p 7080:8080 elfdwz

#启动方式二（将容器挂载到代码目录 /root/elfdwz/ 方便更新代码
docker run -itd -v /root/elfdwz/:/app/ --name elfdwz -p 7080:8080 elfdwz
```

## 其他操作
```bash
# 重启
docker restart elfdwz
```
