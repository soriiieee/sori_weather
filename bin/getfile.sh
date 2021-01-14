#!bin/bash

HOME=/Users/soriiieee/work/sori_weather
BIN=$HOME/bin
DAT=$HOME/dat
OUT=$HOME/OUT
ENV=$HOME/env
TBL=$HOME/tbl

#---------
# source activate sori_conda #activate
# INI_J=202101141500
# DELTA=18
# python mk_tl.py $INI_J $DELTA
#---------
# exit

#気圧配置図のdownload
# -----------------------------------
# DAT2=$DAT/g3
# [ ! -e $DAT2 ] && mkdir -p $DAT2 
# cd $DAT2
# rm -f ./*.png
# _URL=`cat $TBL/list_time.dat | awk '{print $1}'`
# for URL in ${_URL[@]};do
# wget $URL
# sleep 1
# done
# -----------------------------------

#予報図のdownload
# -----------------------------------
  # DAT2=$DAT/fct
  # [ ! -e $DAT2 ] && mkdir -p $DAT2 
  # cd $DAT2
  # rm -f ./*.png
  # #zenkoku
  # wget https://www.jma.go.jp/jp/yoho/images/000_telop_today.png
  # wget https://www.jma.go.jp/jp/yoho/images/000_telop_tomorrow.png
  # # wget https://www.jma.go.jp/jp/yoho/images/000_telop_aftomorrow.png
  # wget https://www.jma.go.jp/jp/yoho/images/000_temp_today.png
  # wget https://www.jma.go.jp/jp/yoho/images/000_temp_tomorrow.png
  # #kantou
  # wget https://www.jma.go.jp/jp/yoho/images/206_telop_today.png
  # wget https://www.jma.go.jp/jp/yoho/images/206_telop_tomorrow.png
  # # wget https://www.jma.go.jp/jp/yoho/images/206_telop_aftomorrow.png
  # wget https://www.jma.go.jp/jp/yoho/images/206_temp_today.png
  # wget https://www.jma.go.jp/jp/yoho/images/206_temp_tomorrow.png
# -----------------------------------

#アメダス等のdownload
# -----------------------------------
  DAT2=$DAT/ame
  [ ! -e $DAT2 ] && mkdir -p $DAT2 
  cd $DAT2
  rm -f ./*.png
  # sekisetushin
  INI_J=`date +%Y%m%d%H`
  wget https://www.jma.go.jp/jp/amedas/imgs/snow/000/${INI_J}00-00.png #snow
  wget https://www.jma.go.jp/jp/amedas/imgs/temp/000/${INI_J}00-00.png #temp

# -----------------------------------

# 上空寒気の状況 500hPa / 850hpa 
DAT2=$DAT/high
[ ! -e $DAT2 ] && mkdir -p $DAT2 
cd $DAT2
wget https://www.sunny-spot.net/chart/data/FEAS50/2021/01/FEAS50_202101140326.pdf #now
wget https://www.sunny-spot.net/chart/data/FEAS502/2021/01/FEAS502_202101140326.pdf #24h
wget https://www.sunny-spot.net/chart/data/FEAS504/2021/01/FEAS504_202101140326.pdf #48h

wget https://www.sunny-spot.net/chart/data/FXFE502/2021/01/FXFE502_202101141236.pdf
wget https://www.sunny-spot.net/chart/data/FXFE504/2021/01/FXFE504_202101141236.pdf
wget https://www.sunny-spot.net/chart/data/FXFE5782/2021/01/FXFE5782_202101141237.pdf #12/24


# 
