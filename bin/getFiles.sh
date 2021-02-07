#!bin/bash

HOME=/home/ysorimachi/work/sori_py2/sori_weather
BIN=$HOME/bin
PY=$HOME/py
DAT=$HOME/dat

#environment
source activate sori_conda

FLG1=0
FLG2=1
FLG3=1

#tenkizu
[ $FLG1 -eq 1] && {
  [ ! -e $DAT/info ] && mkdir -p $DAT/info
  cd $DAT/info
  rm -f *.png
  URL=https://www.jma.go.jp/jp
  wget ${URL}/yoho/images/000_telop_today.png
  wget ${URL}/yoho/images/000_telop_tomorrow.png
  wget ${URL}/yoho/images/000_telop_aftomorrow.png
  wget ${URL}/yoho/images/000_temp_today.png
  wget ${URL}/yoho/images/000_temp_tomorrow.png
}

[ $FLG2 -eq 1] && {



  [ ! -e $DAT/img ] && mkdir -p $DAT/img
  # cd $DAT/info
  # rm -f *.png
  # URL=https://www.jma.go.jp/jp
  # wget ${URL}/yoho/images/000_telop_today.png
  # wget ${URL}/yoho/images/000_telop_tomorrow.png
  # wget ${URL}/yoho/images/000_telop_aftomorrow.png
  # wget ${URL}/yoho/images/000_temp_today.png
  # wget ${URL}/yoho/images/000_temp_tomorrow.png
}


