import ctypes, sys, os

def a():
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