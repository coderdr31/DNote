##################################################################
## ssh
ssh user@host  # 登入
ssh -p 22 user@host  # 改端口
## scp
scp local_file user@host:remote_folder/file # 复制文件
scp -r local_fold user@host:remote_fold  # 复制目录

##################################################################
## screen 窗口管理器,防止远程断开而导致程序终端
screen  # 开启新窗口
screen -S yourname  # 新建一个叫yourname的session
screen -ls  # 列出当前所有的session
screen -r yourname/id  # 回到yourname这个session
screen -d yourname  # 远程detach某个session
screen -d -r yourname  # 结束当前session并回到yourname这个session
screen -wipe  # 清除dead的会话
# 在screen session 下的操作
C-a d  # detach，暂时离开当前session，不影响里面的进程
C-a k  # kill window，强行关闭当前的 window,里面的进程也被杀死了
# 当你退出一个窗口中最后一个程序（通常是bash）后，这个窗口就关闭了(= C-a k)
C-a n  # Next，切换到下一个 window
C-a p  # Previous，切换到前一个 window
C-a 0..9  # 切换到第 0..9 个 window
C-a :  # 杀死所有窗口并退出其中运行的所有程序
