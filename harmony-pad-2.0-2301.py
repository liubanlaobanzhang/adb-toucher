from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time
import os

print('——————————————————————————————————————————')
print('刷码 2.0.2301@2023.1.4@Harmony OS(Pads)]')

for q in range(1,114514):# 检查设备列表
    print('——————————————————————————————————————————')
    os.system('adb devices')
    print('——————————————————————————————————————————')
    sn=int(input('检查是否出现设备，一切正常则输入0回车。输入1重显设备列表。'))
    if sn==1:
        q=q-1
    else:
        sn=0
        break

a=int(input('重复次数？'))+1

with Progress(TextColumn("[progress.description]{task.description}"),
              BarColumn(),
              TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
              TimeRemainingColumn(),
              TimeElapsedColumn()) as progress:
    总进度 = progress.add_task(description="总进度", total=a)
    每个循环 = progress.add_task(description="此循环", total=9)
    for ep in range(1):
        for batch in range(a):
                progress.advance(每个循环, advance=1)
                time.sleep(0.5)
                r=1
                progress.reset(每个循环)
                for step in range(9):
                    if r==1:
                        os.system('adb shell input tap 1350 900') # 点击“扫一扫”
                    if r==2:
                        time.sleep(0.8)
                    if r==3:
                        os.system('adb shell input tap 1450 210') # 呼出照片库（在右上角）
                    if r==4:
                        time.sleep(0.5)
                    if r==5:
                        os.system('adb shell input tap 150 350') # 选择照片
                    if r==6:
                        time.sleep(0.5)
                    if r==7:
                        os.system('adb shell input tap 1500 150') # 确认照片
                    if r==8:
                        time.sleep(3.5) # 等待跳转
                    if r==9:
                        os.system('adb shell input swipe 0 1450 350 1450 100')# 返回
                        os.system('adb shell input swipe 0 1450 350 1450 100')# 返回
                    r=r+1

                    progress.advance(每个循环, advance=1)
                progress.advance(总进度, advance=1)
                