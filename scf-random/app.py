# -*- coding: utf-8 -*-
# 腾讯云 SCF Web 函数（Python Flask 模板）—— 免费默认域名，无需 API 网关
# 访问 <默认域名>/?type=h  ->  随机横屏图
# 访问 <默认域名>/?type=v  ->  随机竖屏图
# 图片经 COS 数据万象实时压缩，原图不受影响
import random
from flask import Flask, redirect, request

BASE = "https://app.hnyqwq.cn/png/hnyqwq"
# 数据万象实时压缩：最长边 1080px + 质量 85，绕过 GitHub camo 大小限制
PROCESS = "?imageMogr2/thumbnail/1080x/quality/85"
POOLS = {
    "h": ["showHorizontal.jpg", "show3.jpg", "showlogin-bg.jpg"],
    "v": ["showVertical.jpg", "show4.jpg", "show1.jpg", "show2.jpg"],
}

app = Flask(__name__)

@app.route("/")
def index():
    t = request.args.get("type", "h")
    pool = POOLS.get(t, POOLS["h"])
    return redirect(BASE + "/" + random.choice(pool) + PROCESS, 302)

if __name__ == "__main__":
    # SCF Web 函数固定监听 9000 端口，不能删
    app.run(host="0.0.0.0", port=9000)
