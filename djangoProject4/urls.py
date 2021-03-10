"""djangoProject4 URL Configuration

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
from django.urls import path
from app4 import views
from django.views.generic import TemplateView,ListView,DetailView
from app4.models import Account
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('savings/',
         ListView.as_view(model=Account, template_name="saving.html", queryset=Account.objects.filter(type="savings")),
         name="savings"),
    path('show<int:pk>/', DetailView.as_view(model=Account, template_name="onesavings.html"))

]
