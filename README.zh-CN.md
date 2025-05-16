[English](README.md) | [中文](README.zh-CN.md)

## 🌐 在线演示

体验最新效果：[TWallpaper Live Demo](https://tiancixiong.github.io/twallpaper/)



## 🛠️ 本地开发

### 前置要求
- 确保已安装 [Node.js](https://nodejs.org/)
- 已安装 [pnpm](https://pnpm.io/) 包管理器

### 启动步骤
1. 安装依赖：
   ```bash
   pnpm install
   ```

2. 构建核心包：

   ```bash
   pnpm --filter twallpaper build
   ```

3. 启动服务：

   ```bash
   pnpm --filter website dev
   ```

服务启动后，访问 [http://localhost:5173](http://localhost:5173/) 即可预览。

> 💡 提示：默认使用 Vite 的 5173 端口，如遇端口冲突会自动调整。



## 📡 API 接口

### `.init(options?, container?)`

初始化动画（重新初始化前会自动调用 `dispose()` 方法）

#### options

Type: [`TWallpaperOptions`](https://github.com/crashmax-dev/twallpaper/blob/master/packages/twallpaper/src/types.ts#L21-L28)

#### container

Type: `Element`

### `.animate(start?)`

启动或停止动画

#### start

Type: `boolean`\
Default: `true`

### `.dispose()`

销毁壁纸实例

### `.scrollAnimate(start?)`

启用/禁用鼠标滚动动画

#### start

Type: `boolean`\
Default: `false`

### `.toNextPosition(onNext?)`

跳转到下一个动画位置（使用后会关闭动画）

#### onNext

当 `toNextPosition` 执行完成时触发
Type: `function`

### `.updateColors(colors)`

强制更新颜色

#### colors

Type: `string[]`

### `.updateFrametime(fps?)`

强制更新帧时间

#### fps

Type: `number`\
Default: `30`

### `.updatePattern(pattern)`

强制更新图案配置

#### pattern

Type: [`PatternOptions`](https://github.com/crashmax-dev/twallpaper/blob/master/packages/twallpaper/src/types.ts#L12-L19)

### `.updateTails(tails?)`

强制更新拖尾速度

#### tails

Type: `number`\
Default `90`



## ⚙️ 配置选项

| 参数                 | 类型                  | 默认值  | 说明                                          |
| -------------------- | --------------------- | ------- | --------------------------------------------- |
| `colors`             | `string[]`            |         | 十六进制颜色数组，最多支持4种颜色             |
| `fps`                | `number`              | `30`    | 动画速度                                      |
| `tails`              | `number`              | `90`    | 拖尾动画速度                                  |
| `animate`            | `boolean`             | `true`  | 是否启用动画                                  |
| `scrollAnimate`      | `boolean`             | `false` | 是否启用滚动动画                              |
| `pattern`            | [`PatternOptions`][1] |         | 图案配置                                      |
| `pattern.image`      | `string`              |         | 壁纸图像。可使用[标准图案][2]或自定义图案     |
| `pattern.mask`       | `boolean`             | `false` | 启用[mask-image][3] CSS属性为背景图像添加遮罩 |
| `pattern.background` | `string`              | `#000`  | 图案背景色（当启用`pattern.mask`时无效）      |
| `pattern.size`       | `string`              | `auto`  | 图案尺寸                                      |
| `pattern.blur`       | `number`              | `0`     | 图案模糊度（当启用`pattern.mask`时无效）      |
| `pattern.opacity`    | `number`              | `0.5`   | 图案透明度                                    |

[1]: https://github.com/tiancixiong/twallpaper/blob/master/packages/twallpaper/src/types.ts#L12-L19
[2]: https://github.com/tiancixiong/twallpaper/tree/master/website/public/patterns
[3]: https://developer.mozilla.org/zh-CN/docs/Web/CSS/mask-image

