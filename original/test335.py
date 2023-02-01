import os
import time
import random

for i in range(1,1145141919810):
    a=round(random.randint(5,8),0)
    b=round(random.randint(2000,2100),0)
    print(i)
    os.system('adb shell input tap '+str(b)+' 1130')
    time.sleep(0.1*a)
