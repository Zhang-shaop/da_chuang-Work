# da_chuang-Work
# 项目结构说明
## 1.文件的结构与内容
+ 12个txt文件中保存的是对应的电解水数据；
+ win1与daChuangWork文件中保存的是主窗口与副窗口的交互界面设计代码，对应于
相应的ui文件中是其静态界面的演示；
+ main函数是运行的主函数，其定义了交互界面中动态交互的动作函数；
+ pic文件中是主窗口的图片背景；
+ client与server是两台计算机交互一组数据的基本语法结构；
+ new_server是服务器应该运行的代码，其中设置对应数量的套接字；
+ new_client(/2)是对应的客户端运行的代码，其中IP填写服务器的ip，并分别设置
不同端口。

## 2.改善方向
+ 可以使用一个套接字，但是多线程来实现多台计算机的交互；
+ 可以尝试显示出数据折线图在对应的数据显示界面上；
+ 需要修改，使其可以定时完成循环，周期性循环；
+ 可以额外增加硬件部分来支撑演示功能。
