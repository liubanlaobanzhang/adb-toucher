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
    print('循环',i,'准备……0.5')
    time.sleep(0.5)
    print('循环',i,'开始')

    atime=time.perf_counter() #开始计时-循环
    print('===============================')
    print('循环',i,'，模拟操作1')
    os.system('adb shell input tap 850 650') # 点击“扫一扫”
    time.sleep(0.6)
    print('循环',i,'，模拟操作2：选择照片')
    os.system('adb shell input tap 920 200') # 呼出照片库（在右上角）
    time.sleep(0.5)
    os.system('adb shell input tap 150 400') # 选择照片
    time.sleep(0.1)
    os.system('adb shell input tap 975 140') # 确认照片
    print('循环',i,'：等待页面……')
    time.sleep(4)
    print('循环',i,'，模拟操作3：返回')
    os.system('adb shell input swipe 0 1450 150 1450 100')
    os.system('adb shell input swipe 0 1450 150 1450 100')
    btime=time.perf_counter() # 开始计时-循环
    cycltime=round(btime-atime,3)
    print('操作循环',i,'：完成，用时',cycltime,'秒')
    print('===============================')
    os.system('adb shell input tap 685 1370') # 关闭由于跳转失败导致的退出确认窗口

stop=time.perf_counter() # 结束计时
time=round(stop-start,3) # 计算时间
avgtime=round(time/i,1)-1.5  # 计算平均时间
print('-----——————————————————————————————————————————-----')

print('任务结束！已经循环',i,'次，用时',time,'秒,平均每次',avgtime,'秒')