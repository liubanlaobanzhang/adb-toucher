#设备适用：MIUI13-按键操作
import os
import random
import time
print('——————————————————————————————————————————')
print('刷码 Ver1.0(debug2,@2022.12.27)')

for q in range(1,3):#检查设备列表
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
if a>10 :
    randomcheck1=round(random.randint(1,a),0)
    print('将在第',randomcheck1-1,'次暂停检查。')
if a>30:
        aavg=int(round(a/3,0))
        randomcheck2=round(random.randint(1,aavg),0)
        randomcheck3=round(random.randint(1,2*aavg),0)
        print('将在第',randomcheck1-1,randomcheck2-1,'和',randomcheck3-1,'次暂停检查。')
askcheckon=int(input('你需要将二维码重新保存一份并置于第一个照片位，并确保手机电量大于40%。确认按0：'))
# 后门：按1取消设备检查

start=time.perf_counter() #开始计时
print('——————————————————————————————————————————')
for i in range(1,a):
    print('循环',i,'准备……')
    time.sleep(1)
    if askcheckon!=1:
        if a>10: #检查设备状态，防止跳转小豆乐园
            if i==randomcheck1:
                input('检查设备状态！')
            if a>20:
                if i==randomcheck2:
                    input('检查设备状态！')
                if i==randomcheck3:
                    input('检查设备状态！')
    atime=time.perf_counter() #开始计时-循环
    print('循环',i,'，模拟操作1')
    os.system('adb shell input tap 930 680') # 点击“扫一扫”
    time.sleep(0.75)
    print('循环',i,'，模拟操作2：选择照片')
    os.system('adb shell input tap 950 210') # 呼出照片库（在右上角）
    time.sleep(0.5)
    os.system('adb shell input tap 150 630') # 选择照片
    time.sleep(3.25)
    if i==randomcheck1:
        os.system('adb shell input swipe 850 1650 850 750 100')
    if i==randomcheck2:
        os.system('adb shell input swipe 850 1650 850 750 100')
    if i==randomcheck3:
        os.system('adb shell input swipe 850 1650 850 750 100')
    print('循环',i,'，模拟操作3：返回')
    os.system('adb shell input tap 800 2330') # 
    os.system('adb shell input tap 800 2330') # 
    btime=time.perf_counter() #开始计时-循环
    cycltime=round(btime-atime,3)
    print('循环',i,'：完成，用时',cycltime,'秒')
    print('——————————————————————————————————————————')

stop=time.perf_counter() # 结束计时
time=round(stop-start,3) # 计算时间
avgtime=round(time/i,1)  # 计算平均时间
print('任务结束！已经循环',i,'次，用时',time,'秒,平均每次',avgtime,'秒')