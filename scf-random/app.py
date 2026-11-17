# -*- coding: utf-8 -*-
# 腾讯云 SCF Web 函数（Python Flask 模板）—— 压缩版
# 绑定域名：1234567hnyznb.rx.hnyqwq.cn（GitHub README 用）
# 访问 <默认域名>/?type=h  ->  随机横屏图
# 访问 <默认域名>/?type=v  ->  随机竖屏图
# 302 跳转到 COS 数据万象实时压缩的图片（原图不动，加载快不卡顿）
import random
from flask import Flask, redirect, request

BASE = "https://app.hnyqwq.cn/png/hnyqwq/github"
# 数据万象实时压缩：质量 85，保留原始分辨率，最大约 3.5MB（camo 限制 5MB）
PROCESS = "?imageMogr2/quality/85"
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
