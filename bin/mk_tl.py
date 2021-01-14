import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

print("start mk_tl.py..")

# now = datetime.now()
# now12 = now.strftime("%Y%m%d%H%M")
ini_j = sys.argv[1]
delta = int(sys.argv[2])
img_24h = (pd.to_datetime(ini_j) + timedelta(hours=delta)).strftime("%Y%m%d%H%M")
img_48h = (pd.to_datetime(ini_j) + timedelta(hours=delta+24)).strftime("%Y%m%d%H%M")


_url = []
img_48h = f"{img_48h[2:10]}"
img_24h = f"{img_24h[2:10]}"
# img_now = f"{ini_j[2:10]}"
_url.append(f"https://www.jma.go.jp/jp/g3/images/jp_c/48h/{img_48h}.png {img_48h}")
_url.append(f"https://www.jma.go.jp/jp/g3/images/jp_c/24h/{img_24h}.png {img_24h}")

for i in range(0, 10 + 1):
  t = (pd.to_datetime(ini_j) - timedelta(hours=3 * i)).strftime("%Y%m%d%H%M")
  _url.append(f"https://www.jma.go.jp/jp/g3/images/jp_c/{t[2:10]}.png {t[2:10]}")

with open("../tbl/list_time.dat", "w") as f:
  for url in _url:
    line = f"{url}\n"
    f.write(line)
# print(now)
# print(now12, hh)