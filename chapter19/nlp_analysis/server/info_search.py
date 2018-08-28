import requests
import re
import jieba
from chapter19.nlp_analysis.database import models
from bs4 import BeautifulSoup

# 请求头
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Cookie': 'appver=1.5.0.75771',
    'Content-Type': 'text/html',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

# url前缀
BAIDU_PRE = 'https://zhidao.baidu.com/'
# url前缀
BAIDU_SEARCH = 'search?word={}&ie=gbk&site=-1&sites=0&date=0&pn={}'


# 数据收集
def get_data_from_web(input_key_word, begin_page=None, end_page=None):
    for i in range(begin_page, end_page):
        if begin_page is not None and begin_page > 0 and i < begin_page - 1:
            continue

        search_url = (BAIDU_PRE + BAIDU_SEARCH).format(input_key_word, i * 10)
        print(f'当前爬取第({i})页，搜索url为:{search_url}')
        try:
            r = requests.get(search_url, headers=headers)
            status_code = r.status_code
            if status_code != 200:
                return

            req = BeautifulSoup(r.content.decode('gbk', 'ignore'), 'html5lib')
            result_item_val = req.find_all('div', re.compile('list-inner'))[0]
            result_item_list = result_item_val.find_all('div', re.compile('list'))[0]
            a_tag_list = result_item_list.find_all('a', re.compile('ti'))
            for a_tag_item in a_tag_list:
                if a_tag_item is None or a_tag_item == '':
                    continue

                href_val = str(a_tag_item.get('href'))
                if href_val is None or href_val == '':
                    continue
                # 问题标题
                question_title = a_tag_item.text
                # 最大取200个字符
                if len(question_title) > 200:
                    question_title = question_title[ : 200]
                # 问题答案
                question_answer = get_detail_info(href_val)
                if len(question_answer) > 500:
                    question_answer = question_answer[ : 500]
                # 问题标题分词结果
                fen_ci_result = jie_ba_fen_ci(question_title)
                if len(fen_ci_result) > 1000:
                    fen_ci_result = fen_ci_result[ : 1000]
                row_info_dict = dict()
                row_info_dict['question_title'] = question_title
                row_info_dict['question_answer'] = question_answer
                row_info_dict['fen_ci_result'] = fen_ci_result
                models.insert_record(row_info_dict, 'nlp_analysis')
        except Exception as ex:
            print(f'爬取第({i})页失败，失败原因：{ex}')
        print(f'第({i})页信息爬取结束。')


def get_detail_info(detail_suffix):
    detail_url = detail_suffix
    r = requests.get(detail_url, headers=headers)
    resp = BeautifulSoup(r.content.decode('gbk', 'ignore'), 'html5lib')
    detail_text_list = resp.find_all('div', re.compile('best-text'))
    if detail_text_list is None or detail_text_list.__len__() <= 0:
        return ''

    question_answer = str(detail_text_list[0].text).strip()

    return question_answer


# jie ba分词
def jie_ba_fen_ci(input_val):
    # 搜索引擎模式
    result_list = jieba.cut_for_search(input_val)
    result_val = ','.join(result_list)
    return result_val


if __name__ == "__main__":
    # 从网站取得数据并存储到数据库
    get_data_from_web('', 0, 1)
