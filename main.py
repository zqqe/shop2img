import execjs
import requests
import json
import random


# 随机生成token，不重要
def generate_random_id():
    def s4():
        return hex(random.randint(0x1000, 0xFFFF))[2:]

    return s4() + s4() + "-" + s4() + "-" + s4() + "-" + s4() + "-" + s4() + s4() + s4()

# js文件路径
with open("md5.js", "r") as f:
    js_file = f.read()
sign = execjs.compile(js_file).call("createsign")


url = "" # 网站图片上传地址
headers = {
    "Conteny-Type": "multipart/form-data",
    "Sign": sign[0],
    "Source": "h5",
    "Timestamp": sign[1],
    "Token": generate_random_id(),
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
}

files = {
    "file": (
        "{}.jpg".format(generate_random_id()),
        open("E:\\Google\\1.jpg", "rb"), # 文件路径
        "image/jpeg/jpg/png",
    )
}
res = requests.post(url, files=files, headers=headers).text
res_json = json.loads(res)
print(res_json)
