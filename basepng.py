import base64
import random
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time
import os

os.system('adb devices')
# 获取上次的QRCODE随机名
lastpng = 'name.txt'
with open(lastpng,encoding='utf-8') as fileObj1:
    for line in fileObj1:
        lastpngname=line.rstrip()

# 获取 QRCODE 的 BASE64 代码
file = 'qrcodebase.txt'
with open(file,encoding='utf-8') as fileObj1:
    for line in fileObj1:
        src=line.rstrip()

data = src.split(',')[1]
image_data = base64.b64decode(data)
name='qrcode'+str(round(random.randint(1,1145141919810),0))+'.png'
with open(name, 'wb') as f:
        f.write(image_data) # 随机命名QRCODE
        f.close()

# 写入本次的QRCODE随机命名
f = open('name.txt','w') 
f.write(name) 
f.close()

print(' Getting things ready…')
with Progress(TextColumn("[progress.description]{task.description}"),
              BarColumn(),
              TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
              TimeRemainingColumn(),
              TimeElapsedColumn()) as progress: # 引用官方Demo

    加载进度 = progress.add_task(description="", total=6)
    for load in range(6):
            if load==0:
                os.system('adb shell rm /sdcard/DCIM/Camera/'+lastpngname+' >nul')
            if load==1:
                time.sleep(0.5)
            if load==3:
                os.system('adb push '+name+' /sdcard/DCIM/Camera >nul')
            if load==4:
                time.sleep(0.5)
            if load==5:
                os.system('adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/'+name+' >nul')
                os.system('del '+name)
            progress.advance(加载进度, advance=1)