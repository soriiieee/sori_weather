import os,sys,re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

import json
import warnings
warnings.simplefilter("ignore")
import time
import requests
# import beautifulsoup4
# from beautifulsoup4 import BeautifulSoup
try:
  from bs4 import BeautifulSoup
except:
  from beautifulsoup4 import BeautifulSoup

# print(requests.__file__)
# print(bs4.__file__)
# print(BeautifulSoup)
# sys.exit()
#---
# OLD PROGRM
# ----

print("start mk_tl2.py..")



#---
# NEW 2021.01.16
# ----

def main():
  URL = "https://www.jma.go.jp/jp/g3/"
  r = requests.get(URL)
  if r.status_code == 200:
    # print(f"Got OK {season}")
    with open(f"../dat/tmp/ree_weather.dat", "w") as f:
      f.write(r.text)
      data = r.text
  else:
    print("Not data...")
  # soup = BeautifulSoup(data, "html")
  return 

def read():
  with open(f"../dat/tmp/ree_weather.dat", "r") as f:
    data = f.read()
  soup = BeautifulSoup(data, "html")
  print(soup.find("label"))
  

if __name__ == "__main__":
  if 0:
    main()
  if 1:
    read()

