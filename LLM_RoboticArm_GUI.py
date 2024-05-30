import tkinter
from tkinter import ttk
from tkinter import messagebox
import qianfan
import socket
import cv2
from PIL import Image, ImageTk
 
"""
    请你写一段代码，首先将mycobot_280pi机械臂移动到默认位置，然后让机械臂以线性的方式运动到位姿为[57.0, -107.4, 316.3, -93.81, -12.71, -163.49]的位置以抓取目标物体，接着将抓取到的物体放置到位姿为[225.9, 157.0, 150.1, -174.34, 0.18, -45.86]的位置。注意：首先需要通过from pymycobot.mycobot import MyCobot导入MyCobot类，还需要通过from pymycobot import PI_PORT, PI_BAUD导入串口和波特率两个变量，最后要通过import time导入time库，初始化MyCoBot类的代码为MyCobot(PI_PORT, PI_BAUD导入串口和波特率两个变量，最后要通过import)夹爪闭合和打开的速度为60mm/s，机械臂运动的速度为30mm/s，机械臂每次运动的时间间隔为5s。最后不需要关闭连接。可能用到的MyCobot类下的函数有：send_angles(degrees, speed)，作用为将机械臂的各个关节以speed的速度运动到degrees的角度，speed为整数，degrees为列表，该机械臂一共有6个关节；set_gripper_state(flag, speed)，作用为将机械臂的夹爪以speed的速度闭合或打开，flag为1时表示夹爪闭合；send_coords(coords, speed, mode)，作用为将机械臂以speed的速度运动到coords的位姿，mode为1时表示机械臂头部移动的路径为线性的。
"""

# 创建一个界面窗口
win = tkinter.Tk()
win.title("LLM + Robotic arm")
win.geometry("1920x1080")

def xFunc(event):
    print(xVariable.get())
    print(type(xVariable.get()))
# 选择模型下拉框
label_name = tkinter.Label(win, text='请选择要访问的大语言模型：', font=('微软雅黑',10), justify=tkinter.LEFT)
label_name.place(x=635,y=0)

xVariable = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=xVariable, width=40)     # #创建下拉菜单
com.pack()     # #将下拉菜单绑定到窗体
com["value"] = ("ERNIE-Bot", "ERNIE-Bot-turbo", "BLOOMZ-7B", "Qianfan-BLOOMZ-7B-compressed", "Llama-2-7b-chat", "Llama-2-13b-chat", "Llama-2-70b-chat", "Qianfan-Chinese-Llama-2-7B", "ChatGLM2-6B-32K", "AquilaChat-7B", "Linly-Chinese-LLaMA-2-7B", "Linly-Chinese-LLaMA-2-13B", "ChatGLM2-6B", "ChatGLM2-6B-INT4", "Falcon-7B", "Falcon-40B-Instruct", "RWKV-4-World", "RWKV-4-pile-14B", "RWKV-Raven-14B", "OpenLLaMA-7B", "Dolly-12B", "MPT-7B-Instruct", "MPT-30B-instruct", "OA-Pythia-12B-SFT-4")    # #给下拉菜单设定值
com.current(0)    # #设定下拉菜单的默认值为第3个，即山东
com.bind("<<ComboboxSelected>>", xFunc)

# 显示prompt文本框
label_name = tkinter.Label(win, text='请输入您的prompt：', font=('微软雅黑',20), justify=tkinter.LEFT)
label_name.place(x=50,y=50)

text1=tkinter.Text(win, width=100, height=20)
text1.pack()
text1.place(x=50, y=100)

