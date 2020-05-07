from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.safestring import mark_safe

from Parking_2.settings import PRICE
from inout.models import Parking
from root.models import Login
from root.tool import all_list, zl_data, get_year, get_month, get_day
from utils.ustil import my_login


@my_login
def root(request):
    username=request.session.get('login_user_name')
    return render(request , 'root.html' ,context=locals())


def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            username=username.strip()
            try:
                user=Login.objects.get(username=username)
            except:
                info='请输入正确的用户名'
                return render(request,'login.html',context=locals())
            if user.password==password:
                request.session['login_user_name']=username
                request.session.set_expiry(0)
                return render(request,'root.html',context=locals())
            else:
                info='请输入正确的密码'
                return render(request,'login.html',context=locals())

@my_login
def registered(request):
    if request.method=="GET":
        return render(request,'registered.html')
    elif request.method=="POST":
        username=request.POST.get("username")
        mobile=request.POST.get("mobile")
        password=request.POST.get("password")
        password2=request.POST.get("password2")

        logins=Login.objects.all()
        for login in logins:
            if login.username==username:
                info="已经有这个管理员"
                return render(request,"registered.html",context=locals())
        if len(mobile)!=11:
            info='请输入11位的手机号'
            return render(request,'registered.html',context=locals())
        if password!=password2:
            info='两次输入密码不同'
            return render(request,'registered.html',context=locals())
        else:
            Login.objects.create(username=username,password=password,mobile=mobile)
            info='管理员创建成功！'
            return render(request,'registered.html',context=locals())

@my_login
def getro(request):
    logins=Login.objects.all()
    return render(request, 'getro.html', context=locals())

@my_login
def rmro(request,no):
    login = Login.objects.get(pk=no)
    login.delete()
    logins = Login.objects.all()
    return render(request, 'getro.html', context=locals())

@my_login
def updatero(request,no):
    login = Login.objects.get(pk=no)
    if request.method=="GET":
        return render(request,'updatero.html',context=locals())
    elif request.method=="POST":
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if len(mobile)!=11:
            info = "请输入11位手机号"
            return render(request,'updatero.html',context=locals())
        elif password != password2:
            info='两次输入密码不同'
            return render(request,'updatero.html',context=locals())
        else:
            login=Login.objects.get(pk=no)
            login.password=password
            login.mobile=mobile
            login.save()
            info='修改成功'
            logins=Login.objects.all()
            return render(request,'getro.html',context=locals())

@my_login
def findro(request):
    if request.method=="GET":
        return render(request,"findro.html")
    elif request.method=="POST":
        username=request.POST.get('username')
        try:
            login=Login.objects.get(username=username)
            return render(request,'findro.html',context=locals())
        except:
            return render(request,'findro.html')

# 查看在停车场内的车辆信息
def incar(request):
    parkings=Parking.objects.filter(Cat_status=True)
    nowtime=datetime.now().timestamp()
    if not  parkings:
        info="停车场内没有车！"
        username=request.session.get('login_user_name')
        return render(request,'root.html',context=locals())
    else:

        for parking in parkings:
            all_time=nowtime-parking.In_time.timestamp()
            all_time=all_time/60+1
            parking.All_time=int(all_time)
        return render(request,'incar.html',context=locals())


def allcar(request):
    parkings=Parking.objects.all()
    return render(request,'allcar.html',context=locals())


def findc(request):
    if request.method=="GET":
        return render(request,'findc.html')
    elif request.method=="POST":
        car_no=request.POST.get('car_no')
        cars=Parking.objects.filter(P_Car_no__Car_no__contains=car_no)
        return render(request,'findc.html',context=locals())


def price(request):
    if request.method=="GET":
        price=PRICE[len(PRICE)-1]
        print(len(PRICE))
        return render(request,'price.html',context=locals())
    elif request.method=="POST":
        price=request.POST.get('price')
        PRICE.append(float(price))
        info='单价'+price+'元/小时设置成功！'
        username = request.session.get('login_user_name')
        return render(request,'root.html',context=locals())


def income(request):
    incomes=Parking.objects.filter(Cat_status=False)
    return render(request,'income.html',context=locals())


def tu_car(request):
    datas=[]
    x_data=[]
    y_data=[]
    parkings=Parking.objects.all()
    for parking in parkings:
        data=parking.In_time
        data=str(data).split(" ",1)[0]
        datas.append(data)
    all=all_list(datas)
    for i in sorted(all.keys()):
        x_data.append(i)
        y_data.append(all[i])
    x_data=mark_safe(x_data)
    print(x_data)
    print(y_data)
    return render(request,'tu_car.html',context=locals())

def tu_money(request):
    datas = []
    moneyss = []
    parks = Parking.objects.filter(Cat_status=False)
    for park in parks:
        data = park.Out_time
        data = str(data).split(" ", 1)[0]
        datas.append(data)
    zl = zl_data(datas)
    zl.sort()
    print(zl)
    for i in zl:
        mons = 0
        print(i)
        moneys = parks.filter(Out_time__year=get_year(i), Out_time__month=get_month(i), Out_time__day=get_day(i))
        for money in moneys:
            mon = money.P_Money
            mons = mons + mon
        print(mons)
        moneyss.append(mons)
    print(zl)
    print(moneyss)
    x_data = mark_safe(zl)
    y_data = mark_safe(moneyss)
    print(x_data)
    print(y_data)

    return render(request, 'tu_money.html', context=locals())


def findmoney(request):
    if request.method=="GET":
        return render(request,'findmoney.html')
    elif request.method=="POST":
        data=request.POST.get('data')
        moneys = Parking.objects.filter(Cat_status=False).filter(Out_time__year=get_year(data), Out_time__month=get_month(data), Out_time__day=get_day(data))
        mons=0
        for money in moneys:
            mon = money.P_Money
            mons = mons + mon
    return render(request,'findmoney.html',context=locals())