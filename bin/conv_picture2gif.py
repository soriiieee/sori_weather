import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta
from pdf2image import convert_from_path, convert_from_bytes
import cv2
import glob
from tqdm import tqdm

from PIL import Image, ImageDraw
# ref: https://note.nkmk.me/python-pillow-gif/
# print(PIL.__file__)
# print(Image)
# sys.exit()


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

def main(cate):
  """
  #reference... https://yakumo-takaya.hatenablog.jp/entry/2019/10/14/000000
  """

  _f = read_files()  #fine name get
  _img = []
  out_path = f'/Users/soriiieee/Desktop/ts_{cate}.gif'

  width = 200
  # center = width // 2
  # color_1 = (0, 0, 0)
  # color_2 = (255, 255, 255)
  # max_radius = int(center * 1.5)
  step = 8

  for f in _f:
    try:
      f_path = f"/Users/soriiieee/work/sori_weather/dat/{cate}/{f}"
      im = Image.open(f_path)
      _img.append(im)
    except:
      pass

  _img[0].save(out_path,save_all=True, append_images=_img[1:], optimize=False, duration=500, loop=0)
  return


if __name__ == "__main__":
  cate="g3"
  main(cate)
  