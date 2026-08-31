# 星河应用下载中心

星河通行证旗下应用下载页面，用于展示各 APP 的正式版和测试版下载链接。

部署地址：[download.hnyqwq.cn](https://download.hnyqwq.cn)

## 特性

- 磨砂玻璃 UI 风格，与[星河通行证](https://user.hnyqwq.cn)设计语言统一
- HarmonyOS Sans SC 字体
- 正式版 / 测试版 Tab 切换
- 多平台跳转链接（App Store、华为应用市场、Google Play 等）
- 移动端自适应
- 纯静态单文件，零依赖，部署简单

## 配置

编辑 `index.html` 顶部的 `APPS` 数组即可增删应用和链接：

```javascript
var APPS = [
  {
    name: "应用名称",
    icon: "🚀",
    desc: "应用描述",
    release: [
      { platform: "App Store", url: "https://apps.apple.com/...", color: "#007AFF", icon: "apple" },
      { platform: "华为应用市场", url: "https://appgallery.huawei.com/...", color: "#cf282a", icon: "huawei" },
    ],
    beta: [
      { platform: "TestFlight", url: "https://testflight.apple.com/...", color: "#007AFF", icon: "apple" },
    ]
  },
];
```

### 字段说明

| 字段 | 说明 |
|---|---|
| `name` | 应用名称 |
| `icon` | 显示图标（Emoji） |
| `desc` | 应用描述 |
| `release` | 正式版链接数组 |
| `beta` | 测试版链接数组 |
| `platform` | 平台名称 |
| `url` | 跳转链接 |
| `color` | 品牌色（用于按钮边框和文字） |
| `icon` | 图标标识（apple / huawei / google / xiaomi / generic） |

## 部署

将项目文件部署到任意 Web 服务器，绑定域名 `download.hnyqwq.cn` 即可。

字体文件从 `user.hnyqwq.cn/fonts/` 加载，无需额外配置。

## 相关项目

- [星河通行证](https://gitee.com/hnyqwq/user-auth-api) — 统一认证平台

## 许可

[Apache 2.0](LICENSE)
