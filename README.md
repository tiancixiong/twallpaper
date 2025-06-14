# TGV

## 说明

Telegram 的默认壁纸在本地可能以 `.tgv`、`.svg`、`.jpg` 等文件格式存储。
tgv 是 Telegram 自定义的一种封装格式，用于存储主题数据（包括壁纸、配色方案等）。tgv 文件本身其实就是一个 xml 文件，可以用文本编辑器直接打开，其中 `<svg/>` 标签内容可以转换成 svg 格式。
tgv 文件是 Telegram theme 的一种格式，它可能包含：

- 背景图（wallpaper）
- 配色方案（颜色值）
- 渐变设置、模糊等参数



## 获取电报壁纸

1. 电报安卓端默认壁纸（pattern.svg）来源：https://web.telegram.org/k/assets/img/pattern.svg
2. 安卓端其他壁纸来源。Telegram 安卓端会把壁纸缓存到本地目录 `/Android/data/org.telegram.messenger/cache/` 下面。安卓端壁纸格式有：jpg、tgv、svg。获取方式：
   1. 把上面目录下的缓存文件全部删除
   2. 打开安卓端：设置->外观->对话壁纸->选择壁纸并设置壁纸
   3. 在路径中下就会出现 .tgv、.svg、.jpg 类型的背景图文件（默认壁纸 pattern.svg 不会出现）




## 其他

- tgv_to_svg.py 脚本作用：自动扫描当前目录下所有`.tgv`文件，将它们转换为`.svg`文件
  - 执行环境：Python3









