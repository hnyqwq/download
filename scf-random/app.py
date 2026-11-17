# -*- coding: utf-8 -*-
# 腾讯云 SCF Web 函数（Python Flask 模板）—— 压缩版
# 绑定域名：1234567hnyznb.rx.hnyqwq.cn（GitHub README 用）
# 访问 <默认域名>/?type=h  ->  随机横屏图
# 访问 <默认域名>/?type=v  ->  随机竖屏图
# 函数代理返回图片，Cache-Control: max-age=60 —— 浏览器每 60 秒重新随机一次
import random
import urllib.request
from flask import Flask, request, Response

BASE = "https://app.hnyqwq.cn/png/hnyqwq/github"
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
    with urllib.request.urlopen(BASE + "/" + name, timeout=25) as r:
        data = r.read()
    return Response(data, mimetype="image/jpeg",
                    headers={"Cache-Control": "max-age=60"})

if __name__ == "__main__":
    # SCF Web 函数固定监听 9000 端口，不能删
    app.run(host="0.0.0.0", port=9000)
