#coding=utf-8

from django.shortcuts import render,redirect
from . models import UserInfo
from df_goods.models import GoodsInfo
from df_order.models import *
from hashlib import sha1
from django.http import *
from . import user_decorator
from django.core.paginator import Paginator

def register(request):
    context = {'title': '用户注册'}
    return render(request,'df_user/register.html',context)

def register_handle(request):
    #接收用户输入
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码
    if upwd!=upwd2:
        return redirect('/user/register')
    # 密码加密
    s1=sha1()
    s1.update(upwd.encode("utf-8"))
    upwd3 = s1.hexdigest()
    #创建对象
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail
    user.save()
    #注册成功，转到登录页面
    return redirect('/user/login/')

def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})


def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

def login_handle(request):
    # 接收请求信息
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    # jizhu=post.get('jizhu',0)
    # 根据用户名查询对象
    users=UserInfo.objects.filter(uname=uname)
    # print(uname)
    # 判断：如果未查到用户名错。如果查到判断密码是否正确，正确转到用户中心
    if len(users)==1:
        s1 = sha1()
        s1.update(upwd.encode("utf-8"))
        if s1.hexdigest()==users[0].upwd:
            url=request.COOKIES.get('url','/')
            red = HttpResponseRedirect(url)
            # if jizhu != 0:
            #     red.set_cookie('uname',uname)
            # else:
            #     red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request,'df_user/login.html',context)

def ceshi(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    context={'user_email':user_email}
    return render(request, 'df_user/ceshi.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def user_center_info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
    # 最近浏览
    goods_list = []
    try:
        goods_ids=request.COOKIES.get('goods_ids','')
        goods_ids1=goods_ids.split(',')
        # GoodsInfo.objects.filter(id_in=goods_ids1)

        for goods_id in goods_ids1:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    except:
        goods_list = []
    context={
        'title':'用户中心',
        'user_email':user_email,
        'user_name':request.session['user_name'],
        'sub_page_name':1,
        'goods_list':goods_list
    }
    return render(request,'df_user/user_center_info.html',context)

@user_decorator.login
def user_center_order(request,pindex):
    # 获取用户订单信息
    uid = request.session['user_id']
    user = UserInfo.objects.get(id=request.session['user_id'])
    orders = OrderInfo.objects.filter(user=user).order_by('-odate')
    # 获取订单商品信息
    for order in orders:
        # 根据order_id查询订单信息
        order_goods = OrderDetailInfo.objects.filter(order_id=order.oid)
        # 根据order_goods计算商品小计
        for goods in order_goods:
            amount = goods.count * goods.price
            # 动态给order_goods增加amount，保存订单商品的小计
            goods.amount = amount
        # 动态给order增加属性，保存订单商品的信息
        order.order_goods = order_goods
    # 分页
    paginator = Paginator(orders, 1)
    page=paginator.page(int(pindex))
    context = {'title': '用户中心',
               'sub_page_name':1,
               'page': page,
               'paginator': paginator,
               'orders':orders,}
    return render(request,'df_user/user_center_order.html',context)

@user_decorator.login
def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context={'title':'用户中心','user':user,'sub_page_name':1,}
    return render(request,'df_user/user_center_site.html',context)












