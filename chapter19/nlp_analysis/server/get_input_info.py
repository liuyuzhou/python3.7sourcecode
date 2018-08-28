BAIDU_MAX_PAGE_NUM = 70


def get_input_data():
    input_str = input("请输入关键词：")
    input_str = input_str.strip()
    while input_str is None or input_str == '':
        input_str = input("请输入关键词：")

    begin_page = input("请输入起始页码(页码必须为大于等于0的数字，"
                       "不输入直接按Enter，默认为0)：")
    begin_page = begin_page.strip()
    if begin_page is None or begin_page == '':
        begin_page = 0
    while number_judge(begin_page) is False:
        begin_page = input("输入不是数字，请输入起始页码(页码必须为大于"
                           "等于0的数字，默认为0)：")

    end_page = input("请输入结束页码(结束页码必须大于等于起始页码，最大为{}，"
                     "不输入直接按Enter，默认为最大值。超过最大值，"
                     "以最大值算)：".format(BAIDU_MAX_PAGE_NUM))
    end_page = end_page.strip()
    if end_page is None or end_page == '':
        end_page = BAIDU_MAX_PAGE_NUM
    while number_judge(end_page) is False:
        end_page = input("输入不是数字，请输结束页码：")
    if int(end_page) > BAIDU_MAX_PAGE_NUM:
        end_page = BAIDU_MAX_PAGE_NUM

    begin_page = int(begin_page)
    end_page = int(end_page)
    if begin_page < 0:
        begin_page = 0

    if end_page <= begin_page:
        end_page = begin_page + 1

    print(f'起始页码为：{begin_page}，结束页码为：{end_page}')
    return input_str, begin_page, end_page


def number_judge(input_val):
    try:
        float(input_val)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(input_val)
        return True
    except (TypeError, ValueError):
        pass

    return False