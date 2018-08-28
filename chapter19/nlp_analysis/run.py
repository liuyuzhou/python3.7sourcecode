from chapter19.nlp_analysis.server.get_input_info import get_input_data
from chapter19.nlp_analysis.server.info_search import get_data_from_web
from chapter19.nlp_analysis.server.word_count import word_count


if __name__ == "__main__":
    # 取得输入参数
    input_key_word, begin_page, end_page = get_input_data()
    # 从网站取得数据并存储到数据库
    get_data_from_web(input_key_word, begin_page, end_page)
    # 词频统计并生成统计图
    word_count()