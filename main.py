import subprocess, time, os, prepare
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn

pad="DBY-W09"
nova5pro="SEA-AL10"
nova3i=0

# 加载上次使用月份
with open('config/lastusemonth',encoding='utf-8') as fileObj1:
    for line in fileObj1:
        lastusemonth=line.rstrip()

# 写入本次使用月份
todayusemonth=time.strftime('%m')

# 判断是否跳月
if lastusemonth.strip()==todayusemonth.strip():
    with open('config/monthtotal',encoding='utf-8') as fileObj1:
        for line in fileObj1:
            totala=line.rstrip()
else:
    totala=0
    f = open('config/lastusemonth','w') 
    f.write(todayusemonth) 
    f.close()



print('—————————————————————————————————————————————————————————————————————')
print('刷码 2.0.2302(Debug 3)')
print('—————————————————————————————————————————————————————————————————————')
prepare.update()
print('—————————————————————————————————————————————————————————————————————')
prepare.prepare()
print('—————————————————————————————————————————————————————————————————————')
all1=2500-int(totala)
if all1<=0:
    showall=0
    situation='（已完成）'
else:
    showall=all1

print('本月已运行'+ totala +'/2500 次，剩余',str(showall),'次',situation)

while 114514!=1919810:
    a=input('重复次数：')
    if a=='all' and showall != 0:
        a=all1
    elif showall == 0:
        a=int(input('本月计划已完成，请指定循环次数：'))
    elif int(a)>0:
        a=int(a)
    else:
        print('请指定有效的数字。')

    with Progress(TextColumn("[progress.description]{task.description}"),
                  BarColumn(),
                  TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                  TimeRemainingColumn(),
                  TimeElapsedColumn()) as progress:

        每个循环 = progress.add_task(description="此循环", total=10)
        总进度 = progress.add_task(description="总进度", total=10*a)


        for aqw in range(a+2):
            xe=subprocess.run("adb shell getprop ro.product.model",stdout=subprocess.PIPE) # 获取设备序列号
            qr=xe.stdout.decode("gbk")
            devicename=qr.strip()
            if devicename == pad:
                progress.reset(每个循环)
                progress.advance(每个循环, advance=1)
                time.sleep(0.5)
                for step in range(10):
                    if step==0:
                        os.system('adb -s '+devicename+' shell input tap 1350 900') # 点击“扫一扫”
                    if step==1:
                        time.sleep(0.8)
                    if step==2:
                        os.system('adb -s '+devicename+' shell input tap 1450 210') # 呼出照片库（在右上角）
                        time.sleep(0.3)
                    if step==3:
                        time.sleep(0.2)
                        os.system('adb -s '+devicename+' shell input tap 150 350') # 选择照片
                        time.sleep(0.2)
                    if step==4:
                        os.system('adb -s '+devicename+' shell input tap 1500 150') # 确认照片
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
                        os.system('adb -s '+devicename+' shell input swipe 0 1450 350 1450 100') # 返回
                        os.system('adb -s '+devicename+' shell input swipe 0 1450 350 1450 100') # 返回
                    progress.advance(每个循环, advance=1)
                    progress.advance(总进度, advance=1)

            elif devicename == nova5pro:
                progress.reset(每个循环)
                progress.advance(每个循环, advance=1)
                for step in range(10):
                    if step==0:
                        os.system('adb -s '+devicename+' shell input tap 850 650') # 点击“扫一扫”
                        time.sleep(0.3)
                    if step==1:
                        time.sleep(0.5)
                    if step==2:
                        os.system('adb -s '+devicename+' shell input tap 920 200') # 呼出照片库（在右上角）
                        time.sleep(0.4)
                    if step==3:
                        os.system('adb -s '+devicename+' shell input tap 150 400') # 选择照片
                        time.sleep(0.3)
                    if step==4:
                        os.system('adb -s '+devicename+' shell input tap 975 140') # 确认照片
                        time.sleep(0.5) # 等待跳转
                    if step==5:
                        time.sleep(0.75) # 等待跳转
                    if step==6:
                        time.sleep(0.5) # 等待跳转
                    if step==7:
                        time.sleep(0.5) # 等待跳转
                    if step==8:
                        time.sleep(0.5) # 等待跳转
                        os.system('adb -s '+devicename+' shell input swipe 0 1450 150 1450 100') # 返回
                        os.system('adb -s '+devicename+' shell input swipe 0 1450 150 1450 100') # 返回
                    if step==9:
                        os.system('adb -s '+devicename+' shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
                    progress.advance(每个循环, advance=1)
                    progress.advance(总进度, advance=1)
            
            elif devicename == nova3i:
                progress.reset(每个循环)
                progress.advance(每个循环, advance=1)
                for step in range(10):
                    if step==0:
                        os.system('adb -s '+devicename+' shell input tap 850 650') # 点击“扫一扫”
                        time.sleep(0.3)
                    if step==1:
                        time.sleep(0.5)
                        os.system('adb -s '+devicename+' shell input tap 920 200') # 呼出照片库（在右上角）
                    if step==2:
                        time.sleep(0.4)
                        os.system('adb -s '+devicename+' shell input tap 150 400') # 选择照片
                    if step==3:
                        time.sleep(0.4)
                        os.system('adb -s '+devicename+' shell input tap 150 400') # 选择照片
                    if step==4:
                        os.system('adb -s '+devicename+' shell input tap 975 140') # 确认照片
                        time.sleep(0.75) # 等待跳转
                    if step==5:
                        time.sleep(0.75) # 等待跳转
                    if step==6:
                        time.sleep(0.75) # 等待跳转
                    if step==7:
                        time.sleep(0.75) # 等待跳转
                    if step==8:
                        os.system('adb -s '+devicename+' shell input tap 300 2250') # 返回
                        os.system('adb -s '+devicename+' shell input tap 300 2250') # 返回
                    if step==9:
                        os.system('adb -s '+devicename+' shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
                    progress.advance(每个循环, advance=1)
                    progress.advance(总进度, advance=1)

            totala=str(int(totala)+1)
            f = open('config/monthtotal','w') 
            f.write(totala) 
            f.close()

print('—————————————————————————————————————————————————————————————————————')
os.system('cls')
print('程序正在退出……')
time.sleep(3)