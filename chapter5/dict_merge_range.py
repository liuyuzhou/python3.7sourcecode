def merge_range():
    lan_ver = {"lan": "python", "v": "3.7"}
    rea_ai = {"why": "hobby", "how": "do"}
    d_merge = dict()
    d_merge.update(lan_ver)
    d_merge.update(rea_ai)

    desc_list = sorted(dt2ls(d_merge), key=lambda x:x[0], reverse=True)
    desc_dict = dict(desc_list)
    asc_list = sorted(dt2ls(d_merge), key=lambda x:x[0], reverse=False)
    asc_dict = dict(asc_list)

    print(f'合并后的结果：{d_merge}')
    print(f'按照第0个元素降序排列：{desc_dict}' )
    print(f'按照第0个元素升序排列：{asc_dict}' )


def dt2ls(dic:dict):
    """ 将字典转化为列表 """
    keys = dic.keys()
    values = dic.values()
    lst = [(key, val) for key, val in zip(keys, values)]
    return lst

merge_range()