# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/9 9:39
desc:
"""
import os
files = os.listdir("E://2文件下载/SogouCS")  # 获取当前目录下的文件
from chardet.universaldetector import UniversalDetector


def get_encode_info(file):
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']


def read_file(file):
    with open(file, 'rb') as f:
        return f.read()


def write_file(content, file):
    with open(file, 'wb') as f:
        f.write(content)


def convert_encode2utf8(file, original_encode, des_encode):
    file_content = read_file(file)
    file_decode = file_content.decode(original_encode, 'ignore')
    file_encode = file_decode.encode(des_encode)
    write_file(file_encode, file)


if __name__ == "__main__":
    for filename in files:
        print(filename)
        file_content = read_file(filename)
        encode_info = get_encode_info(filename)
        if encode_info != 'utf-8':
            convert_encode2utf8(filename, encode_info, 'utf-8')
        encode_info = get_encode_info(filename)
        print(encode_info)