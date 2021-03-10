from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Account

class ShowIndex(TemplateView):
     template_name = "index.html"

class ShowAllSavings(ListView):
     model = Account
     template_name = "saving.html"
     queryset = Account.objects.filter(type="savings")


class ShowOneSavings(DetailView):
     model = Account
     template_name = "onesavings.html"
