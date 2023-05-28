from PIL import Image
import imagehash
import os
import pandas as pd

# the total list of images
target_files = os.listdir('target_png/')
source_files = os.listdir('source_png/')

for file in target_files:
    target_hash =  imagehash.phash(Image.open('target_png/'+file))

# 画像と差分をまとめる
image_hash = {}

for file in source_files:
    try:
        img_name = 'source_png/' + file
        source_hash =  imagehash.phash(Image.open(img_name))
        hamming = target_hash - source_hash
        image_hash[img_name] = hamming
    except IndexError:
        pass

dic = sorted(image_hash.items(),key=lambda x:x[1],reverse=True)
print(dic)
