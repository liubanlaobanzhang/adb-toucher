import subprocess

# xe = subprocess.run("iperf3 -c 127.0.0.1 -p 5668 -J",stdout=subprocess.PIPE)
xe = subprocess.run("ping baidu.com",stdout=subprocess.PIPE)

print(xe.stdout.decode("gbk"))#打印控制台输出
print(xe.returncode)#为0为运行ok，为1则运行异常