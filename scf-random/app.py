# -*- coding: utf-8 -*-
# 腾讯云 SCF Web 函数（Python Flask 模板）—— 压缩版
# 绑定域名：1234567hnyznb.rx.hnyqwq.cn（GitHub README 用）
# 访问 <默认域名>/?type=h  ->  随机横屏图
# 访问 <默认域名>/?type=v  ->  随机竖屏图（数据万象等比缩放到宽 1080，不裁剪不变形）
import random
from flask import Flask, redirect, request

BASE = "https://app.hnyqwq.cn/png/hnyqwq/github"
# 竖屏等比缩放到宽 1080 + 质量 85：统一 2:3 比例保证布局稳定，文件约 0.16MB
VCROP = "?imageMogr2/thumbnail/1080x/quality/85"
POOLS = {
    "h": ["showHorizontal.jpg", "show3.jpg", "showlogin-bg.jpg"],
    "v": ["showVertical.jpg", "show4.jpg", "show1.jpg", "show2.jpg"],
}

app = Flask(__name__)

@app.route("/")
def index():
    t = request.args.get("type", "h")
    pool = POOLS.get(t, POOLS["h"])
    name = random.choice(pool)
    if t == "v":
        return redirect(BASE + "/" + name + VCROP, 302)
    return redirect(BASE + "/" + name, 302)

if __name__ == "__main__":
    # SCF Web 函数固定监听 9000 端口，不能删
    app.run(host="0.0.0.0", port=9000)
