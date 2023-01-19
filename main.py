import subprocess
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time
import os
pad="DXQBB22324201093"
pad2='192.168.3.188:5555'
nova5pro="6HJ4C19716015113"

print('—————————————————————————————————————————————————')
print('刷码 2.0.2301(Debug 1)')
print('—————————————————————————————————————————————————')
        
os.system('python %cd%/config/prepare.py')

a=int(input('重复次数：'))
with Progress(TextColumn("[progress.description]{task.description}"),
                  BarColumn(),
                  TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                  TimeRemainingColumn(),
                  TimeElapsedColumn()) as progress2:

        每个循环 = progress2.add_task(description="此循环", total=10)
        总进度 = progress2.add_task(description="总进度", total=10*a)


        for aqw in range(a):
            xe=subprocess.run("adb/adb get-serialno",stdout=subprocess.PIPE) # 获取设备序列号
            qr=xe.stdout.decode("gbk")
    
            if qr.strip() == pad or qr.strip() == pad2:
                progress2.reset(每个循环)
                progress2.advance(每个循环, advance=1)
                time.sleep(0.5)
                for step in range(10):
                    if step==0:
                        os.system('adb/adb shell input tap 1350 900') # 点击“扫一扫”
                    if step==1:
                        time.sleep(0.8)
                    if step==2:
                        os.system('adb/adb shell input tap 1450 210') # 呼出照片库（在右上角）
                        time.sleep(0.3)
                    if step==3:
                        time.sleep(0.2)
                        os.system('adb/adb shell input tap 150 350') # 选择照片
                        time.sleep(0.2)
                    if step==4:
                        os.system('adb/adb shell input tap 1500 150') # 确认照片
                        time.sleep(0.3) # 等待跳转
                    if step==5:
                        time.sleep(0.5) # 等待跳转
                    if step==6:
                        time.sleep(0.5) # 等待跳转
                    if step==7:
                        time.sleep(0.5) # 等待跳转
                    if step==8:
                        time.sleep(0.5) # 等待跳转
                    if step==9:
                        os.system('adb/adb shell input swipe 0 1450 350 1450 100') # 返回
                        os.system('adb/adb shell input swipe 0 1450 350 1450 100') # 返回
                    progress2.advance(每个循环, advance=1)
                    progress2.advance(总进度, advance=1)

            if qr.strip() == nova5pro:
                progress2.reset(每个循环)
                progress2.advance(每个循环, advance=1)
                for step in range(12):
                    if step==0:
                        os.system('adb/adb shell input tap 850 650') # 点击“扫一扫”
                    if step==1:
                        time.sleep(0.8)
                    if step==2:
                        os.system('adb/adb shell input tap 920 200') # 呼出照片库（在右上角）
                        time.sleep(0.4)
                    if step==3:
                        os.system('adb/adb shell input tap 150 400') # 选择照片
                        time.sleep(0.3)
                    if step==4:
                        os.system('adb/adb shell input tap 975 140') # 确认照片
                        time.sleep(0.5) # 等待跳转
                    if step==5:
                        time.sleep(0.75) # 等待跳转
                    if step==6:
                        time.sleep(0.75) # 等待跳转
                    if step==7:
                        time.sleep(0.75) # 等待跳转
                    if step==8:
                        os.system('adb/adb shell input swipe 0 1450 150 1450 100') # 返回
                        os.system('adb/adb shell input swipe 0 1450 150 1450 100') # 返回
                    if step==9:
                        os.system('adb/adb shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
                    progress2.advance(每个循环, advance=1)
                    progress2.advance(总进度, advance=1)