from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time
import os
import sys

total=0
print('—————————————————————————————————————————————————')
print('正在运行在 Python',sys.version)
print('刷码 2.0.2301(Debug 1) [2023.1.4@Harmony OS(Phone)]')
print('此工具正在运行在此目录：')
os.system('echo %cd%')

for fullprogress in range(114514):
    for q in range(1,114514):# 检查设备列表
        print('—————————————————————————————————————————————————')
        os.system('adb devices')
        os.system('adb shell input swipe 950 1450 950 850 100')
        os.system('adb shell input swipe 950 850 950 1450 100')
        print('—————————————————————————————————————————————————')
        print('检查是否出现设备，一切正常则输入循环次数。输入0重显设备列表，留空回车以退出。')
        a=int(input('次数：'))
        if a!=0:
            break
    print('如果出现异常，请按下 Ctrl+C 终止刷码进程。出现锁死情况，请在“此循环”进度条在0%~8%时按下“取消”。')

    with Progress(TextColumn("[progress.description]{task.description}"),
              BarColumn(),
              TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
              TimeRemainingColumn(),
              TimeElapsedColumn()) as progress: # 引用官方Demo
        总进度 = progress.add_task(description="总进度", total=a*14)
        for ep in range(1):
            每个循环 = progress.add_task(description="此循环", total=14)
            for batch in range(a):
                progress.reset(每个循环)
                progress.advance(每个循环, advance=1)
                time.sleep(0.5)
                r=1
                for step in range(14):
                    if r==1:
                        os.system('adb shell input tap 850 650') # 点击“扫一扫”
                    if r==2:
                        time.sleep(0.8)
                    if r==3:
                        os.system('adb shell input tap 920 200') # 呼出照片库（在右上角）
                    if r==4:
                        time.sleep(0.4)
                    if r==5:
                        os.system('adb shell input tap 150 400') # 选择照片
                    if r==6:
                        time.sleep(0.3)
                    if r==7:
                        os.system('adb shell input tap 975 140') # 确认照片
                    if r==8:
                        time.sleep(0.5) # 等待跳转
                    if r==8:
                        time.sleep(0.5) # 等待跳转
                    if r==9:
                        time.sleep(0.5) # 等待跳转
                    if r==10:
                        time.sleep(0.5) # 等待跳转
                    if r==11:
                        time.sleep(0.5) # 等待跳转
                    if r==12:
                        time.sleep(0.5) # 等待跳转
                    if r==13:
                        os.system('adb shell input swipe 0 1450 150 1450 100') # 返回
                        os.system('adb shell input swipe 0 1450 150 1450 100') # 返回
                    if r==14:
                        os.system('adb shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
                    r=r+1
                    progress.advance(每个循环, advance=1)
                    progress.advance(总进度, advance=1)
                
    print('======== 完成 ========')
    total=total+a
    print('已进行',total,'次扫码行为。')