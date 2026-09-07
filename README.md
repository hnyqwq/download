# hnyqwq 应用下载中心

hnyqwq 应用下载页面，用于展示各 HarmonyOS APP 的正式版和测试版下载链接。

网站地址：[download.hnyqwq.cn](https://download.hnyqwq.cn)

## 包含应用

| 应用 | 类型 | 正式版 | 测试版 | 源码 |
|---|---|---|---|---|
| 星河工具盒 | 应用 | [华为应用市场](https://appgallery.huawei.com/app/detail?id=yylx.hny.qwq) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/8q2ifpJx0Qz) | [GitHub](https://github.com/hnyqwq/hny) \| [Gitee](https://gitee.com/hnyqwq/XHTB) \| [GitCode](https://gitcode.com/hnyqwq/XHTB)（私密） |
| 云影工具屋 | 应用 | [华为应用市场](https://appgallery.huawei.com/app/detail?id=com.hny.video) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/7bALvBIvIby) | [GitHub](https://github.com/hnyqwq/video) \| [Gitee](https://gitee.com/hnyqwq/video) \| [GitCode](https://gitcode.com/hnyqwq/video)（私密） |
| 轨交查询指南 | 应用 | [华为应用市场](https://appgallery.huawei.com/app/detail?id=yylx.hnyqwq.metro) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/4uQpMlTjyh5) | [GitHub](https://github.com/hnyqwq/metro) \| [Gitee](https://gitee.com/hnyqwq/metro) \| [GitCode](https://gitcode.com/hnyqwq/metro)（私密） |
| 轨交查询指南（元服务） | 元服务 | [华为服务卡片](https://hoas.drcn.agconnect.link/1f33800aef81874fb9abc8ede95723a5e6443a6c61d5e25c90d4e9adac2006b5) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/97HN26SIItX) | [GitHub](https://github.com/hnyqwq/Metroyfw) \| [Gitee](https://gitee.com/hnyqwq/Metroyfw) \| [GitCode](https://gitcode.com/hnyqwq/Metroyfw)（私密） |
| 云影工具屋（元服务） | 元服务 | [华为服务卡片](https://hoas.drcn.agconnect.link/d499b2ab6cce532a602a2d55a93d66b3a3c371573bc3251790e81b84481f2309) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/52fRvA7p5Ow) | [GitHub](https://github.com/hnyqwq/videoyfw) \| [Gitee](https://gitee.com/hnyqwq/videoyfw) \| [GitCode](https://gitcode.com/hnyqwq/videoyfw)（私密） |

## 特性

- 磨砂玻璃 UI 风格，与[星河通行证](https://user.hnyqwq.cn)设计语言统一
- HarmonyOS Sans SC 字体
- 正式版 / 测试版 / 安卓版 Tab 切换，支持 `?tab=` 参数直链
- 安卓版 Tab 实时检测更新：`?v=` 传入当前版本，自动比较并提示新版本，读取 `apks/metro/update.json`
- 响应式布局，小屏单列大屏双列自动排布
- AppGallery 下载徽章 + AppTest 文字按钮
- 深色/浅色模式切换，跟随系统实时切换
- 背景图切换，首次换图后自动升级高清版
- 收起/展开，收起后进入赏图模式
- 纯静态单文件，零依赖

## 配置

编辑 `index.html` 中的 `APPS` 数组即可增删应用和链接：

```javascript
var APPS = [
  {
    name: "应用名称",
    icon: "images/xxx.png",       // 应用图标
    desc: "应用描述",
    release: [
      { platform: "华为应用市场", url: "https://appgallery.huawei.com/app/detail?id=..." }
    ],
    beta: [
      { platform: "AppTest 邀请测试", url: "https://appgallery.huawei.com/apptest/..." }
    ]
  },
];
```

### 字段说明

| 字段 | 说明 |
|---|---|
| `name` | 应用名称 |
| `icon` | 应用图标图片路径 |
| `desc` | 应用描述 |
| `release` | 正式版链接数组 |
| `beta` | 测试版链接数组 |
| `platform` | 平台名称，决定显示的平台图标（含"AppTest"显示 AppTest 图标，否则显示 AppGallery 图标） |
| `url` | 跳转链接 |

> 正式版下载徽章根据当前主题自动选择：浅色模式使用 `baji2.png`，深色模式使用 `baji1.png`。测试版使用文字按钮，无需手动配置。

### 背景图

默认背景图（低清）：

| 方向 | 文件 |
|---|---|
| 竖屏 | `Vertical.jpg`、`login-bg2.jpg` |
| 横屏 | `login-bg.jpg`、`Horizontal.jpg` |

点击换图后自动升级为高清版：

| 方向 | 文件 |
|---|---|
| 竖屏 | `showVertical.jpg`、`show1.jpg`、`show2.jpg` |
| 横屏 | `showlogin-bg.jpg`、`show3.jpg`、`showHorizontal.jpg` |

### 安卓版更新检测

安卓版 Tab 从 `apks/metro/update.json` 读取版本信息，APK 文件放在服务器 `apks/metro/` 目录（已 gitignore，不发仓库）。

发版步骤：修改 `update.json` 中的版本号、日期、更新内容，上传新 APK 到服务器 `apks/metro/`。

```json
{
  "app": "轨交查询指南",
  "platform": "Android",
  "latest": {
    "versionName": "1.3.2.1",
    "versionCode": 10302001,
    "date": "2026-09-08",
    "apk": "apks/metro/metro-1.3.2.1.apk",
    "size": "12.3 MB",
    "notes": ["更新内容一", "更新内容二"]
  }
}
```

| 字段 | 说明 |
|---|---|
| `versionName` | 最新版本号，用于与 `?v=` 参数比较 |
| `versionCode` | 数字版本号，可选 |
| `date` | 发布日期，可选 |
| `apk` | APK 下载链接，相对站点根目录 |
| `size` | 包大小文案，可选 |
| `notes` | 更新内容，一行一个元素，支持换行排版（也可用单个字符串按 `\n` 拆分） |

`notes` 排版规则（按每行首字符识别）：

| 行首 | 渲染效果 |
|---|---|
| `【xxx】` | 加粗小节标题 |
| `- xxx` | 列表项 |
| `> xxx` | 缩进子行，附着到上一个列表项下 |
| 其他 | 普通段落 |
| 空行 | 忽略（间距由 CSS 控制） |

```json
"notes": [
  "【新增】",
  "- 新功能描述",
  "> 功能补充说明第一行",
  "> 功能补充说明第二行",
  "- 修复某问题",
  "结尾普通段落"
]
```

链接参数：

| 参数 | 说明 |
|---|---|
| `?tab=android` | 直达安卓版 Tab |
| `?v=1.3.2.1` | 传入当前已装版本，页面自动比较并显示"发现新版本 / 已是最新" |

App 内检测更新示例：`https://download.hnyqwq.cn/?tab=android&v=` + 当前 versionName。

### 其他图片资源

| 文件 | 说明 |
|---|---|
| `baji1.png` | 正式版下载徽章（深色模式） |
| `baji2.png` | 正式版下载徽章（浅色模式） |
| `XHTB.png` | 星河工具盒图标 |
| `video.png` | 云影工具屋图标 |
| `metro.png` | 轨交查询指南图标 |
| `metroyfw.png` | 轨交查询指南（元服务）图标 |
| `videoyfw.png` | 云影工具屋（元服务）图标 |
| `AppGallery.png` | AppGallery 平台图标 |
| `AppTest.png` | AppTest 平台图标 |

## 相关项目

- [星河通行证](https://gitee.com/hnyqwq/user-auth-api)（私密） — 统一认证平台
