import time
import pyautogui   #鼠标键盘操作
import pyperclip   #模拟剪贴板
import os
 
#识别图像的函数（让计算机直到你要点哪个图标）
def mapping_img(img,click):
    box_location=pyautogui.locateOnScreen(img)
    center=pyautogui.center(box_location)
    if click=='double':
        pyautogui.doubleClick(center)
    else:
        pyautogui.leftClick(center)
    time.sleep(1)
 
#自动搜索（别人或自己）
def chat_user(user):
    if user !='':
        #搜索别人
        mapping_img('search.png','single')
        pyautogui.typewrite(user)
        time.sleep(1)
        pyautogui.moveRel(xOffset=0,yOffset=80)#将鼠标移至下方，参数则为位置
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(5)                    
    else:
        #搜索自己（两张图，一个是头像图，一个是消息图，自己试试点击头像就知道什么意思啦）
        mapping_img('shao.png','single') 
        mapping_img('chat.png','single') 
 
#读取txt文件并粘贴发送的函数        
def read_txt(txt):
    file=open(txt,"r",encoding='utf-8') #读文件
    content=file.readlines()
    pyperclip.copy(content[0])
    pyautogui.hotkey('ctrl','v') #复制啦
    file.close()
 
 
def main():
    os.chdir("D:/Users/OCR") #切换到当前工作目录
    print(os.getcwd())      
    mapping_img('wechat.png','double')
    chat_user('wenjianchuanshuzhushou') #这是个栗子，里头如果不填就是发送自己啦
    read_txt('xxxx.txt')    #同目录建立个txt文本，上面便是你要自动发消息的内容
    pyautogui.press('enter')
    time.sleep(2)
 
if __name__=='__main__':
    main()