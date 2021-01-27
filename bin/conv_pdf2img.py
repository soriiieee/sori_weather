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

def cut_image(fname2):
  if not os.path.exists('../dat/high/{}.png'.format(fname2)):
    pdf2img(fname2)
  
  img_master = cv2.imread('../dat/high/{}.png'.format(fname2), cv2.IMREAD_GRAYSCALE)
  img_japan = cv2.imread('../dat/japan_red.png')
  h,w = img_japan.shape[:2]
  
  if "FEAS" in fname2:
    img = img_master[100:1000, 80:img_master.shape[1] - 80] 
    print(img.shape)
    img[100:100+h, 200:200+w] = img_japan
    cv2.imwrite('../dat/high/out/{}.png'.format(fname2), img)
  return 
  
def japan_png():
  """
  http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
  """
  # img = cv2.imread('../dat/japan.png',cv2.IMREAD_GRAYSCALE)
  img = cv2.imread('../dat/japan.png')

  img = img[0:792, 0:592]
  #回転角を指定
  angle = 45.0
  scale = 1.0
  h,w = img.shape[:2]
  center = (int(w/2), int(h/2))
  trans = cv2.getRotationMatrix2D(center, angle, scale)
  img = cv2.warpAffine(img, trans, (w, h))
  before_color = [0, 0, 0]
  chenge_color = [255, 255, 255]
  img[np.where((img == before_color).all(axis=2))] = chenge_color
  
  ret,img = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
  img = cv2.bitwise_not(img) #hanten1

  #moruforogy
  kernel = np.ones((10, 10), np.uint8)
  img = cv2.dilate(img, kernel, iterations=1)
  img = cv2.bitwise_not(img)  #hanten2
  
  #black to red color
  before_color = [0, 0, 0]
  chenge_color = [0, 0, 255]
  img[np.where((img == before_color).all(axis=2))] = chenge_color

  img = cv2.resize(img, (220, 150))
  cv2.imwrite('../dat/japan_red.png', img)
  # https://watlab-blog.com/2020/03/08/rgba-png/

  return
  

def pdf2png_simple():
  DIR="/Users/soriiieee/work/sori_weather/dat/high"
  _fpath = glob.glob(f"{DIR}/*.pdf")
  for fpath in tqdm(_fpath):
    fname = os.path.basename(fpath).split(".")[0]
    outpath = f"{DIR}/png/{fname}.png"
    # outpath = 
    pdf2img(fpath, outpath)
  return



if __name__ == "__main__":
  pdf2png_simple()
  sys.exit()
  fname = '../dat/high/FEAS50_202101140326.pdf'
  fname2 = os.path.basename(fname).split(".")[0]
  #making
  # cut_image(fname2)
  japan_png()