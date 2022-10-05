# dante: socks5 proxy
Run dante in docker with docker-compose

## Usage
Put your own username and password in Dockerfile
```
RUN printf '123qwe\n123qwe\n' | adduser anonymous
```

```
docker-compose.yaml up -d --build
```