# ELF 短网址
一个简单的的 Python 短网址程序

使用 Redis 存储数据

Demo: https://i.myelf.club

## Docker 安装 Redis

```bash
docker pull redis:latest
docker run -itd --name redis -p 6379:6379 redis
# 查看 ip
docker network inspect bridge
```

## Docker 安装短链程序

```bash
docker build -t elfdwz:latest .
docker run -itd --name elfdwz -p 7080:8080 elfdwz
```

