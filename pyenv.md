#### step 1
安装库文件
sudo apt-get update
sudo apt-get update 
sudo apt-get install make build-essential libssl-dev zlib1g-dev 
sudo apt-get install libbz2-dev libreadline-dev libsqlite3-dev wget curl 
sudo apt-get install llvm libncurses5-dev libncursesw5-dev

#### step2
下载安装pyenv 到home/下的.pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

#### step3
设置环境变量
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshenv
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshenv

#### step4
增加pyenv init
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshenv

保证此条命令时添加到/.zshenv 的末尾，因为它不是一条path,/.zshenv首先会寻找path,如果再中途遇到非path会出错
查看命令
tail ~/.zshrc


#### step5
pyenv的常用命令
pyenv version # 查看当前系统的python版本
pyenv versions # 查看当前系统中所有存在的python
pyenv install --list  # 查看当前可供安装的python版本
pyenv install x.x.x  # 
pyenv unintall x.x.x
pyenv local x.x.x  # 告诉某个本地文件夹使用那个版本
pyenv global x.x.x  # 设置当前全局的python版本
pyenv global system # 设置为系统的python版本
pyenv shell x.x.x
优先级：shell > local > global
pyenv rehash  # 当你安装一个新的python版本时要重新哈希一下

更新：
cd ~/.pyenv 或者 cd $(pyenv root)
git pull

#### step6
背景：pyenv通过使用virtualenv 创建虚拟环境，实现了真正的环境隔离，每一个项目都使用一个单独的环境即虚拟环境

##### stepA
安装
cd .pyenv/plugins
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

##### stepB
增加环境变量
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshenv

##### stepC
重启shell
exec "$SHELL"

##### stepD
命令
1 #创建一个版本为2.7.10的python为于${pyrnv root}/version 下的my-vir...文件夹下
pyenv virtualenv 2.7.10 my-virtual-env-2.7.10

pyenv virtualenvs  # 显示当前系统中有的虚拟环境
pyenv activate <name> # 激活虚拟环境
pyenv deactivate # 不激活虚拟环境

pyenv uninstall my-virtual-env # 删除当前的虚拟环境
pyenv virtualenv-delete my-virtual-env # 删除当前的虚拟环境

