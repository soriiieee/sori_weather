import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta
from pdf2image import convert_from_path, convert_from_bytes
import cv2


def pdf2img(fname):
  img = convert_from_path('../dat/high/FEAS50_202101140326.pdf')
  img[0].save('../dat/high/FEAS50_202101140326.png', "png")
  return
  

if __name__ == "__main__":
  fname = '../dat/high/FEAS50_202101140326.pdf'

  print(fname)
  sys.exit()
  pdf2img(fname)