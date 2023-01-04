# 设备适用：HarmonyOS 平板-手势操作
import os
import time
print('——————————————————————————————————————————')
print('刷码 Ver1.0[debug3@2022.12.28@Harmony OS(Pads)]')

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
askcheckon=int(input('你需要将二维码重新保存一份并置于第一个照片位，并确保手机电量大于40%。确认按0；跳过检查按1：'))
r=0

start=time.perf_counter() # 开始计时
print('——————————————————————————————————————————')

for i in range(1,a):
    print('循环',i,'准备……')
    time.sleep(0.5)
    r=r+1
    atime=time.perf_counter() #开始计时-循环
    print('循环',r,'，模拟操作1')
    os.system('adb shell input tap 1350 900') # 点击“扫一扫”
    time.sleep(0.8)
    print('循环',r,'，模拟操作2：选择照片')
    os.system('adb shell input tap 1450 210') # 呼出照片库（在右上角）
    time.sleep(0.75)
    os.system('adb shell input tap 150 350') # 选择照片
    time.sleep(0.5)
    os.system('adb shell input tap 1500 150') # 确认照片
    print('循环',r,'，等待链接跳转')
    time.sleep(3.5)
    print('循环',r,'，模拟操作3：返回')
    os.system('adb shell input swipe 0 1450 350 1450 100')
    os.system('adb shell input swipe 0 1450 350 1450 100')
    btime=time.perf_counter() # 开始计时-循环
    cycltime=round(btime-atime,3)
    print('操作循环',r,'：完成，用时',cycltime,'秒')
    print('——————————————————————————————————————————')


stop=time.perf_counter() # 结束计时
time=round(stop-start,3) # 计算时间
avgtime=round(time/i,1)  # 计算平均时间
print('任务结束！已经循环',i,'次，用时',time,'秒,平均每次',avgtime,'秒')
exit()
