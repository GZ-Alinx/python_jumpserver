# python_jump_script
# 跳板服务器脚本

##  1. 简单跳板功能;
##  2. 服务器添加简单;
##  3. SSH原生连接;







# 部署到跳板机
登陆启动：
```
[root@jumpserver ~]# vim ~/.bash_profile
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH
# 以上内容原有，添加如下行，接口实现用户登陆运行
/usr/local/bin/python3 /root/jump/jumps.py
```
# 效果图

![image](https://github.com/GZ-Alinx/python_jump_script/blob/master/img/xg.png)
