import base64
import os

src = input('Base64 图片代码：')
data = src.split(',')[1]
image_data = base64.b64decode(data)

with open('Output.png', 'wb') as f:
    f.write(image_data)

print('完成')