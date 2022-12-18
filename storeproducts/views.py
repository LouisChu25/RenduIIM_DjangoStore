from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Product
from .forms import ProductForm

def create_view(request):
    context= {}

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context['form']= form
    return render(request, "create.html", context)

def list_view(request):
    context={}

    context["dataset"] = Product.objects.all()

    return render(request, "list.html", context)


def detail_view(request, id):
    context ={}
 
    context["data"] = Product.objects.get(id = id)
         
    return render(request, "details.html", context)


def update_view(request, id):
    context ={}
 
    obj = get_object_or_404(Product, id = id)
 
    form = ProductForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "edit.html", context)

def delete_view(request, id):
    context ={}
 
    obj = get_object_or_404(Product, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "delete.html", context)