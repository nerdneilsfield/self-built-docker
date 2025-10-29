# ========= Build Caddy with Plugins =========
FROM docker.io/caddy:builder-alpine AS builder
RUN xcaddy build \
    --with github.com/caddyserver/nginx-adapter \
    --with github.com/sjtug/caddy2-filter \
    --with github.com/zhangjiayin/caddy-geoip2 \
    --with github.com/caddyserver/replace-response \
    --with github.com/WeidiDeng/caddy-cloudflare-ip \
    --with github.com/hairyhenderson/caddy-teapot-module@v0.0.3-0

# ========= Compress with UPX =========
FROM gruebel/upx:latest AS UPX
COPY --from=builder /usr/bin/caddy /usr/bin/caddy.org
RUN upx --best --lzma /usr/bin/caddy.org -o /usr/bin/caddy && \
    chmod +x /usr/bin/caddy

# ========= Final Stage =========
FROM docker.io/caddy:alpine AS prod
LABEL maintainer="Qi Deng <dengqi935@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/nerdneilsfield/self-built-docker"
LABEL org.opencontainers.image.description="Caddy Server with custom plugins (nginx-adapter, filter, geoip2, replace-response, cloudflare-ip, teapot)"
LABEL org.opencontainers.image.licenses="MIT"

COPY --from=UPX /usr/bin/caddy /usr/bin/caddy
ENTRYPOINT ["/usr/bin/caddy"]
