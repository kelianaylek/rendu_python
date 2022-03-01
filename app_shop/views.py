from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from .models import Product
from .forms import ProductForm

def index(request):
    context ={}
    context["dataset"] = Product.objects.all()

    return render(request,'app_shop/index.html', context)

def details(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
    context["range"] = range(1, context["data"].quantity+1)

    return render(request, "app_shop/details.html", context)

def update(request, id):

    items = request.POST.get('quantity')

    obj = get_object_or_404(Product, id = id)

    Product.objects.filter(id = id).update(quantity = obj.quantity - int(items))
    obj.refresh_from_db()

    return HttpResponseRedirect("/shop")
