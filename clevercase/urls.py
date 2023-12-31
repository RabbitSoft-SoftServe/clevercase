"""
URL configuration for clevercase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from registration.views import signup_page, LoginPage,  LogoutPage, landing_page, debts_menu
from wallet.views import home_page, analytics_page
from reg_pay.views import regpay_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_page, name='signup'),
    path('login/', LoginPage, name='login'),
    path('home/', home_page, name='home'),
    path('logout/', LogoutPage, name='logout'),
    path('', landing_page, name="landing"),
    path('regularpays/', regpay_page, name='regularpays'),
    path('debts/', debts_menu, name="debts"),
    path('analytics/', analytics_page, name="analytics"),
]
#category_create_view