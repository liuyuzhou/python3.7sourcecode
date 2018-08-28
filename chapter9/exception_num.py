# -*- coding:UTF-8 -*-

num_list = [5,0,73,0,16]


class ExceptionNum(object):
    def __init__(self):
        pass


    @staticmethod
    def num_operation():
        # 正常数数组
        normal_num_list = list()
        # 异常数数组
        exp_num_list = list()
        for item in range(num_list.__len__()):
            if item == num_list.__len__() - 1:
                divisor_num, dividend_num = num_list[item], num_list[item]
            else:
                # divisor_num除数, dividend_num被除数
                divisor_num, dividend_num = num_list[item + 1], num_list[item]
            try:
                divisor_num / dividend_num
                rt_str = '第' + str(item + 1) + '个是正常数，值：' + str(num_list[item])
                normal_num_list.append(rt_str)
            except ZeroDivisionError as ex:
                exp_num = SelfDefineError(num_list[item]).__int__()
                rt_str = '第' + str(item + 1) + '个是异常数，值：' + str(exp_num)
                exp_num_list.append(rt_str)
                print(SelfDefineError(num_list[item]).__str__())

        return normal_num_list, exp_num_list


class SelfDefineError(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return 'error info:The dividend num equals zero.'

    def __int__(self):
        return self.num

if __name__ == "__main__":
    normal_num_list, exp_num_list = ExceptionNum().num_operation()
    print(f'正常数数组：{normal_num_list}')
    print(f'异常数数组：{exp_num_list}')
