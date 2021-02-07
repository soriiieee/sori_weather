# -*- coding: utf-8 -*-
# when   : 2020.0x.xx
# who : [sori-machi]
# what : [ ]
#---------------------------------------------------------------------------
# basic-module
import matplotlib.pyplot as plt
import sys,os,re,glob
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.simplefilter('ignore')
from tqdm import tqdm
import seaborn as sns
#---------------------------------------------------
# sori -module
sys.path.append('/home/ysorimachi/tool')
# from getErrorValues import me,rmse,mae,r2 #(x,y)
# from convSokuhouData import conv_sfc #(df, ave=minutes,hour)
# #amedas relate 2020.02,04 making...
# from tool_AMeDaS import code2name, name2code
# from tool_110570 import get_110570,open_110570
# from tool_100571 import get_100571,open_100571
#(code,ini_j,out_d)/(code,path,csv_path)
#---------------------------------------------------
import subprocess

import quandl
import torch
from torch.autograd import Variable


"""
2021.02.07 start
https://qiita.com/creaith/items/2d606a7f0effd5d839d5
"""


class GetData:
  def __init__(self,n_prev, data_code):
    self.n_prev = n_prev
    # self.data = quandl.get(data_code, start_date = "2017/07/01",end_date = "2019/07/25")
    self.data = quandl.get(data_code)

  def get_data(self,today):
    tmpX,tmpY=[],[]
    print(today)

    for k in range(self.n_prev):
      tmpX.append(self.data[today - self.n_prev + k][1])
    
    tmpY.append(self.data[today][1])
    return
  
  def get_raw_data(self):
    return self.data

  def preprocess(self, df):
    df["Date"] = pd.to_datetime(df["Date"])
    use_col = ["Date","Close","Volume"]
    df =df[use_col]
    return df

# class MakeDataSet:
#   def __init__(self,)

if __name__ == "__main__":

  n_prev = 30
  hidden_size = 300
  cell_size=100
  epochs=5

  gd = GetData(n_prev, "WIKI/AAPL")
  if not os.path.exists("../dat/stock.csv"):
    print("not found getting..")
    data = gd.get_raw_data()
    data.to_csv("../dat/stock.csv")
  else:
    print("already getting..")
    data = pd.read_csv("../dat/stock.csv")
    pass



