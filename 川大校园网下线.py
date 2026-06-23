import requests
import re

def getLoginMsg():
    url = 'http://192.168.2.135'
    r = requests.get(url=url)
    try:
        pattern = "href='(\S+)'"
        href = re.search(pattern=pattern, string=r.text).group(1)
    except TypeError:
        print('你已在线')
    destination = href.split('?')[0]  # 跳转目标url
    params = href.split('?')[1]  # params字符串
    return params
def logout():
    url = 'http://192.168.2.135/eportal/InterFace.do?method=logout'

    # 获取当前登录状态信息
    try:
        paramstr = getLoginMsg()
    except:
        paramstr = ""

    data = {
        "queryString": paramstr,
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": ""
    }

    r = requests.post(url=url, data=data)
    result = r.json()

    if result.get("result") == "success":
        print("登出成功")
        return True
    else:
        print("登出失败:", result.get("message", "未知错误"))
        return False


# 可以直接调用登出函数
if __name__ == "__main__":
    logout()