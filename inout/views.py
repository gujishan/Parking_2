import tempfile
import time
from datetime import datetime
from random import choice

from alipay import AliPay
from django.http import HttpResponse

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Car_w.models import Car_w

from Parking_2.settings import ALIPAY_APPID, APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY, MEDIA_ROOT, PRICE
from inout.chepai import scan
from inout.models import Car, Parking
from inout.tupian import scan_tu


def carin(request):
    c_no=scan()
    print(c_no)
    cws_no=[]
    cws=Car_w.objects.filter(Car_w_status=True)
    for cw in cws:
        cws_no.append(cw.Car_w_no)
    cw_no=choice(cws_no)
    print(cw_no)
    if not cw_no and c_no:
        info='扫描错误！'
        cws = Car_w.objects.filter(Car_w_status=True)
        return render(request,'index.html',context=locals())
    else:
        p_cars=Parking.objects.filter(Cat_status=True)
        for p_car in p_cars:
            if c_no==p_car.P_Car_no.Car_no:
                info='已经有这辆车'
                cws = Car_w.objects.filter(Car_w_status=True)
                return render(request,'index.html',context=locals())
        else:
            cars = Car.objects.all()
            for car in cars:
                if (c_no==car.Car_no):
                    car.Car_no=c_no
                    car.save()
                    break
            else:
                Car.objects.create(Car_no=c_no)

            car_no=Car.objects.get(Car_no=c_no)
            carw_no=Car_w.objects.get(Car_w_no=cw_no)
            Parking.objects.create(P_Car_no=car_no,P_Car_w_no=carw_no)
            carw_no.Car_w_status=False
            carw_no.save()
            info="车辆"+c_no+"进入停车场"
            cws = Car_w.objects.filter(Car_w_status=True)
            return render(request,'index.html',context=locals())
# 扫描图片进入停车场
def carin_tu(request):
    if request.method=="GET":
        return render(request,'carin_tu.html')
    elif request.method=="POST":
        chepai=request.FILES['chepai']
        save_path=MEDIA_ROOT+chepai.name
        print(save_path)
        with open(save_path,'wb')as f:
            for content in chepai.chunks():
                f.write(content)
        img=save_path
        c_no = scan_tu(image=img)
        print(c_no)
        cws_no = []
        cws = Car_w.objects.filter(Car_w_status=True)
        for cw in cws:
            cws_no.append(cw.Car_w_no)
        cw_no = choice(cws_no)
        print(cw_no)
        if not cw_no and c_no:
            info = '扫描错误！'
            cws = Car_w.objects.filter(Car_w_status=True)
            price = PRICE[len(PRICE) - 1]
            return render(request, 'index.html', context=locals())
        else:
            p_cars = Parking.objects.filter(Cat_status=True)
            for p_car in p_cars:
                if c_no == p_car.P_Car_no.Car_no:
                    info = '已经有这辆车'
                    cws = Car_w.objects.filter(Car_w_status=True)
                    price=PRICE[len(PRICE)-1]
                    return render(request, 'index.html', context=locals())
            else:
                cars = Car.objects.all()
                for car in cars:
                    if (c_no == car.Car_no):
                        car.Car_no = c_no
                        car.save()
                        break
                else:
                    Car.objects.create(Car_no=c_no)

                car_no = Car.objects.get(Car_no=c_no)
                carw_no = Car_w.objects.get(Car_w_no=cw_no)
                Parking.objects.create(P_Car_no=car_no, P_Car_w_no=carw_no)
                carw_no.Car_w_status = False
                carw_no.save()
                info = "车辆" + c_no + "进入停车场"
                cws = Car_w.objects.filter(Car_w_status=True)
                price = PRICE[len(PRICE) - 1]
                return render(request, 'index.html', context=locals())

def carout(request):
    c_no = scan()
    print(c_no)
    # car_rm = Parking.objects.filter(Cat_status=True).get(P_Car_no__Car_no=c_no)
    cars=Parking.objects.filter(Cat_status=True)
    for car in cars:
        if not c_no==car.Car_no:
            info='没有这辆车'
        return render(request,'index.html',context=locals())
    else:
        car_rm=cars.get(P_Car_no__Car_no=c_no)
        car_w = Car_w.objects.get(Car_w_no=car_rm.P_Car_w_no.Car_w_no)
        car_w.Car_w_status = True
        car_w.save()
        intime = car_rm.In_time
        outtime = datetime.now()
        car_rm.Out_time = outtime
        intime_str = intime.strftime("%Y-%m-%d %H:%M:%S")
        outtime_str = outtime.strftime("%Y-%m-%d %H:%M:%S")
        intime_f = intime.timestamp()
        outtime_f = outtime.timestamp()
        alltime = outtime_f - intime_f
        alltime = int(alltime / 60 + 1)
        time_hour = int(alltime / 60)
        time_min = alltime - time_hour * 60
        pri_time = int(alltime / 60 + 1)
        price=PRICE[len(PRICE)-1]
        Money = pri_time * price
        car_rm.P_Money = price
        car_rm.P_Money = Money
        car_rm.All_time = alltime
        car_rm.Cat_status = False
        car_rm.save()
        print(intime, outtime)
        hourtime = alltime / 60 + 1
        return render(request, 'pay.html', context=locals())

def carout_tu(request):
    if request.method=="GET":
        return render(request,'carout_tu.html')
    elif request.method=="POST":
        chepai=request.FILES['chepai']
        save_path=MEDIA_ROOT+chepai.name
        print(save_path)
        with open(save_path,'wb')as f:
            for content in chepai.chunks():
                f.write(content)
        img=save_path
        c_no = scan_tu(image=img)
        print(c_no)
        try:
            car_rm = Parking.objects.filter(Cat_status=True).get(P_Car_no__Car_no=c_no)
        except:
            info = "没有这辆车！"
            cws = Car_w.objects.filter(Car_w_status=True)
            return render(request, 'index.html', context=locals())
        if car_rm:
            car_w = Car_w.objects.get(Car_w_no=car_rm.P_Car_w_no.Car_w_no)
            car_w.Car_w_status = True
            car_w.save()
            intime = car_rm.In_time
            outtime = datetime.now()
            car_rm.Out_time = outtime
            intime_str = intime.strftime("%Y-%m-%d %H:%M:%S")
            outtime_str = outtime.strftime("%Y-%m-%d %H:%M:%S")
            intime_f = intime.timestamp()
            outtime_f = outtime.timestamp()
            alltime = outtime_f - intime_f
            alltime = int(alltime / 60 + 1)
            time_hour = int(alltime / 60)
            time_min = alltime - time_hour * 60
            pri_time = int(alltime / 60 + 1)
            price=PRICE[len(PRICE)-1]
            Money = pri_time * price
            car_rm.P_Money = Money
            car_rm.All_time = alltime
            car_rm.Cat_status = False
            car_rm.P_price=price
            car_rm.save()
            print(intime, outtime)
            hourtime = alltime / 60 + 1
            return render(request, 'pay.html', context=locals())



def pay(request):
    money = request.GET.get('money')
    # 构建支付的客户端 AlipayClient
    alipay_client = AliPay(
        appid=ALIPAY_APPID,
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False  # 默认False
    )
    # 使用Alipay进行支付请求的发起
    subject = '停车费13'
    # 客户端操作
    no = str(int(time.time()))
    order_string = alipay_client.api_alipay_trade_page_pay(
        out_trade_no=no,
        total_amount=money,
        subject=subject,
        return_url="http://127.0.0.1:8000/index",
        notify_url=""  # 可选, 不填则使用默认notify url
    )
    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)


