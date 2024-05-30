# LLM_Robotics

## ChatGLM API 部署流程

### 1.拉取github项目
```shell
git clone https://github.com/THUDM/ChatGLM2-6B
```

### 2.下载模型到本地，将下载好的模型文件存放到新建的model文件夹中，model文件夹放到ChatGLM2-6B目录下
- 链接：https://pan.baidu.com/s/11DXurqKc_RzCjfITRxu5EQ?pwd=f55v#list/path=%2F
- 提取码：f55v

### 3.将模型路径修改为model所在路径，显存不够时（即 GPU 显存有限，低于13GB），尝试以量化方式加载模型的，需要添加代码 .quantize(8) 或 .quantize(4) ：
- int8精度加载，需要10G显存；
- int4精度加载，需要6G显存；
```python
tokenizer = AutoTokenizer.from_pretrained("C:\\Users\\***\\Desktop\\ChatGLM2-6B\\model", trust_remote_code=True)     # THUDM/chatglm2-6b
model = AutoModel.from_pretrained("C:\\Users\\***\\Desktop\\ChatGLM2-6B\\model", trust_remote_code=True).quantize(4).cuda()
```

### 4.安装依赖
```shell
pip install -r requirements.txt
```

### 5.关闭服务器本机防火墙
<div align=center><img src="images/关闭防火墙.png" ></div>

### 6.新建服务器本机入站规则
<div align=center><img src="images/新建入站规则1.png" ></div>
<div align=center><img src="images/新建入站规则2.png" ></div>

### 7.编写客户端访问程序
```python
import requests
url = 'http://127.0.0.1:8000'
headers = {
    'Content-Type': 'application/json',
}
data = "{\"prompt\": \"此处写你的自然语言指令\", \"history\": []}"
response = requests.post(url, headers=headers, data=data.encode('utf-8'))
print(response)
print(response.content.decode('utf-8'))
```

### 8.开启服务器api
```shell
python api.py
```

### 9.运行客户端程序
```shell
python API_GLM.py
```

## ChatGLM 控制机械臂运动
通过将大象机械臂的 API 接口说明以 Prompt 的形式传递给大模型，大模型利用这些接口以及自身的多级任务规划能力，完成抓取放置操作
<div align=center><img src="images/1.png"  width="20%"> <img src="images/2.png"  width="20%"> <img src="images/3.png"  width="20%"></div>
<div align=center><img src="images/4.png"  width="30%"> <img src="images/5.png"  width="30%"></div>
<div align=center></div>

## 基于百度千帆大模型平台编写 GUI 界面，可视化生成的控制程序
```shell
python LLM_Robotics_GUI_Qianfan.py
```

<div align=center><img src="images/6.png" ></div>
