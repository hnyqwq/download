# -*- coding: utf-8 -*-
# 腾讯云 SCF Web 函数（Python Flask 模板）—— 一个函数、两个自定义域名：
#   random.rx.hnyqwq.cn      -> 原图（清晰版）
#   1234567hnyznb.rx.hnyqwq.cn -> COS 数据万象实时压缩版（GitHub README 用）
# 访问时加 ?type=h（横屏）或 ?type=v（竖屏）
import random
from flask import Flask, redirect, request

BASE = "https://app.hnyqwq.cn/png/hnyqwq"
# 数据万象实时压缩：最长边 1080px + 质量 85，绕过 GitHub camo 大小限制
PROCESS = "?imageMogr2/thumbnail/1080x/quality/85"
POOLS = {
    "h": ["showHorizontal.jpg", "show3.jpg", "showlogin-bg.jpg"],
    "v": ["showVertical.jpg", "show4.jpg", "show1.jpg", "show2.jpg"],
}
# 压缩版专用域名
COMPRESSED_HOST = "1234567hnyznb.rx.hnyqwq.cn"

app = Flask(__name__)

@app.route("/")
def index():
    t = request.args.get("type", "h")
    pool = POOLS.get(t, POOLS["h"])
    target = BASE + "/" + random.choice(pool)
    host = (request.host or "").lower()
    if host.startswith(COMPRESSED_HOST):
        target += PROCESS
    return redirect(target, 302)

if __name__ == "__main__":
    # SCF Web 函数固定监听 9000 端口，不能删
    app.run(host="0.0.0.0", port=9000)
