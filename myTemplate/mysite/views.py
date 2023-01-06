from django.shortcuts import render
from datetime import datetime
# Create your views here.
# https://www.youtube.com/embed/測試碼
def index (request,tvno = 0):
    tv_list = [{'name':'Gundam Info', 'tvcode':'bBjzNiGSC3A'},
    {'name':'ELDEN RING', 'tvcode':'Pv7_1UyCuLU'},
    {'name':'One Ok Rock', 'tvcode':'fnyzHd2PoS0'},
    {'name':'God of War Ragnarök', 'tvcode':'V4OAT3HxOlo'},
    {'name':'Bloodborne', 'tvcode':'m1w3d0YgjZ8'},
    {'name':'鐵血孤兒', 'tvcode':'6GORJ5bOcAE'},
    {'name':'冰雪奇緣2', 'tvcode':'d_zVfl4bpJI'},]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())
    #（如果要傳遞的變數比較多，能將字典形式改成使用Python的locals()函數）

def engtv(request, tvno='0'):
    tv_list = [{'name':'SkyNews', 'tvcode':'99U4CH_k5F0'},
    {'name':'Euro News', 'tvcode':'F-uW_IswLh8'},
    {'name':'India News', 'tvcode':'E7dbhET6_EA'},
    {'name':'CCTV', 'tvcode':'vCDDYb_M2B4'},]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    return render(request, 'engtv.html', locals())