# -*- coding: utf-8 -*-
# 腾讯云函数（SCF）随机跳转 —— 创建时选 Python 3.6+，执行方法 main.main_handler
# 每次访问随机 302 到一张图：
#   https://<触发器URL>/?type=h  ->  随机横屏图（README 贡献图上方）
#   https://<触发器URL>/?type=v  ->  随机竖屏图（README 左半边）
import random

BASE = "https://app.hnyqwq.cn/png/hnyqwq"
POOLS = {
    "h": ["showHorizontal.jpg", "show3.jpg", "showlogin-bg.jpg"],
    "v": ["showVertical.jpg", "show4.jpg"],
}

def main_handler(event, context):
    qs = (event.get("queryStringParameters") or {})
    t = qs.get("type", "h")
    pool = POOLS.get(t, POOLS["h"])
    pick = random.choice(pool)
    return {
        "statusCode": 302,
        "headers": {
            "Location": BASE + "/" + pick,
            "Cache-Control": "no-store, max-age=0",
        },
        "isBase64Encoded": False,
    }
