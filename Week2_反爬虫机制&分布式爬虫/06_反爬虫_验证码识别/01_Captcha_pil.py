# 先安装依赖库libpng, jpeg, libtiff, leptonica
# brew install leptonica
# 安装tesseract
# brew install tesseract
# 与python对接需要安装的包
# pip3 install pillow
# pip3 install pytesseract

# import os
import requests
from PIL import Image
import pytesseract
from fake_useragent import UserAgent

# 下载图片
session = requests.session()
img_url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1320441599' \
          ',4127074888&fm=26&gp=0.jpg'
agent = UserAgent(verify_ssl=False)  # 关闭ssl验证
user_agent = agent.random
header = {'User-Agent': user_agent}
r = session.get(img_url, headers=header)
print(type(r))
with open('cap.jpg', 'wb') as f:
    f.write(r.content)

# 打开并显示文件
image = Image.open('cap.jpg')
# image.show()

# 灰度图片
gray = image.convert('L')
gray.save('c_gray2.jpg')
image.close()

# 二值化
threshold = 100  # 设定一个阈值
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
out.save('c_th.jpg')

th = Image.open('c_th.jpg')
th.show()
print(pytesseract.image_to_string(th, lang='chi_sim+eng'))

# 各种语言识别库 https://github.com/tesseract-ocr/tessdata
