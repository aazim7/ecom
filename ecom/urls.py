"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from products import views as webviews
from accounts import views as uservievs
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-login', uservievs.login_page),
    path('user-registration', uservievs.register),
    path('verification', uservievs.otp_verification),
    path('reotp', uservievs.re_otp),
    path('logout', uservievs.logout_view),
    #Product
    path('', webviews.homepage, name="home"),#use of name="xys" to get inside template {% url 'xys' %}
    path('products/<str:slug>', webviews.product_details, name="detail"),#matching secquence
    path('products/', webviews.product_list, name="shop"),#if not match above then here
    path('add-to-cart/', webviews.addcart)
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()