from django.shortcuts import render

# Create your views here.
from Car_w.models import Car_w
from Parking_2.settings import PRICE
from utils.ustil import my_login


@my_login
# 添加停车位
def addcw(request):
    if request.method=="GET":
        return render(request,'addcw.html')
    elif request.method=="POST":
        cw_no=request.POST.get('cw_no')
        cw_length=request.POST.get('cw_length')
        cw_wz=request.POST.get('cw_wz')
        print(cw_no,cw_length,cw_wz)
        try:
            cws = Car_w.objects.all()
            for cw in cws:
                if cw_no == str(cw.Car_w_no):
                    info = '已经有这个车位'
                    return render(request, 'addcw.html', context=locals())
            else:
                Car_w.objects.create(Car_w_no=cw_no,Car_w_length=cw_length,Car_w_wz=cw_wz)
                info = '添加成功'
            return render(request, 'addcw.html', context=locals())
        except:
            Car_w.objects.create(Car_w_no=cw_no,Car_w_length=cw_length,Car_w_wz=cw_wz)
            info = '添加成功'
            return render(request, 'addcw.html', context=locals())

@my_login
# 查看停车位
def showcw(request):
    cws=Car_w.objects.all()
    return render(request,'showcw.html',context=locals())

@my_login
# 删除停车位
def rmcw(request,no):
    cw=Car_w.objects.get(Car_w_no=no)
    cw.delete()
    cws=Car_w.objects.all()
    return render(request,'showcw.html',context=locals())

@my_login
# 更改车辆信息
def updatecw(request,no):
    if request.method=="GET":
        return render(request,'updatecw.html',context=locals())
    elif request.method=="POST":
        cw_length=request.POST.get('cw_length')
        cw_wz=request.POST.get('cw_wz')

        car_w_re = Car_w.objects.get(Car_w_no=no)
        car_w_re.Car_w_length = cw_length
        car_w_re.Car_w_wz = cw_wz
        car_w_re.save()
        info = '第' + no + '车位修改成功'
    return render(request,'showcw.html',context=locals())

@my_login
# 查找某一车位
def findcw(request):
    if request.method=="GET":
        return render(request,"findcw.html")
    elif request.method=="POST":
        cw_no=request.POST.get('cw_no')
        try:
            cw=Car_w.objects.get(Car_w_no=cw_no)
            return render(request,'findcw.html',context=locals())
        except:
            info="没有这个车位"
            return render(request, 'findcw.html')

def index(request):
    cws=Car_w.objects.filter(Car_w_status=True)
    price=PRICE
    return render(request,'index.html',context=locals())