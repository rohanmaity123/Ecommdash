from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import category,subcategory
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def addcategory(request):
    if request.method == 'POST':
        categoryname = request.POST['category']
        categoryimage = request.FILES['image']

        insert = category.objects.create(name=categoryname,image=categoryimage,status=True)
        insert.save()
        messages.success(request,'Category added Successfully')
        return render(request, 'addcategory.html')
    else:

        return render(request, 'addcategory.html')

def managecategory(request):
    allcategory = category.objects.all()
    params = {'category':allcategory}
    return render(request, 'managecategory.html',params)

def deletecategory(request,pk):
    catid = category.objects.get(id=pk)
    catid.delete()
    messages.success(request,'Category Deleted Successfully')
    allcategory = category.objects.all()
    params = {'category':allcategory}
    return render(request, 'managecategory.html',params)

def getcategory(request,pk):
    mycategory = category.objects.get(id=pk)
    params = {'category':mycategory}
    return render(request, 'editcategory.html',params)

def editcategory(request,pk):
    if request.method == 'POST':
        categoryname = request.POST['category']
        categoryimage = request.FILES['image']
        update = category.objects.update(id=pk,name=categoryname,image=categoryimage,status=True)
        update.save()
        messages.success(request,'Category Edited Successfully')
        mycategory = category.objects.get(id=pk)
        params = {'category':mycategory}
        return render(request, 'editcategory.html',params)
    else:
        mycategory = category.objects.get(id=pk)
        params = {'category':mycategory}
        return render(request, 'editcategory.html',params)

def addsubcategory(request):
    if request.method == 'POST':
        catid = request.POST['select']
        subcatname = request.POST['subcategory']
        subcatimage = request.FILES['image']
        print(catid,subcatname,subcatimage)
        insert = subcategory.objects.create(catId=catid,name=subcatname,image=subcatimage,status=True)
        insert.save()
        messages.success(request,'Subcategory added Successfully')
        allcategory = category.objects.all()
        params = {'category':allcategory}
        return render(request, 'addsubcategory.html',params)
    else:
        allcategory = category.objects.all()
        params = {'category':allcategory}
        return render(request, 'addsubcategory.html',params)

def managesubcategory(request):
    allsubcategory = subcategory.objects.all()
    params = {'subcategory':allsubcategory}
    return render(request, 'managesubcategory.html',params)

def deletesubcategory(request,pk):
    subcatid = subcategory.objects.get(id=pk)
    subcatid.delete()
    messages.success(request,'Sub-Category Deleted Successfully')
    allsubcategory = subcategory.objects.all()
    params = {'subcategory':allsubcategory}
    return render(request, 'managecategory.html',allsubcategory)