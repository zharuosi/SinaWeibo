#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
import json
import urllib2
from PIL import Image,ImageDraw,ImageFont

def weather():
    # 获取每日天气数据
    try:
        url = 'http://api.map.baidu.com/telematics/v3/weather?location=上海&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback='
        s=json.loads(urllib2.urlopen(url).read())
        s1 = s["results"][0]["weather_data"][0]["temperature"]
        s2 = s["results"][0]["weather_data"][0]["weather"]
        s3 = s["results"][0]["currentCity"]

        print s["results"][0]["weather_data"][0]["temperature"]
        print s["results"][0]["weather_data"][0]["weather"]
        print s["results"][0]["currentCity"]
        return s1,s2,s3
    except :
        print"error"
def draw_pic(l):
    img = Image.open('../image/background.jpg')
    draw = ImageDraw.Draw(img)
    # myfont = ImageFont.truetype('LiberationSans-Regular.ttf', size=140) 
    myfont = ImageFont.truetype(u'/home/rzha/app/msyh.ttf', size=70) 
    draw.text((img.size[0]/9,img.size[1]/9),unicode(l[2]),font=myfont, fill = 'cyan')
    draw.text((img.size[0]/3,img.size[1]/3),unicode(l[0]),font=myfont, fill = 'blue')
    draw.text((img.size[0]*2/3,img.size[1]*2/3),unicode(l[1]),font=myfont, fill = 'cyan')
    img.save('../image/todayWeather.jpg','jpeg')
    print 'ok'

#Test:
#draw_pic(weather())
