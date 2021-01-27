#!bin/bash

HOME=/Users/soriiieee/work/sori_weather
BIN=$HOME/bin
DAT=$HOME/dat
OUT=$HOME/OUT
ENV=$HOME/env
TBL=$HOME/tbl



#------------------------------------------------------------------------------------------
# time list making...
#------------------------------------------------------------------------------------------
# [確認] https://www.jma.go.jp/jp/g3/

# source activate sori_conda #activate
INI_J=202101271200
INI_F=202101272100
# DELTA=15
python mk_tl.py $INI_J $INI_F
# exit
# ---------
# exit

# python ./conv_pdf2img.py 
# exit

#------------------------------------------------------------------------------------------
# data downloading...
#------------------------------------------------------------------------------------------
FLG_KIATSU=0
FLG_TENKI=0
FLG_AMEDAS=0
FLG_HIGH=1

#気圧配置図のdownload
# -----------------------------------
[ $FLG_KIATSU=1 ] && {
  DAT2=$DAT/g3
  [ ! -e $DAT2 ] && mkdir -p $DAT2 
  cd $DAT2
  rm -f ./*.png
  _URL=`cat $TBL/list_time.dat | awk '{print $1}'`
  for URL in ${_URL[@]};do
  [ ! -e ${DAT2}/`basename $URL` ] && {
    echo "None"
    wget $URL
  } || {
    echo "Already" `basename $URL`
  }
  done

  DAT2=$DAT/g3_asia
  [ ! -e $DAT2 ] && mkdir -p $DAT2 
  cd $DAT2
  rm -f ./*.png
  _URL=`cat $TBL/list_time.dat | awk '{print $3}'`
  for URL in ${_URL[@]};do
  [ ! -e ${DAT2}/`basename $URL` ] && {
    echo "None"
    wget $URL
  } || {
    echo "Already" `basename $URL`
  }
  done
}
# -----------------------------------

#予報図のdownload
# -----------------------------------
  
[ $FLG_TENKI -eq 1 ] && {
  DAT2=$DAT/fct
  [ ! -e $DAT2 ] && mkdir -p $DAT2 
  cd $DAT2
  rm -f ./*.png
  #zenkoku
  wget https://www.jma.go.jp/jp/yoho/images/000_telop_today.png
  wget https://www.jma.go.jp/jp/yoho/images/000_telop_tomorrow.png
  # wget https://www.jma.go.jp/jp/yoho/images/000_telop_aftomorrow.png
  wget https://www.jma.go.jp/jp/yoho/images/000_temp_today.png
  wget https://www.jma.go.jp/jp/yoho/images/000_temp_tomorrow.png
  #kantou
  wget https://www.jma.go.jp/jp/yoho/images/206_telop_today.png
  wget https://www.jma.go.jp/jp/yoho/images/206_telop_tomorrow.png
  # wget https://www.jma.go.jp/jp/yoho/images/206_telop_aftomorrow.png
  wget https://www.jma.go.jp/jp/yoho/images/206_temp_today.png
  wget https://www.jma.go.jp/jp/yoho/images/206_temp_tomorrow.png 
}
# -----------------------------------

#アメダス等のdownload
# -----------------------------------
[ $FLG_AMEDAS -eq 1 ] && {
  DAT2=$DAT/ame
  [ ! -e $DAT2 ] && mkdir -p $DAT2 
  cd $DAT2
  rm -f ./*.png
  # sekisetushin
  INI_J=`date +%Y%m%d%H`
  wget https://www.jma.go.jp/jp/amedas/imgs/snow/000/${INI_J}00-00.png #snow
  wget https://www.jma.go.jp/jp/amedas/imgs/temp/000/${INI_J}00-00.png #temp
}
# -----------------------------------


[ $FLG_HIGH -eq 1 ] && {
# 上空寒気の状況 500hPa / 850hpa 
  DAT2=$DAT/high
  [ ! -e $DAT2 ] && mkdir -p $DAT2

  cd $DAT2

  rm -f ./*.pdf
  # 極東地上気圧・風・降水量／500hPa高度・渦度予想図（ 12時間毎 ）
  wget https://www.jma.go.jp/jp/metcht/pdf/kosou/fxfe502_00.pdf
  wget https://www.jma.go.jp/jp/metcht/pdf/kosou/aupq35_00.pdf
  #極東850hPa気温・風、700hPa上昇流／700hPa湿数、500hPa気温予想図
  wget https://www.jma.go.jp/jp/metcht/pdf/kosou/fxfe5782_12.pdf 
  wget https://www.jma.go.jp/jp/metcht/pdf/kosou/axfe578_00.pdf
  # 日本850hPa相当温位・風12・24・36・48時間予想図（FXJP854）
  wget https://www.jma.go.jp/jp/metcht/pdf/kosou/fxjp854_00.pdf
  # rm -f ./*.pdf
  # wget https://www.sunny-spot.net/chart/data/FEAS50/2021/01/FEAS50_202101140326.pdf #now
  # wget https://www.sunny-spot.net/chart/data/FEAS502/2021/01/FEAS502_202101140326.pdf #24h
  # wget https://www.sunny-spot.net/chart/data/FEAS504/2021/01/FEAS504_202101140326.pdf #48h

  # wget https://www.sunny-spot.net/chart/data/FXFE502/2021/01/FXFE502_202101141236.pdf
  # wget https://www.sunny-spot.net/chart/data/FXFE504/2021/01/FXFE504_202101141236.pdf
  # wget https://www.sunny-spot.net/chart/data/FXFE5782/2021/01/FXFE5782_202101141237.pdf #12/24

}

# 