# 应用API Key替换your_ak，Secret Key替换your_sk
chat_comp = qianfan.ChatCompletion(ak="YFWPNvFRzaKjFBViiWG5DV3g", sk="QE9bkHR8EI5R2DaZy9uqdRPrbh2cSNfw")
# 获取prompt输入框的内容
def genreate_code():
    prompt = text1.get("1.0","end")
    if prompt == "\n":
        tkinter.messagebox.showinfo(title='提示！', message='请输入您的prompt：')
        return
    # 指定特定模型
    resp = chat_comp.do(model=xVariable.get(), messages=[{
        "role": "user",
        "content": prompt
    }])
    text2.delete("1.0", "end")
    code_str = resp['result'].split("```")[1].strip('python')
    text2.insert(tkinter.INSERT, code_str)

btn1=tkinter.Button(win, bd=4, font=('微软雅黑',20), text="生成机械臂执行任务的代码", command=genreate_code)
btn1.pack()
btn1.place(x=50,y=375)

text2=tkinter.Text(win, width=100, height=40)
text2.pack()
text2.place(x=50, y=445)

# 机械臂 IP
label_name = tkinter.Label(win, text='请输入机械臂的IP地址：', font=('微软雅黑',10), justify=tkinter.LEFT)
label_name.place(x=1550,y=50)
text5=tkinter.Text(win, width=30, height=1)
text5.pack()
text5.place(x=1550, y=80)
# 机械臂端口号
label_name = tkinter.Label(win, text='请输入机械臂的端口号：', font=('微软雅黑',10), justify=tkinter.LEFT)
label_name.place(x=1550,y=100)
text6=tkinter.Text(win, width=30, height=1)
text6.pack()
text6.place(x=1550, y=130)

def exec_real():
    code_str = text2.get("1.0","end")
    ip_adders = text5.get("1.0","end")
    port = text6.get("1.0","end")
    if code_str == "\n":
        tkinter.messagebox.showinfo(title='提示！', message='您还没有生成指定代码！')
        return
    if ip_adders == "\n":
        tkinter.messagebox.showinfo(title='提示！', message='您还没有输入机械臂IP地址！')
        return
    if port == "\n":
        tkinter.messagebox.showinfo(title='提示！', message='您还没有输入机械臂端口号！')
        return
    
    #创建一个udp套件字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #使用套件字收发数据
    send_data=code_str
    #目标IP 和端口，元组类型
    ip_port = (ip_adders.strip(), int(port))
    udp_socket.sendto(send_data.encode('utf-8'),ip_port)
    #关闭套件字
    udp_socket.close()

btn2=tkinter.Button(win, bd=4, font=('微软雅黑',15), text="在虚拟环境中执行", command="")
btn2.pack()
btn2.place(x=800,y=50)

text3=tkinter.Text(win, width=100, height=30)
text3.pack()
text3.place(x=800, y=100)

btn3=tkinter.Button(win, bd=4, font=('微软雅黑',15), text="在真实环境中执行", command=exec_real)
btn3.pack()
btn3.place(x=800,y=520)



### 播放视频
app = tkinter.Frame(win, bg="white")
app.pack()
app.place(x=800,y=570)
# Create a label in the frame
lmian = tkinter.Label(app)
lmian.pack()

# Capture from camera
cap = cv2.VideoCapture('test.mp4')

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    img = img.resize((704, 396), Image.LANCZOS)
    imgtk = ImageTk.PhotoImage(image=img)
    lmian.imgtk = imgtk
    lmian.configure(image=imgtk)
    lmian.after(1, video_stream)

video_stream()


#显示作者信息
# label_name = tkinter.Label(win, text='姓名：李绍焜', font=('微软雅黑',20), justify=tkinter.LEFT)
# label_name.place(x=100,y=620)
# label_ID = tkinter.Label(win, text='学号：3120221325', font=('微软雅黑',20), justify=tkinter.LEFT)
# label_ID.place(x=100,y=660)
# label_School = tkinter.Label(win, text='学院：集成电路与电子学院', font=('微软雅黑',20), justify=tkinter.LEFT)
# label_School.place(x=100,y=700)

#设置退出按钮
button0 = tkinter.Button(win, bd=4, font=('微软雅黑',30), text="Exit", command=win.quit)
button0.place(x=1700,y=900)
win.mainloop()