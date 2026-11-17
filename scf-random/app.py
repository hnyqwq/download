# -*- coding: utf-8 -*-
# 腾讯云 SCF Web 函数（Python Flask 模板）—— 压缩版
# 绑定域名：1234567hnyznb.rx.hnyqwq.cn（GitHub README 用）
# 访问 <默认域名>/?type=h  ->  随机横屏图
# 访问 <默认域名>/?type=v  ->  随机竖屏图
# 每张图单独调质量档位，全部卡在 GitHub camo 5MB 限制内（实测值留了余量）
import random
from flask import Flask, redirect, request

BASE = "https://app.hnyqwq.cn/png/hnyqwq"
POOLS = {
    "h": [("showHorizontal.jpg", 95), ("show3.jpg", 100), ("showlogin-bg.jpg", 92)],
    "v": [("showVertical.jpg", 89), ("show4.jpg", 100), ("show1.jpg", 90), ("show2.jpg", 93)],
}

app = Flask(__name__)

@app.route("/")
def index():
    t = request.args.get("type", "h")
    pool = POOLS.get(t, POOLS["h"])
    name, quality = random.choice(pool)
    return redirect(BASE + "/" + name + "?imageMogr2/quality/%d" % quality, 302)

if __name__ == "__main__":
    # SCF Web 函数固定监听 9000 端口，不能删
    app.run(host="0.0.0.0", port=9000)
