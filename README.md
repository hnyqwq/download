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
- 正式版 / 测试版 Tab 切换
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
