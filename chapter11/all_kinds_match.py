# -*- coding:UTF-8 -*-
import re

# 匹配目标
def target_match(content):
    result = re.match('^Hello\s(\d+)\sWorld', content)
    return result, result.group(), result.group(1), result.span()

# 通用匹配
def gena_match(content):
    result = re.match('^Hello.*Demo$', content)
    return result, result.group(), result.span()

# 贪婪匹配
def greed_match(content):
    result = re.match('^He.*(\d+).*Demo$', content)
    return result, result.group(1)

# 非贪婪匹配
def un_greed_match(content):
    result = re.match('^He.*(\d+).*Demo$', content)
    return result, result.group(1)

if __name__ == "__main__":
    con_match = 'Hello 1234567 World_This is a Regex Demo'
    target_match(con_match)
    gena_match(con_match)
    greed_match(con_match)
    result_v, result_group = un_greed_match(con_match)
    print(result_v, result_group)
