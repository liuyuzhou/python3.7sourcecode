def func_filter(x):
    return x>3
f_list=filter(func_filter,[1,2,3,4,5])
print('列表中大于3的元素有：',[item for item in f_list])
