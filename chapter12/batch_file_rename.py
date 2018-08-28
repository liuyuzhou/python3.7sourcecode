#-*- coding:UTF-8 -*-
import os
import time

#  批量文件重命名
def batch_rename(path):
    global img_num
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False

    if os.path.isfile(path):
        # 分割出目录与文件
        file_path = os.path.split(path)
        # 分割出文件与文件扩展名
        lists = file_path[1].split('.')
        # 取出后缀名(列表切片操作)
        file_ext = lists[-1]
        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
        if file_ext in img_ext:
            os.rename(path, file_path[0] + '/' + lists[0] + '_cn.' + file_ext)
            img_num += 1
    elif os.path.isdir(path):
        for item in os.listdir(path):
            # 递归调用
            batch_rename(os.path.join(path, item))

if __name__ == "__main__":
    img_dir = 'F:\\download\\vpn'
    img_dir = img_dir.replace('\\','/')
    start = time.time()
    img_num = 0
    batch_rename(img_dir)
    print('总共处理了 %s 张图片，耗时：%0.2f.' % (img_num, time.time() - start))
