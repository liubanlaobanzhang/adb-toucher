import base64, time, os, random
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn
import ctypes, sys

def redeploy():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        os.system('copy adb/adb.exe %windir%')
        os.system('copy adb/AdbWinApi.dll %windir%')
        os.system('copy adb/AdbWinUsbApi.dll %windir%')
        os.system('copy adb/libwinpthread-1.dll %windir%')
        os.system('pause')

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def prepare():
    os.system('adb devices >nul') # 预热adb

    print(' Getting things ready…')
    with Progress(TextColumn("[progress.description]{task.description}"),
              BarColumn(),
              TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
              TimeElapsedColumn()) as progress: # 引用官方Demo

        加载进度 = progress.add_task(description='',total=9)
        for load in range(-4,6,1):
            if load==-4: # 获取上次的 QRCODE 随机名
                with open('config/name',encoding='utf-8') as fileObj1:
                    for line in fileObj1:
                        lastpngname=line.rstrip()

            if load==-3:
                 # 获取 QRCODE 的 BASE64 代码
                with open('config/qrcodebase.txt',encoding='utf-8') as fileObj1:
                    for line in fileObj1:
                        src=line.rstrip()

            if load==-2:
                data = src.split(',')[1]
                image_data = base64.b64decode(data)
                name='qrcode'+str(round(random.randint(0,1145141919810),0))+'.png'
                with open(name, 'wb') as f:
                    f.write(image_data) # 随机命名QRCODE
                    f.close()

            if load==-1:
                # 写入本次的 QRCODE 随机命名
                f = open('config/name','w') 
                f.write(name) 
                f.close()

            if load==0:
                os.system('adb shell rm /sdcard/DCIM/Camera/'+lastpngname+' >nul')

            if load==1:
                time.sleep(0.5)

            if load==2:
                os.system('adb push '+name+' /sdcard/DCIM/Camera >nul')

            if load==3:
                time.sleep(0.5)
            if load==4:
                os.system('adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/'+name+' >nul')
                os.system('del '+name)
            progress.advance(加载进度, advance=1)