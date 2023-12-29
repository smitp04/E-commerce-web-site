"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from user import views as uv
from products import views as pv
from cart import views as cv


urlpatterns = [
    path('', uv.log_in_view),       
    path('admin/', admin.site.urls),
    path('view_products/<str:username>/', uv.showProduct,name='products'),
    path('view_products/<str:username>/cart/',cv.cart, name ='cart'),
    path('createNewUser', uv.createNewUser),    
    path('signUpPage', uv.signUpPage),
    path('view_products/<str:username>/place_order', cv.placeOrder),
    path('logout/',uv.user_logout, name='logout'),
    path('profile/', uv.user_profile, name='profile'),
    path('view_products/<str:username>/place_order/', cv.placeOrder), 
    path('view_products/<str:username>/place_order/message/', cv.message), 
    path('view_products/<str:username>/cart/',cv.cart, name ='cart'),
]
