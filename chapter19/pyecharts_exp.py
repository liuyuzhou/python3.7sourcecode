import os
from pyecharts import Bar


# 水平横条
bar = Bar("Python 3.7 从零开始学", "按城市统计")
bar.add("阅读人数分布", ["北京", "上海", "广州", "深圳", "杭州", "成都"],
        [500, 450, 360, 450, 355, 380])
# 打印设置参数信息
bar.show_config()
bar.render(path=os.getcwd() + '/static/' + "pyecharts_exp.html")
