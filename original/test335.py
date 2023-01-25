import os
import time

for i in range(1,1145141919810):
    os.system('adb shell input tap 1580 1380')
    os.system('adb shell input tap 1720 1100')
    time.sleep(0.3)
