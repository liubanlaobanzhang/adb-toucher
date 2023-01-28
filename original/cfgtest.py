import configparser
import os

# 创建对象
cf = configparser.ConfigParser()
# 获取当前工作路径
rootPath = os.path.dirname(__file__)

def readconfig():
    # 输出当前的工作目录
    print(rootPath)

    # 读取一个文件
    cf.read(rootPath + "\\config.ini", "gbk")

    # 获取文件中所有节的名称
    sections = cf.sections()
    print(sections)
    
    # 获取对应节中对应键的值
    name = cf.get("devices", "deivce6")
    print(name) 


def writecongif():
    # 添加节
    cf.add_section("B")

    # 设置键值
    cf.set("B", "a", "123")

    # 删除节
    cf.remove_section("B")

    # 删除键
    cf.remove_option("me", "uid")

    # 保存文件
    cf.write(open(rootPath+"\\config.ini", "w")) 

# 修改自：热心的裴同学 https://www.bilibili.com/read/cv4243065/ 
# 出处：bilibili