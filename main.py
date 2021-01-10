# -*- coding: utf-8 -*-
import requests
import json
import datetime


# 请求 URL: http://hdjw.hnu.edu.cn/secService/login
def jwxt_login(username, password):
    # print("开始模拟登录jwxt")
    post_url = "http://hdjw.hnu.edu.cn/secService/login"
    post_data = {
        "password": password,
        "userCode": username,
        "kaptcha": "testa",
        "userCodeType": "account"
    }
    login_header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "app": "PCWEB",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "hdjw.hnu.edu.cn",
        "KAPTCHA-KEY-GENERATOR-REDIS": "securityKaptchaRedisServiceAdapter",
        "locale": "zh_CN",
        "Origin": "http://hdjw.hnu.edu.cn",
        "Referer": "http://hdjw.hnu.edu.cn/Njw2017/login.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63",
        "X-Requested-With": "XMLHttpRequest"
    }
    response_res = requests.post(post_url, data=json.dumps(post_data), headers=login_header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    # print(f"statusCode = {response_res.status_code}")
    # print(f"statusText = {response_res.text}")
    # print("statusText =",
    # json.dumps(response_res.json(), sort_keys=True, indent=4, separators=(',', ': ',), ensure_ascii=False))
    if response_res.json()["errorCode"] != "success":
        print("登陆失败！程序退出~")
        print("友情提醒：1、核验info.txt的信息是否正确，如不正确，使用get_parameter工具再次生成,尽量避免手动填写")
        print("        2、教务系统存在密码错误保护机制，多次输错密码要求输入验证码，验证码识别机制咸鱼还在做~")
        exit(0)
    return str(response_res.json()["data"]["token"]), response_res.cookies


def search_pkgl002(semester, token, cookies):
    post_url = "http://hdjw.hnu.edu.cn/resService/jwxtpt/v1/xsd/xsdjsjygl_info/searchPkgl002List?" \
               "resourceCode=XSMH0702&apiCode=jw.xsd.xsdInfo.controller.XsdJsjyglController.searchPkgl002List"
    post_data = {
        "jczy013id": semester
    }
    pkgl002_header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "app": "PCWEB",
        "Cache-Control": "no-cache",
        "Content-Length": "27",
        "Content-Type": "application/json",
        "Host": "hdjw.hnu.edu.cn",
        "locale": "zh_CN",
        "Origin": "http://hdjw.hnu.edu.cn",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://hdjw.hnu.edu.cn/Njw2017/index.html",
        "Simulated-By": "",
        "TOKEN": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63",
        "userAgent": "",
        "userRoleCode": "student",
        "X-Requested-With": "XMLHttpRequest"
    }
    response_res = requests.post(post_url, data=json.dumps(post_data), headers=pkgl002_header, cookies=cookies)
    # print(f"statusCode = {response_res.status_code}")
    # print(f"text = {response_res.text}")
    # print(json.dumps(response_res.json(), sort_keys=True, indent=4, separators=(',', ': ',), ensure_ascii=False))
    table = []
    for i in [0, 1, 2, 3, 4]:
        table.append(response_res.json()["data"][0]["pkgl00201List"][i]["dyname"]
                     + " "
                     + response_res.json()["data"][0]["pkgl00201List"][i]["zyxjs"]
                     + " "
                     + response_res.json()["data"][0]["pkgl00201List"][i]["djkssj"]
                     + "-"
                     + response_res.json()["data"][0]["pkgl00201List"][i]["djjssj"]
                     )
    return response_res.json()["data"][0]["id"], table


def search_one_xskb(semester, pkgl002id, token, cookies):
    # print("开始模拟查找——>学生门户——>我的选课——>课表查看")
    post_url = "http://hdjw.hnu.edu.cn/resService/jwxtpt/v1/xsd/xsdqxxkb_info/searchOneXskbList?" \
               "resourceCode=XSMH0701&apiCode=jw.xsd.xsdInfo.controller.XsdQxxkbController.searchOneXskbList"
    post_data = {
        "jczy013id": semester,
        "pkgl002id": pkgl002id
    }
    xskb_header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "app": "PCWEB",
        "Cache-Control": "no-cache",
        "Content-Length": "56",
        "Content-Type": "application/json",
        "Host": "hdjw.hnu.edu.cn",
        "locale": "zh_CN",
        "Origin": "http://hdjw.hnu.edu.cn",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://hdjw.hnu.edu.cn/Njw2017/index.html",
        "Simulated-By": "",
        "TOKEN": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63",
        "userAgent": "",
        "userRoleCode": "student",
        "X-Requested-With": "XMLHttpRequest"
    }
    response_res = requests.post(post_url, data=json.dumps(post_data), headers=xskb_header, cookies=cookies)
    # print(f"statusCode = {response_res.status_code}")
    # print(f"text = {response_res.text}")
    content = []
    for i in response_res.json()["data"]:
        # print((i["pkzcmx"].ljust(40, " "), i["pksjshow"][0:3], i["djkssj"] + "-" + i["djjssj"], i["js_name"],
        #                 i["teachernames"].center(8, " "), i["kc_name"]))
        if i["pksjshow"][1:2] == "一":
            content.append([i["pkzcmx"], i["pksjshow"], i["djkssj"] + "-" + i["djjssj"], i["js_name"] + " " +
                            i["teachernames"] + " " + i["kc_name"]])
    for i in response_res.json()["data"]:
        if i["pksjshow"][1:2] == "二":
            content.append([i["pkzcmx"], i["pksjshow"], i["djkssj"] + "-" + i["djjssj"], i["js_name"] + " " +
                            i["teachernames"] + " " + i["kc_name"]])
    for i in response_res.json()["data"]:
        if i["pksjshow"][1:2] == "三":
            content.append([i["pkzcmx"], i["pksjshow"], i["djkssj"] + "-" + i["djjssj"], i["js_name"] + " " +
                            i["teachernames"] + " " + i["kc_name"]])
    for i in response_res.json()["data"]:
        if i["pksjshow"][1:2] == "四":
            content.append([i["pkzcmx"], i["pksjshow"], i["djkssj"] + "-" + i["djjssj"], i["js_name"] + " " +
                            i["teachernames"] + " " + i["kc_name"]])
    for i in response_res.json()["data"]:
        if i["pksjshow"][1:2] == "五":
            content.append([i["pkzcmx"], i["pksjshow"], i["djkssj"] + "-" + i["djjssj"], i["js_name"] + " " +
                            i["teachernames"] + " " + i["kc_name"]])
    for i in response_res.json()["data"]:
        if i["pksjshow"][1:2] == "六":
            content.append([i["pkzcmx"], i["pksjshow"], i["djkssj"] + "-" + i["djjssj"], i["js_name"] + " " +
                            i["teachernames"] + " " + i["kc_name"]])
    for i in response_res.json()["data"]:
        if i["pksjshow"][1:2] == "日":
            content.append([i["pkzcmx"], i["pksjshow"], i["djkssj"] + "-" + i["djjssj"], i["js_name"] + " " +
                            i["teachernames"] + " " + i["kc_name"]])
    new_content = []
    for i in content:
        if i not in new_content:
            new_content.append(i)
    return new_content


