// EdgeOne 边缘函数：随机跳转图片
// 部署：EdgeOne 控制台 → 站点 → 边缘函数 → 创建函数，粘贴本文件全部代码
// 然后添加两条触发规则（匹配 URL 路径）：
//   /png/hnyqwq/random-h.jpg  ->  随机横屏图（README 贡献图上方）
//   /png/hnyqwq/random-v.jpg  ->  随机竖屏图（README 左半边）

const POOLS = {
    "random-h.jpg": ["showHorizontal.jpg", "show3.jpg", "showlogin-bg.jpg"],
    "random-v.jpg": ["showVertical.jpg", "show4.jpg"],
};

addEventListener("fetch", (event) => {
    event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
    const url = new URL(request.url);
    const name = url.pathname.split("/").pop(); // random-h.jpg 或 random-v.jpg
    const pool = POOLS[name] || POOLS["random-h.jpg"];
    const pick = pool[Math.floor(Math.random() * pool.length)];
    return new Response(null, {
        status: 302,
        headers: {
            Location: `${url.origin}/png/hnyqwq/${pick}`,
            "Cache-Control": "no-store, max-age=0",
        },
    });
}
