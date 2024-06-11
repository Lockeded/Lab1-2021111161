# 软件工程实验一

`MainWithUI.py` 为带有UI界面的程序入口,为了实现UI界面与有向图的绘制,需要安装`pyqt5`,`fluent-qt`组件与`graphviz`
安装命令如下：

`pip install pyqt5`

`pip install PyQt-Fluent-Widgets -i https://pypi.org/simple/`

`pip install graphviz`

启动直接运行`Main.py`即可,但根目录必须为当前`README`文件所在目录,不然会发生相对路径的引用错误

如果需要测试随机游走的终止功能,请将程序265行的注释`time.sleep(0.5)`取消,这将使随机游走的时间变长,从而有时间来按下取消按钮