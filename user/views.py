from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from user.models import User as User1
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from products.models import Product
from django.urls import path
from cart.models import Cart
from user.models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

currnetuser =''
def log_in_view(request, *args, **kwargs):
    
    u = request.POST or None
    con = {}
    uservalid = {}

    if u is None:
        return render(request, 'login.html')

    else:
        try:
            uname = request.POST.get('name', 'default')
            upassword = request.POST.get('password', 'defalut')

            user = authenticate(request, username=uname, password=upassword)
            if user is None:
                raise User.DoesNotExist
            else:
                login(request, user)
                urlgreet = './view_products/'+uname
            return HttpResponseRedirect(urlgreet)

        except User.DoesNotExist:
            con = {'condition': 'User Not Found'}
            return render(request, 'login.html', con)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('..')


@login_required
def showProduct(request, username):
    
    global currnetuser
    currnetuser=request.user
    name = str(request.user)
    if name == username:
        if request.method == 'POST' and request.POST.get('sub') != None:
            pid = request.POST.get('sub', 0)
            pid = int(pid)

            pname, pprice, img_url = Product.objects.values_list(
                'name', 'price', 'image_url').get(pid=pid)

            try:
                qty = Cart.objects.get(username=username, productkey=pid)
                qty.quantity += 1
                qty.total_price += pprice
                qty.total_price = '{:.2}'.format(qty.total_price)
                qty.save()

            except:
                reg = Cart(username=username, quantity=1, total_price=pprice,
                           productkey=pid, productname=pname, image_url=img_url)
                reg.save()
                pass

        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})
    else:
        logout(request)
        return HttpResponseRedirect('/../')


def signUpPage(request, *args, **kwargs):
    con = {}

    try:
        con = {'condition': args[0]}
        return render(request, 'signup.html', con)
    except:
        return render(request, 'signup.html')


def createNewUser(request, *args, **kwargs):
    # print(args)
    while True:
        uname = request.POST.get('name', 'default')
        uemail = request.POST.get('email', 'default')
        upassword = request.POST.get('password', 'default')
        mobile = request.POST.get('mobile', 'None')
       

        if len(uname) == 0 or len(uemail) == 0 or len(upassword) == 0:
            return signUpPage(request, 'Please Fill All The Fields!')

        try:
            u = User.objects.get(username=uname)

            if u is not None:
                return signUpPage(request, 'User Already Exist')

        except Exception as e:
            break

    user = User.objects.create_user(uname, uemail, upassword)
    user.first_name = request.POST.get('firstname', 'default')
    user.last_name = request.POST.get('lastname', 'default')
    user.save()

    customer = Customer(user_info=user, mobile=mobile)
    customer.save()
    return render(request, 'success.html')


def user_profile(request,*args,**kwargs):
    # user = User.objects.filter(username=currnetuser).all()
    user = User.objects.get(username=currnetuser)
    # customer = Customer.objects.filter(user_info=currnetuser).all()
    customer = Customer.objects.get(user_info=currnetuser)
    return render(request, 'profile.html',{'users':user,'customers':customer})