def date_add(start_date, days):
    d = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    delta = datetime.timedelta(days=days)
    n_days = d + delta
    return n_days.strftime('%Y-%m-%d')


def handle_time(start_date, content):
    for i in content:
        if i[1][1:2] == "一":
            week_day = 1
        elif i[1][1:2] == "二":
            week_day = 2
        elif i[1][1:2] == "三":
            week_day = 3
        elif i[1][1:2] == "四":
            week_day = 4
        elif i[1][1:2] == "五":
            week_day = 5
        elif i[1][1:2] == "六":
            week_day = 6
        elif i[1][1:2] == "日":
            week_day = 7
        else:
            week_day = 0
        week_str = i[0].split(",")
        week_num = []
        for j in week_str:
            week_num.append(date_add(start_date, (int(j) - 1) * 7 + week_day - 1))
        i[0] = week_num
        # print(i)
    return content


def convert_to_one_by_one(content):
    course_list = []
    for i in content:
        for j in i[0]:
            course_list_item = list()
            course_list_item.append(j)
            for k in i:
                if k != i[0]:
                    course_list_item.append(k)
            # print(course_list_item)
            course_list.append(course_list_item)
            # print(course_list)
    # for i in course_list:
    #     print(i)
    return course_list


def get_parameter():
    file = open("./dist/info.txt", "r")
    username = file.readline()
    password = file.readline()
    semester = file.readline()
    start_date = file.readline()
    today = file.readline()
    file.close()
    username = username[0:len(username)-1]
    password = password[0:len(password) - 1]
    semester = semester[0:len(semester) - 1]
    start_date = start_date[0:len(start_date) - 1]
    today = today[0:len(today) - 1]
    print("学号 ", username)
    print("密码 ", password)
    print("学期 ", semester)
    print("对应学期校历第一天（第一周前的那个周日）", start_date)
    print("你要查的那一天 ", today)
    return username, password, semester, start_date, today


def main_factory():
    print("***********************************等待参数*********************************************")
    username, password, semester, start_date, today = get_parameter()
    print("***********************************等待结束*********************************************")
    print()
    print("***********************************尝试登录*********************************************")
    token, cookies = jwxt_login(username, password)
    # print("得到token:", token)
    # print("得到cookie(字符串）:", cookies)
    # print("得到cookie(字典):", requests.utils.dict_from_cookiejar(cookies))
    print("***********************************登录成功*********************************************")
    print()
    print("***********************************课表格式*********************************************")
    pkgl002id, table = search_pkgl002(semester, token, cookies)
    for i in table:
        print(i)
    print("***********************************格式完成*********************************************")
    print()
    print("***********************************课表内容*********************************************")
    content = search_one_xskb(semester, pkgl002id, token, cookies)
    # s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
    # print (s)
    # print (s.keys())
    # print (s["name"])
    # print (s["type"]["name"])
    # print (s["type"]["parameter"][1])
    print("***********************************内容成功*********************************************")
    print()
    print("***********************************解析内容*********************************************")
    content = handle_time(start_date, content)
    print("***********************************解析成功*********************************************")
    print()
    print("***********************************转换条目*********************************************")
    course_list = convert_to_one_by_one(content)
    print("***********************************转换成功*********************************************")
    print()
    print("***********************************排序条目*********************************************")
    course_list.sort(key=lambda elem: (elem[0], elem[2]))
    for i in course_list:
        print(i)
    print("***********************************排序成功*********************************************")
    print()
    print("***********************************今日课表*********************************************")
    print(today)
    for i in course_list:
        if i[0] == today:
            print(i)
    print("***********************************获取成功*********************************************")


def main():
    main_factory()


if __name__ == "__main__":
    main()
