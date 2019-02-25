#### 安装命令

sudo apt-get install openssh-server # 安装ssh服务器
sudo service ssh start  or sudo /etc/init.d/ssh start # 使ssh运行
sudo ps -e | grep ssh # c查看当前ssh的状态

#### 传送文件

scp -r local_dir username@servername:remote_dir

local_dir : 本地文件夹

username : 服务器上的某个与用户名

servename : 服务器的IP地址

scp -r username@servername:/home/remote_dir   /local_dir 从服务器上下载文件

scp /path/filename username@servername:/path_on_server/ 当个文件

