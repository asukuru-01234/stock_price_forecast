import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import mplfinance as mpf
from PIL import Image

def dataframe_to_img(chart_range, img_name, df=None):
    df = df[0:chart_range]
    mpf.plot(df, type="candle", show_nontrading=False, volume=False, title="", xlabel="", ylabel="",  datetime_format='',figsize=(4,2),savefig=dict(fname=img_name,dpi=50))
    #mpf.plot(df, type="candle", show_nontrading=False, volume=False, title="", xlabel="", ylabel="",  datetime_format='',figsize=(8,4),savefig=dict(fname=img_name,dpi=70))

#csvをarrayに読み込む
arr = pd.read_csv('data.csv')

#DataFrameに変換
col_name = ["Date","Open","High","Low","Close"]
df = pd.DataFrame(arr,columns=col_name)

#日付をIndex
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

#行数カウント
count = len(df)

# 画像に含まれる日足
chart_range = 5

# 画像数
#count - chart_range
for i in range(count - chart_range + 1):
    try:
        img_name = str(i) + '.png'
        dataframe_to_img(chart_range, img_name, df=df[i:chart_range+i])
        im = Image.open(img_name)
        im_crop = im.crop((35,10,182,85))
        #im_crop = im.crop((105,35,505,230))
        im_crop.save(img_name, quality=100)
    except IndexError:
        pass
