from yiban import yb

if __name__ == '__main__':
    if yb.login() is None:
        print("帐号或密码错误")
    result_auth = yb.auth()
    UncompletedList = yb.getUncompletedList()
    print("未打卡的任务:")
    print(UncompletedList.get('data'))
