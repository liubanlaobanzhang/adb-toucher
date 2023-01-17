from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
import time
import os

print('—————————————————————————————————————————————————')
print('刷码 2.0.2301(Debug 1)')
print('—————————————————————————————————————————————————')
print(' Getting things ready…')
with Progress(TextColumn("[progress.description]{task.description}"),
              BarColumn(),
              TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
              TimeRemainingColumn(),
              TimeElapsedColumn()) as progress: # 引用官方Demo
    加载进度 = progress.add_task(description="", total=5)

    loadstep=1
    for load in range(5):
        if load==0:
            os.system('adb shell rm /sdcard/DCIM/Camera/qrcode.png >nul')
        if load==1:
            time.sleep(0.5)
        if load==2:
            os.system('adb push qrcode.png /sdcard/DCIM/Camera >nul')
        if load==3:
            time.sleep(0.5)
        if load==4:
            os.system('adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/qrcode.png >nul')
        progress.advance(加载进度, advance=1)
