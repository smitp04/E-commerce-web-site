from django.shortcuts import render
from .models import Cart
from products.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

def cart(request, username):
    print()
    if str(request.user) == username:
        if request.method == 'POST':
            pid = request.POST.get('plus') or request.POST.get('minus')
            update = Cart.objects.get(username=username, productkey=pid)
            price = Product.objects.values_list('price',).get(pid=pid)
            price = float(price[0])
            
            if request.POST.get('plus') != None:
            
                update.quantity += 1
                update.total_price = update.quantity * price
            
            elif request.POST.get('minus') != None:
                if update.quantity != 0:
                    update.quantity -= 1
                    update.total_price = update.quantity*price
                
            update.total_price = '{:.2}'.format(update.total_price)
            update.save()
        
        carts = Cart.objects.filter(username=username).all()
        # print(carts)
        price = 0
        
        for cart in carts:
            print(cart.total_price)
            price += cart.total_price
        return render(request, 'cart.html', {'carts': carts, 'total_price': price})
    else:
        logout(request)
        return HttpResponseRedirect('/../')

def placeOrder(request, username):
    if str(request.user) == username:
        carts = Cart.objects.filter(username=username).all()
        return render(request, 'placeOrder.html', {'carts': carts})
    else:
        logout(request)
        return HttpResponseRedirect('/../')

def message(request, username):
    return render(request,'message.html',{})