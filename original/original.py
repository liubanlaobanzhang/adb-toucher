import os
import time
a=int(input('重复次数？'))+1
start=time.perf_counter()
for i in range(1,a):
    time.sleep(1)
    print('循环',i,'模拟操作1')
    os.system('adb shell input tap 850 650')
    # 扫描到屏幕上的二维码
    time.sleep(5.75)
    print('循环',i,'模拟操作2:返回')
    os.system('adb shell input tap 80 140')
    time.sleep(0.2)
    os.system('adb shell input tap 80 140')
    print('操作循环',i,'完成')
stop=time.perf_counter()
time=round(stop-start,3)
avgtime=time/(i-1)
print('任务结束！已经循环',i,'次，用时',time,'秒,平均每次',avgtime,'秒')