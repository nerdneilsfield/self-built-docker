FROM docker.io/caddy:builder-alpine AS builder

LABEL maintainer="Qi Deng <dengqi935@gmail.com>"

RUN xcaddy build \
    --with github.com/caddyserver/nginx-adapter \
    --with github.com/sjtug/caddy2-filter \
    --with github.com/zhangjiayin/caddy-geoip2 \
    --with github.com/caddyserver/replace-response \
    --with github.com/WeidiDeng/caddy-cloudflare-ip \
    --with github.com/hairyhenderson/caddy-teapot-module@v0.0.3-0 # --with github.com/git001/caddyv2-upload \

FROM gruebel/upx:latest as upx
COPY --from=builder /usr/bin/caddy /usr/bin/caddy.org
RUN upx --best --lzma /usr/bin/caddy.org -o /usr/bin/caddy

FROM docker.io/caddy:alpine as prod

COPY --from=upx /usr/bin/caddy /usr/bin/caddy
