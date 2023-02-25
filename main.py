try:
        import subprocess, time, os
        from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
except ModuleNotFoundError:
        print('正在下载必要的应用框架……')
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ rich')
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ subprocess')
        print()


try:
    import prepare
except ModuleNotFoundError:
    print('请尝试重新进行部署。')
    print('错误代码：2')
    exit()

pad="DBY-W09"
nova5pro="SEA-AL10"
nova3i=0
lastusetime='<Unknown>'
mik40pro='M2012K11C'

# 加载上次使用时间
with open('config/lastusetime',encoding='utf-8') as fileObj1:
    for line in fileObj1:
        lastusetime=line.rstrip()

# 加载上次使用月份
with open('config/lastusemonth',encoding='utf-8') as fileObj2:
    for line in fileObj2:
        lastusemonth=line.rstrip()

todayusemonth=time.strftime('%m')
if lastusemonth.strip() == todayusemonth.strip():
    # 获取总数
    with open('config/monthtotal',encoding='utf-8') as fileObj3:
        for line in fileObj3:
            totala=line.rstrip()
else:
    # 写入新月份
    totala=0
    f = open('config/lastusemonth','w') 
    f.write(todayusemonth) 
    f.close()
    # 运行次数写为0
    f = open('config/monthtotal','w') 
    f.write('0') 
    f.close()

nowtime=time.strftime('%Y/%m/%d %H:%M:%S')
f = open('config/lastusetime','w') 
f.write(nowtime) 
f.close()

print('—————————————————————————————————————————————————————————————————————')
print('刷码 2.0.2302(Debug 9)')
# print('—————————————————————————————————————————————————————————————————————')
# prepare.update()
print('—————————————————————————————————————————————————————————————————————')
prepare.prepare()
print('—————————————————————————————————————————————————————————————————————')


