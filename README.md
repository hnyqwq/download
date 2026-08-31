# 星河应用下载中心 - hnyqwq

星河应用下载页面，用于展示各 APP 的正式版和测试版下载链接。

网站地址：[download.hnyqwq.cn](https://download.hnyqwq.cn)

## 包含应用

| 应用 | 类型 | 正式版 | 测试版 | 源码 |
|---|---|---|---|---|
| 星河工具盒 | 应用 | [华为应用市场](https://appgallery.huawei.com/app/detail?id=yylx.hny.qwq) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/8q2ifpJx0Qz) | [hnyqwq/hny](https://gitee.com/hnyqwq/hny)（私密） |
| 云影工具屋 | 应用 | [华为应用市场](https://appgallery.huawei.com/app/detail?id=com.hny.video) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/7bALvBIvIby) | [hnyqwq/video](https://gitee.com/hnyqwq/video)（私密） |
| 轨交查询指南 | 应用 | [华为应用市场](https://appgallery.huawei.com/app/detail?id=yylx.hnyqwq.metro) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/4uQpMlTjyh5) | [hnyqwq/metro](https://gitee.com/hnyqwq/metro)（私密） |
| 轨交查询指南（元服务） | 元服务 | [华为服务卡片](https://h5hosting-drcn.dbankcdn.cn/cch5/ScenarizedDist/filePage/dist/index.html) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/97HN26SIItX) | [hnyqwq/Metroyfw](https://gitee.com/hnyqwq/Metroyfw)（私密） |
| 云影工具屋（元服务） | 元服务 | [华为服务卡片](https://hoas.drcn.agconnect.link/d499b2ab6cce532a602a2d55a93d66b3a3c371573bc3251790e81b84481f2309) | [AppTest 邀请测试](https://appgallery.huawei.com/apptest/52fRvA7p5Ow) | [hnyqwq/videoyfw](https://gitee.com/hnyqwq/videoyfw)（私密） |

## 特性

- 磨砂玻璃 UI 风格，与[星河通行证](https://user.hnyqwq.cn)设计语言统一
- HarmonyOS Sans SC 字体
- 正式版 / 测试版 Tab 切换
- AppGallery 下载徽章按钮
- 移动端自适应
- 纯静态单文件，零依赖，部署简单

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

> 下载徽章根据当前主题自动选择：浅色模式使用 `baji2.png`，深色模式使用 `baji1.png`，无需手动配置。 |

### 图片资源

| 文件 | 说明 |
|---|---|
| `baji1.png` | 正式版下载徽章（前往 AppGallery 下载） |
| `baji2.png` | 测试版下载徽章（AppTest 邀请测试） |
| `XHTB.png` | 星河工具盒图标 |
| `video.png` | 云影工具屋图标 |
| `metro.png` | 轨交查询指南图标 |
| `metroyfw.png` | 轨交查询指南（元服务）图标 |
| `videoyfw.png` | 云影工具屋（元服务）图标 |
| `AppGallery.png` | AppGallery 平台图标 |
| `AppTest.png` | AppTest 平台图标 |
| `Vertical.jpg` | 竖屏背景图 |
| `Horizontal.jpg` | 横屏背景图 |
| `login-bg.jpg` | 横屏默认背景图 |

## 部署

将项目文件部署到任意 Web 服务器，绑定域名 `download.hnyqwq.cn` 即可。

字体文件从 `user.hnyqwq.cn/fonts/` 加载，无需额外配置。

## 相关项目

- [星河通行证](https://gitee.com/hnyqwq/user-auth-api) — 统一认证平台

## 许可

[Apache 2.0](LICENSE)
