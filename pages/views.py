from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='signin')
def index(request):
    pro=Product.objects.all().filter(is_active=True).order_by("-id")[:8]
    context={
        "title":'home',
        "latesproduct":pro,
    }
    return render(request, 'pages/index.html',context)

@login_required(login_url='signin')
def about(request):
    context={
         "title":'about',
    }
    return render(request, 'pages/about.html',context)


@login_required(login_url='signin')
def coffee(request):
    context={
         "title":'coffee',
    }
    return render(request, 'pages/coffee.html',context)