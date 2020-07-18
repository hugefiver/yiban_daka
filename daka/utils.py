import json
from random import choices

import requests

_BASE_CHARS = r'0123456789abcdefghijklmnopqrstuvwxyz' \
              r'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def rand_str(length: int) -> str:
    return ''.join(choices(_BASE_CHARS, k=length))


def parse_data(url):
    """
    :param url
    将分享链接的数据解析出来生成表单数据字典
    """
    from daka.yiban import yb

    initiateId = url.split('=')[-1]
    # print(initiateId)
    share_url = 'https://api.uyiban.com/workFlow/c/share/index?InitiateId={}&CSRF={}'.format(initiateId, yb.CSRF)
    share_res = yb.request(share_url, cookies=yb.COOKIES)
    save_data_url = share_res.get('data')['uri']
    save_data_res = requests.get(save_data_url)
    save_data = save_data_res.json()
    FormDataJson = save_data.get('Initiate')['FormDataJson']
    dict_form = {i.get('id'): i.get("value") for i in FormDataJson}
    # if '8992cd6ce8968fb4e7e75089fd73b641' not in dict_form:
    #     dict_form['8992cd6ce8968fb4e7e75089fd73b641'] = '否'
    return json.dumps(dict_form)


# 最终提交的表单数据
from daka.yiban.config import url
form_data = parse_data(url)

if __name__ == '__main__':
    # 打印表单提取的数据
    print(json.loads(form_data))
