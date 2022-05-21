
引号括号虽然不属于markdown语法，但也支持相同的包围、选择、去包围操作。
引号括号智能双击选择时略特殊的是：双击引号括号内侧，选中引号括号里的内容(不含引号括号)；按下Alt+双击引号括号内侧，则选中包含符号的整段文字

HBuilderX还支持以下对2**侧文本高效处理的手段**
1. 选中文字按Ctrl+\是在选区两侧添加光标，可以继续输入~~，会在2侧同时输入
2. 向2侧扩大选择：【Win:Alt+Shit+→ 、Mac:Ctrl++Shit+→】；由2侧向内减少选择：【Win:Alt+Shit+← 、Mac:Ctrl++Shit+←】

[链接文字](http://dcloud.io)

```
[链接文字](http://dcloud.io)
```

|		|		|		|
|		|		|		|

1. Emmet：table3*3后敲Tab，表示生成3行3列的表格，行首生效
2. md表格对齐是传统md的痛点，按下Ctrl+K可以自动整理表格格式（暂未兼容不同缩放模式和字体的情况）
3. 支持从excel、wps、word、number的表格中复制粘贴表格进来（不支持合并单元格和单元格换行）

# 《五》分割线

------------- 【Emmet：hr后敲Tab】

*************
=============

# 《六》代码区

``` javascript
	var a = document
```
Emmet：code后敲Tab，行首生效
智能双击：双击语法区开头，即!左侧，选中包含定义符的整段文字
支持代码直接高亮着色，这应该是只有HBuilderX才有的功能。注意需要在代码区开头指定语言类型

# 《七》注释

<!--注释--> 
快捷键：Ctrl+/
智能双击：双击注释首尾的定义符，选中整段注释

# 《八》其他emmet快捷输入

day后敲Tab，当前日期。注意day需在行首或前面有空格
time后敲Tab，当前时间。注意time需在行首或前面有空格

# 《九》文档结构图

文章很长时，word里有文档结构图，HBuilderX也有。
菜单视图-文档结构图，快捷键Alt+W(mac是ctrl+W)，轻松管理长文档

# 《十》运行、预览和打印PDF

对md文件点工具栏或菜单里的浏览器运行，可以使用外部浏览器预览此md文件，会自动渲染为HTML。
点右上角的预览【快捷键Alt+p】，可在HBuilderX右侧预览该md文档的HTML渲染结果。
在浏览器中点打印，选择打印到PDF，可将md输出为PDF格式。（注意在打印选项里去掉页眉页脚）

# 《十一》一键分享

markdown拥有迷人的输入体验，但分享并不方便，尤其是缺少免费、稳定、高速的图床。
[uniCloud](https://unicloud.dcloud.net.cn/)提供了免费、稳定、高速的服务器和cdn。
HBuilderX，基于uniCloud，提供了markdown的一键分享功能。

利用uniCloud的前端网页托管，将markdown稳定转成了HTML网页，并发布为在线的URL。您可以把URL发送给任何想要分享的人。
同时markdown里涉及的图片也会自动上传到前端网页托管里免费cdn中。

更多见: [MarkDown一键分享使用说明](https://ask.dcloud.net.cn/article/37573)

# 《十二》其他常用但你可能不知道的快捷操作技巧

- Ctrl+鼠标左键添加多光标，然后敲字或粘贴，可批量处理。Ctrl+鼠标左键拖选，可选中多个选区。
- Ctrl+鼠标右键删除多光标
- 不选内容按Ctrl+C或X可复制或剪切整行
- 选中2个选区后，按Ctrl+Shift+X，可互换选区内容。如无选区，只是2个光标，则互换2行
- Ctrl+上下键可上下移动行
- Ctrl+Insert可重复插入当前行，如果有选中内容，可重复插入选中内容
- Ctrl+Shift+K可合并多行（是格式化Ctrl+K的反操作）
- 删除
	* 按Ctrl+D可删除选中行，支持多光标
	* Shift+Del删除到行尾
	* Shift+Backspace删除到行首
- 选择
	* Ctrl+E选相同词(mac是Command+D)，连续按可选中多词进一步操作，比替换更方便
	* Ctrl+L可连选多行，Ctrl+Shift+L也是选择行，但不选行首尾的空白字符
	* Ctrl+=可逐级放大选区
	* 双击标题、列表符可选中相应段落
	* 双击英文引号、括号内侧，可选中内部内容
	* 双击缩进符，可选中同缩进段落
	* 双击连字符比如-或_，可选中相连的词，比如双击这里试试，uni-app
- 查找
	* Ctrl+P查找文件
	* Ctrl+Alt+F可在当前目录的所有文档中搜索指定关键字(mac是Command+Shift+f)
	* 选中文字按F3，查找下一个，Shift+F3找上一个
- 云同步：HBuilderX+markdown用于云同步笔记的技巧，请参考[http://ask.dcloud.net.cn/article/13097](http://ask.dcloud.net.cn/article/13097)

都学会了吗？
markdown语法其实很简单，认真学半小时就能掌握。
HBuilderX的极客操作则需要不停反复练习，熟练掌握这些技巧，你将成为高效极客！

