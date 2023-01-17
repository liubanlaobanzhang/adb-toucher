from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time
import os


total=0
print('—————————————————————————————————————————————————')
print('刷码 2.0.2301(Debug 3) [2023.1.4@Harmony OS(Pads)]')
print('此工具正在运行在此目录：')
os.system('echo %cd%')

for qwert in range(114514):
    for q in range(114514):# 检查设备列表
        print('—————————————————————————————————————————————————')
        os.system('adb devices')
        os.system('adb shell input swipe 950 1450 950 850 100')
        time.sleep(0.3)
        os.system('adb shell input swipe 950 850 950 1450 100')
        print('—————————————————————————————————————————————————')
        print('检查屏幕是否有所滑动，一切正常则输入重复次数。输入0重显设备列表，留空回车以退出。')
        a=int(input('重复次数：'))
        if a!=0:
            break
        if q==114513:
            print('Python: 真无聊，走了。')
            exit()

    with Progress(TextColumn("[progress.description]{task.description}"),
                  BarColumn(),
                  TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                  TimeRemainingColumn(),
                  TimeElapsedColumn()) as progress:

        每个循环 = progress.add_task(description="此循环", total=13)
        总进度 = progress.add_task(description="总进度", total=13*a)

        for ep in range(1):
            for batch in range(a):
                progress.reset(每个循环)
                progress.advance(每个循环, advance=1)
                time.sleep(0.5)
                r=1
                for step in range(13):
                    if r==1:
                        os.system('adb shell input tap 1350 900') # 点击“扫一扫”
                    if r==2:
                        time.sleep(0.8)
                    if r==3:
                        os.system('adb shell input tap 1450 210') # 呼出照片库（在右上角）
                        time.sleep(0.3)
                    if r==4:
                        time.sleep(0.2)
                    if r==5:
                        os.system('adb shell input tap 150 350') # 选择照片
                    if r==6:
                        time.sleep(0.2)
                    if r==7:
                        os.system('adb shell input tap 1500 150') # 确认照片
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
                        os.system('adb shell input swipe 0 1450 350 1450 100') # 返回
                        os.system('adb shell input swipe 0 1450 350 1450 100') # 返回
                    r=r+1

                    progress.advance(每个循环, advance=1)
                    progress.advance(总进度, advance=1)
    print('======== 完成 ========')
    total=total+a
    print('已进行',total,'次扫码行为。')