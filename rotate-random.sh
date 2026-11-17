#!/bin/bash
# 每日随机轮换脚本 —— 在服务器上运行（建议加入 crontab）
# 部署：放到服务器上 png/hnyqwq 对应的图片目录里，然后：
#   chmod +x rotate-random.sh && ./rotate-random.sh   # 手动跑一次验证
#   crontab -e  加一行（每天凌晨 2 点执行，按需改时间）：
#   0 2 * * * /path/to/images/rotate-random.sh
cd "$(dirname "$0")" || exit 1

# 竖屏池：随机一张存为 random.jpg（README 左半边）
vertical=(showVertical.jpg show4.jpg)
# 横屏池：随机一张存为 randomHorizontal.jpg（README 贡献图上方）
horizontal=(showHorizontal.jpg show3.jpg showlogin-bg.jpg)

pick() {
    local files=($1)
    cp -f "${files[$((RANDOM % ${#files[@]}))]}" "$2"
}

pick "${vertical[*]}" random.jpg
pick "${horizontal[*]}" randomHorizontal.jpg
echo "rotated: random.jpg=$(stat -c%s random.jpg 2>/dev/null || wc -c < random.jpg)B, randomHorizontal.jpg=$(stat -c%s randomHorizontal.jpg 2>/dev/null || wc -c < randomHorizontal.jpg)B"
