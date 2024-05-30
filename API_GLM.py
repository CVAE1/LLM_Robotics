'''
    curl -X POST "http://127.0.0.1:8000" -H "Content-Type: application/json" -d "{\"prompt\": \"你好\", \"history\": []}"

    {
        "response":"你好👋！我是人工智能助手 ChatGLM2-6B，很高兴见到你，欢迎问我任何问题。",
        "history":[["你好","你好👋！我是人工智能助手 ChatGLM2-6B，很高兴见到你，欢迎问我任何问题。"]],
        "status":200,
        "time":"2023-03-23 21:38:40"
    }
'''

'''
    1.首先通过下列两个语句导入MyCobot类以及两个变量：from pymycobot.mycobot import MyCobot、from pymycobot import PI_PORT, PI_BAUD。初始化MyCobot类时要将两个变量作为参数传进去，形式为MyCobot(PI_PORT, PI_BAUD)。MyCobot类下的set_color(r, g, b)可以设置机械臂上灯光的颜色，其中r、g、b均为整数型参数，当r=255,g=0,b=0时灯光为红色，当r=0,g=255,b=0时灯光为绿色，当r=0,g=0,b=255时灯光为蓝色。请你给出一段代码，将mycobot机械臂上的灯光颜色设置为红色，间隔0.5秒后进入循环，设置为绿色，再间隔0.5秒设置为蓝色，再间隔0.5秒设置为红色，再间隔0.5秒进入下一次循环。
    2.首先通过下列两个语句导入MyCobot类以及两个变量：from pymycobot.mycobot import MyCobot、from pymycobot import PI_PORT, PI_BAUD。初始化MyCobot类时要将两个变量作为参数传进去，形式为MyCobot(PI_PORT, PI_BAUD)。MyCobot类下的send_angles(degrees, speed)可以控制机械臂的6个关节按照指定速度进行旋转，如send_angles([0, 0, 0, 0, 0, 0], 30)表示机械臂以速度30将6个关节旋转到默认位置。请你给出一段代码，使机械臂以速度40将6个关节旋转到到默认位置。
    3.首先通过下列两个语句导入MyCobot类以及两个变量：from pymycobot.mycobot import MyCobot、from pymycobot import PI_PORT, PI_BAUD。初始化MyCobot类时要将两个变量作为参数传进去，形式为MyCobot(PI_PORT, PI_BAUD)。MyCobot类下的send_coords(coords, speed, mode)可以控制机械臂头部按照指定速度进行移动，如send_coords([57.0, -107.4, 316.3, -93.81, -12.71, -163.49], 80, 1)表示机械臂头部以速度80到达[58.0, -107.4, 316.3, -93.81, -12.71, -163.49]这个位姿。请你给出一段代码，使机械臂头部以速度30到达[57.0, -107.4, 316.3, -93.81, -12.71, -163.49]这个位姿。
    4.
'''

import requests
import json

url = 'http://127.0.0.1:8000'
headers = {
    'Content-Type': 'application/json',
}
data = "{\"prompt\": \"首先通过下列两个语句导入MyCobot类以及两个变量：from pymycobot.mycobot import MyCobot、from pymycobot import PI_PORT, PI_BAUD。初始化MyCobot类时要将两个变量作为参数传进去，形式为MyCobot(PI_PORT, PI_BAUD)。MyCobot类下的send_coords(coords, speed, mode)可以控制机械臂头部按照指定速度进行移动，如send_coords([57.0, -107.4, 316.3, -93.81, -12.71, -163.49], 80, 1)表示机械臂头部以速度80到达[58.0, -107.4, 316.3, -93.81, -12.71, -163.49]这个位姿。MyCobot类下的get_coords()可以获取机械臂头部当前坐标和姿态。在控制机械臂头部按照指定速度进行移动前必须调用get_coords()获取机械臂头部当前坐标和姿态。MyCobot类下的set_gripper_state(flag, speed)可以控制机械臂夹爪合拢或打开，如set_gripper_state(1, 50)表示机械臂夹爪以速度50合拢，set_gripper_state(0, 50)表示机械臂夹爪以速度50打开。请你给出一段代码，初始化机械臂夹爪打开，然后控制机械臂头部以速度30到达[57.0, -107.4, 316.3, -93.81, -12.71, -163.49]这个位姿，经过3秒后控制机械臂夹爪合拢。\", \"history\": []}"
response = requests.post(url, headers=headers, data=data.encode('utf-8'))
print(response)
print(json.loads(response.content.decode('utf-8'))['response'])