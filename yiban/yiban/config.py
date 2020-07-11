import os

_BASE_PATH = os.path.split(os.path.abspath(__file__))[0]
CONFIG_TXT = os.path.join(_BASE_PATH, '../config.txt')

# 手机号-密码
ACCOUNT = ''
PASSWD = ''

# 近几天的一次易班打卡登记表的转发审批表单的链接
# 需要替换此链
with open(CONFIG_TXT) as f:
    url = f.read().strip()
