from django.views.generic import TemplateView
from .forms import SubscriberForm
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = "home.html"


class SignView(TemplateView):
    template_name = "sign.html"

class RegView(TemplateView):
    template_name = "reg.html"

class BaseView(TemplateView):
    template_name = "base.html"

def landing(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()
    return render(request, 'reg.html', locals())