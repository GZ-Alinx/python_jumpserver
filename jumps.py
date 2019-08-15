#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 作者： 李雄
# 个人github： https://github.com/GZ-Alinx

import os

ip_server = {}
n = 0
with open('ip.txt', mode='r', encoding='UTF-8') as f:
    while True:
        n += 1
        line = f.readline()
        if len(line) == 0:
            break
        ip_server[str(n)] = line


while True:
    try:
        # 把字典的key按照顺序排列, 初始化一个列表
        ip_list = sorted(ip_server.items(), key=lambda x:x[0])
        #print(ip_list)
        for k,v in ip_list:
            print("{0}: {1}".format(k,v))
            print('-'*100)
        option = input("\033[1;32m请选择操作的服务器:\033[0m")
        if option in ip_server.keys():
            print(ip_server[option])
            user = 'root'
            rsa = 'id_rsa'
            cmd = ' ssh -i %s -o StrictHostKeyChecking=no %s@%s '%(rsa,user,ip_server[option].split()[0])
            # server_check = os.system('ping %s -c 5'%ip_server[option].split()[0])
            # if server_check:
            #     print('服务器在线')
            # else:
            #     print('服务器不在线')
            ssh = os.system(cmd)


        elif option == "exit":
            break
        elif option == "quit":
            break
        else:
            print("\033[1;31m请输入正确的服务器!\033[0m")
    except ValueError as e:
        print(e)