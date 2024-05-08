FROM docker.io/caddy:builder-alpine AS builder

RUN xcaddy build \
    --with github.com/caddyserver/nginx-adapter \
    --with github.com/sjtug/caddy2-filter \
    --with github.com/zhangjiayin/caddy-geoip2 \
    --with github.com/caddyserver/replace-response \
    --with github.com/git001/caddyv2-upload \
    --with github.com/WeidiDeng/caddy-cloudflare-ip \
    --with github.com/hairyhenderson/caddy-teapot-module@v0.0.3-0

FROM docker.io/caddy:alpine

COPY --from=builder /usr/bin/caddy /usr/bin/caddy