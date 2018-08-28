other = {'城市': '北京', '爱好': '编程'}
def per_info(name, number, **kw):
    print(f'名称:{name},学号:{number},其他:{kw}')

per_info('小智', 1002, 城市=other['城市'], 爱好=other['爱好'])

per_info('小智', 1002, **other)