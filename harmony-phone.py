# 设备适用：HarmonyOS 手机-手势操作
import os
import time

print('——————————————————————————————————————————')
print('刷码 Ver1.0[debug3,@2022.12.30@Harmony OS(Phone)]')

for q in range(1,114514):#检查设备列表
    print('——————————————————————————————————————————')
    os.system('adb devices')
    os.system('adb shell input swipe 950 1450 950 850 100')
    os.system('adb shell input swipe 950 850 950 1450 100')
    print('——————————————————————————————————————————')
    sn=int(input('检查是否出现设备，一切正常则输入0回车。输入1重显设备列表。'))
    if sn==1:
        q=q-1
    else:
        sn=0
        break

a=int(input('重复次数？'))+1

start=time.perf_counter() #开始计时
print('——————————————————————————————————————————')
print('进程已开始。预计需要',(a-1)*7.5,'秒。')
for i in range(1,a):
    atime=time.perf_counter() #开始计时-循环
    os.system('cls')

    si=1
    print('循环',i,'▓'*si*10,'-'*(50-si*10),si*20,'%')
    os.system('adb shell input tap 850 650') # 点击“扫一扫”
    os.system('cls')

    si=2
    print('循环',i,'▓'*si*10,'-'*(50-si*10),si*20,'%')
    time.sleep(0.5)
    os.system('adb shell input tap 920 200') # 呼出照片库（在右上角）
    time.sleep(0.75)
    os.system('adb shell input tap 150 400') # 选择照片
    time.sleep(0.1)
    os.system('adb shell input tap 975 140') # 确认照片
    os.system('cls')

    si=3
    print('循环',i,'▓'*si*10,'-'*(50-si*10),si*20,'%')
    time.sleep(4)
    os.system('cls')

    si=4
    print('循环',i,'▓'*si*10,'-'*(50-si*10),si*20,'%')
    os.system('adb shell input swipe 0 1450 150 1450 100')
    os.system('adb shell input swipe 0 1450 150 1450 100')
    os.system('cls')

    si=5
    btime=time.perf_counter() # 结束计时-循环
    cycltime=round(btime-atime,3)
    print('循环',i,'▓'*si*10,'-'*(50-si*10),si*20,'%')
    os.system('adb shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口
    time.sleep(0.5)
    os.system('cls')

stop=time.perf_counter() # 结束计时
time=round(stop-start,3) # 计算时间
avgtime=round(time/i,1)-1.5  # 计算平均时间

os.system('cls')
print('-----——————————————————————————————————————————-----')
print('任务结束！已经循环',i,'次，用时',time,'秒,平均每次',avgtime,'秒')