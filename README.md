# pachong
SDN用户体验系统

本人菜鸟，用Python自己写着玩的，基于tornado框架，测试打开网站的速度,问题很多，目前只是把网页的URL爬取时间统计一下，打印在网页表格上。其中多进程那个程序有问题，只能爬取URL本身，不能爬取URL里面包含的图片等信息。单进程那个可以。

使用方法就是在window本地新建一个txt文件，里面按照行写URL地址，格式如下：

http://www.sina.com/

http://www.baidu.com/

爬取百度总是返回的HTML信息不全或者干脆不返回，还不知道原因，有知道原因的朋友欢迎告诉我哈。
