# Self-Built Images

[![Update for caddy](https://github.com/nerdneilsfield/self-built-docker/actions/workflows/update-caddy.yaml/badge.svg)](https://github.com/nerdneilsfield/self-built-docker/actions/workflows/update-caddy.yaml)
[![Update for cloudflared](https://github.com/nerdneilsfield/self-built-docker/actions/workflows/update-cloudflared.yaml/badge.svg)](https://github.com/nerdneilsfield/self-built-docker/actions/workflows/update-cloudflared.yaml)

## Caddy

The custom Caddy image ships with a handful of extra modules baked in via `xcaddy`, including `github.com/caddyserver/nginx-adapter`, `github.com/sjtug/caddy2-filter`, `github.com/zhangjiayin/caddy-geoip2`, `github.com/caddyserver/replace-response`, `github.com/WeidiDeng/caddy-cloudflare-ip`, and `github.com/hairyhenderson/caddy-teapot-module@v0.0.3-0`, and the binary is further compressed with UPX before publishing at `ghcr.io/nerdneilsfield/caddy`.

## Cloudflared

The patched Cloudflared image applies our proxy-aware dialer so outbound tunnels honor the environment’s proxy settings, and the multi-arch build is published at `ghcr.io/nerdneilsfield/cloudflared` with architecture-specific tags (for example, `amd64-latest` and `arm64-latest`) alongside the unified `latest`.
