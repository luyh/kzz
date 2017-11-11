#coding=utf-8
import urllib

users = ['luyh','heml']

stokc = ''
amount = 10000
price = 100

try:
    import easytrader
    # 设置easytrader,需在windows下安装银河客户端，详见easystockr说明
    user = easytrader.use( 'yh_client' )  # 银河客户端支持 ['yh_client', '银河客户端']

    for _user in users
        user.prepare( 'users/%s.json',_user )  # 配置文件路径
        user.buy( stock, price, amount )
        user.exit()

except:
    print(u'请检查客户端或easystockr设置')

