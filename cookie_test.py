import requests

cookies = {
    'CASTGC': 'TGT-7053-19mbTcuP14JMoBAlwY1IRo0y1UbV6phqbm9Bhtiiv2fogeUrOl-cas',
    'theusername': 'wxjtj'
}


if __name__ == '__main__':
    ret = requests.get('http://202.103.199.210:8070/nnxmgl/nnwebsite/index.jspx', cookies=cookies)
    print(ret.text)