print('上次运行于：',lastusetime)
while 114514!=1919810:
    try:



        all1=2500-int(totala)
        if all1<=0:
            showall=0
            situation='\033[0;32m（✅ 已完成）\033[0m'
        else:
            showall=all1
            situation='\033[1;31m（❌ 未完成）\033[0m'

        print('本月已运行', totala +'/2500 次，剩余',str(showall),'次',situation)
        print('退出程序输入：-1。')
        a=input('重复次数：')
        if a== '-1':
            break
        elif a=='all' and showall != 0:
            a=all1
        elif a=='all' and showall == 0:
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


            for aqw in range(a):
                xe=subprocess.run("adb shell getprop ro.product.model",stdout=subprocess.PIPE) # 获取设备序列号
                qr=xe.stdout.decode("gbk")
                devicename=qr.strip()

                if devicename == pad: # Device 1
                    progress.reset(每个循环)
                    progress.advance(每个循环, advance=1)
                    time.sleep(0.5)
                    for step in range(10):
                        if step==0:
                            os.system('adb shell input tap 1350 900') # 点击“扫一扫”
                        if step==1:
                            time.sleep(0.8)
                        if step==2:
                            os.system('adb shell input tap 1450 210') # 呼出照片库（在右上角）
                            time.sleep(0.3)
                        if step==3:
                            time.sleep(0.2)
                            os.system('adb shell input tap 150 350') # 选择照片
                            time.sleep(0.1)
                        if step==4:
                            os.system('adb shell input tap 1500 150') # 确认照片
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
                            os.system('adb shell input swipe 0 1450 350 1450 100') # 返回
                            os.system('adb shell input swipe 0 1450 350 1450 100') # 返回
                        progress.advance(每个循环, advance=1)
                        progress.advance(总进度, advance=1)

                elif devicename == nova5pro: # Device 2
                    progress.reset(每个循环)
                    progress.advance(每个循环, advance=1)
                    for step in range(10):
                        if step==0:
                            os.system('adb shell input tap 850 650') # 点击“扫一扫”
                            time.sleep(0.3)
                        if step==1:
                            time.sleep(0.5)
                        if step==2:
                            os.system('adb shell input tap 920 200') # 呼出照片库（在右上角）
                            time.sleep(0.4)
                        if step==3:
                            os.system('adb shell input tap 150 400') # 选择照片
                            time.sleep(0.3)
                        if step==4:
                            os.system('adb shell input tap 975 140') # 确认照片
                            time.sleep(0.5) # 等待跳转
                        if step==5:
                            time.sleep(0.75) # 等待跳转
                        if step==6:
                            time.sleep(0.5) # 等待跳转
                        if step==7:
                            time.sleep(0.5) # 等待跳转
                        if step==8:
                            time.sleep(0.5) # 等待跳转
                            os.system('adb shell input swipe 0 1450 150 1450 100') # 返回
                            os.system('adb shell input swipe 0 1450 150 1450 100') # 返回
                        if step==9:
                            os.system('adb shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
                        progress.advance(每个循环, advance=1)
                        progress.advance(总进度, advance=1)
                
                elif devicename == nova3i: # Device 3
                    progress.reset(每个循环)
                    progress.advance(每个循环, advance=1)
                    for step in range(10):
                        if step==0:
                            os.system('adb shell input tap 850 650') # 点击“扫一扫”
                            time.sleep(0.3)
                        if step==1:
                            time.sleep(0.5)
                            os.system('adb shell input tap 920 200') # 呼出照片库（在右上角）
                        if step==2:
                            time.sleep(0.4)
                            os.system('adb shell input tap 150 400') # 选择照片
                        if step==3:
                            time.sleep(0.4)
                            os.system('adb shell input tap 150 400') # 选择照片
                        if step==4:
                            os.system('adb shell input tap 975 140') # 确认照片
                            time.sleep(0.75) # 等待跳转
                        if step==5:
                            time.sleep(0.75) # 等待跳转
                        if step==6:
                            time.sleep(0.75) # 等待跳转
                        if step==7:
                            time.sleep(0.75) # 等待跳转
                        if step==8:
                            os.system('adb shell input tap 300 2250') # 返回
                            os.system('adb shell input tap 300 2250') # 返回
                        if step==9:
                            os.system('adb shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
                        progress.advance(每个循环, advance=1)
                        progress.advance(总进度, advance=1)

                elif devicename == mik40pro: # Device 4
                    progress.reset(每个循环)
                    progress.advance(每个循环, advance=1)
                    for step in range(10):
                        if step==0:
                            os.system('adb shell input tap 930 650') # 点击“扫一扫”
                            time.sleep(0.4)
                        if step==1:
                            time.sleep(0.3)
                            os.system('adb shell input tap 950 210') # 呼出照片库（在右上角）
                        if step==2:
                            time.sleep(0.5)
                            os.system('adb shell input tap 150 630') # 选择照片
                            time.sleep(0.2)
                        if step==3:
                            time.sleep(0.2)
                            os.system('adb shell input tap 975 140') # 确认照片
                            time.sleep(0.4) # 等待跳转    
                        if step==4:
                            time.sleep(0.55)
                        if step==5:
                            time.sleep(0.55)
                        if step==6:
                            time.sleep(0.55) # 等待跳转
                        if step==7:
                            time.sleep(0.55) # 等待跳转
                        if step==8:
                            time.sleep(0.5)
                            os.system('adb shell input tap 792 2368') # 返回
                            os.system('adb shell input tap 792 2368') # 返回
                        if step==9:
                            time.sleep(0.2)
                            os.system('adb shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
                        progress.advance(每个循环, advance=1)
                        progress.advance(总进度, advance=1)

                totala=str(int(totala)+1)
                f = open('config/monthtotal','w') 
                f.write(totala) 
                f.close() 
            prepare.notice()
            
    except KeyboardInterrupt:
        exitreason='0'
        break

    except ValueError:
        exitreason='错误：非法字符，程序崩溃。'
        break

print('—————————————————————————————————————————————————————————————————————')
os.system('cls')
print('程序正在退出……\n\033[1;31m⚠️  请不要拔出设备！\033[0m')
savetime=time.strftime('%Y/%m/%d %H:%M:%S')
with open('config/name',encoding='utf-8') as fileObj1:
    for line in fileObj1:
        pngname=line.rstrip()
os.system('%cd%/adb/adb.exe shell rm /sdcard/DCIM/Camera/'+pngname+' >nul')
os.system('git commit -a -m "'+savetime+'"')
os.system('git push')
os.system('cls')