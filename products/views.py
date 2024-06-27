from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.

# products
@login_required(login_url='signin')
def products(request):
    pro=Product.objects.all().filter(is_active=True).order_by("id")
    if request.method =="GET":
        
        cs=request.GET.get("cs")
        
        
            
        if "searchName" in request.GET:
            name=request.GET.get("searchName")
            if name:
                if cs=="on":
                    pro=pro.filter(name__contains=name)
                    
                else:
                    pro=pro.filter(name__icontains=name)
                    
        if "searchDesc" in request.GET:
            description=request.GET.get("searchDesc")
            
            if description:
                if cs =="on":
                    pro=pro.filter(description__contains=description)
                else:
                    pro=pro.filter(description__icontains=description)
                
        if "priceFrom" in request.GET and "priceTo" in request.GET:
            priceFrom=request.GET.get("priceFrom")
            priceTo=request.GET.get("priceTo")
            if priceFrom and priceTo :
                if priceFrom.isdigit() and priceTo.isdigit():
                    pro=pro.filter(price__gte=priceFrom, price__lte=priceTo)
            

        
    context={
        'title':"products",
        "product":pro,

    }
    return render(request, 'products/products.html',context)



# product

@login_required(login_url='signin')
def product(request,idProduct):
    pro= get_object_or_404(Product,id=idProduct)
    context={
        'title':"product",
        "product":pro,
    }
    return render(request, 'products/product.html',context)

@login_required(login_url='signin')
def search(request):
    context={
        'title':"Search",
    }
    return render(request, 'products/search.html',context)