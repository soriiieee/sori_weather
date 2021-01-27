import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta
from pdf2image import convert_from_path, convert_from_bytes
import cv2
import glob
from tqdm import tqdm

def pdf2img(inpath, outpath):
  img = convert_from_path(inpath)
  img[0].save(outpath, "png")
  return

def read_files():
  tbl_path = f"../tbl/list_time.dat"
  tl = list(pd.read_csv(tbl_path, delim_whitespace=True, header=None)[0].values)
  _f = [os.path.basename(f) for f in tl]
  _f = sorted(_f)
  return _f

def main():
  """
  #reference... https://yakumo-takaya.hatenablog.jp/entry/2019/10/14/000000
  """

  _f = read_files()  #fine name get
  _img = []
  name = '/Users/soriiieee/Desktop/g3.avi'
  h, w = 581, 600
  fps = 2
  out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
  fps, (w, h))

  for f in _f:
    input_path = f"../dat/g3/{f}"
    if os.path.exists(input_path):
      img = cv2.imread(f"../dat/g3/{f}")
      h, w, l = img.shape
      out.write(img)
      # _img.append(img)
  
  out.release()
  return


if __name__ == "__main__":
  main()
  