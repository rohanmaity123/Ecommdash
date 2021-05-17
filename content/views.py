from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import category,subcategory,product
from django.contrib import messages
from .forms import categoryform
# from django.views.decorators.csrf import csrf_exempt

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
        form = categoryform(request.POST or None, request.FILES or None)
        return render(request, 'addcategory.html',{'form':form})

# @csrf_exempt
def savecategory(request):
    if request.method == 'POST':
        categoryname = request.POST['name']
        categoryimage = request.POST['image']
        print(categoryname,categoryimage)
        insert = category.objects.create(name=categoryname,image=categoryimage,status=True)
        print(insert)
        insert.save()
        return JsonResponse({'status':'Save'})        
    else:
        return JsonResponse({'status':0})
        

def managecategory(request):
    allcategory = category.objects.all()
    params = {'category':allcategory}
    return render(request, 'managecategory.html',params)

def deletecategory(request):
    if request.method == 'POST':
        catId = request.POST.get('catagoryID')
        query = category.objects.get(pk=catId)
        query.delete()

        return JsonResponse({'status':1}) 
    else:
        return JsonResponse({'status':0})

def getcategory(request,pk):
    mycategory = category.objects.get(id=pk)
    params = {'category':mycategory}
    return render(request, 'editcategory.html',params)

def editcategory(request,pk):
    if request.method == 'POST':
        categoryname = request.POST['category']
        categoryimage = request.FILES['image']
        update = category.objects.create(id=pk,name=categoryname,image=categoryimage,status=True)
        update.save()
        messages.success(request,'Category Edited Successfully')
        allcategory = category.objects.all()
        params = {'category':allcategory}
        return render(request, 'managecategory.html',params)
    else:
        allcategory = category.objects.all()
        params = {'category':allcategory}
        return render(request, 'managecategory.html',params)

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

def addproduct(request):
    if request.method == 'POST':

        subcatid = request.POST['sub_id']
        pname = request.POST['product']
        price = request.POST['price']
        quantity = request.POST['quantity']
        unit = request.POST['unit']
        image = request.FILES['image']

        # print(subcatid,pname,price,quantity,unit,image)
        insert = product.objects.create(subcatId=subcatid,name=pname,price=price,quantity=quantity,unit=unit,image=image,status=True)
        insert.save()
        messages.success(request,'Product added Successfully')

        allcategory = category.objects.all()
        params = {'category':allcategory}
        return render(request, 'addproduct.html',params)
    else:
        allcategory = category.objects.all()
        params = {'category':allcategory}
        return render(request, 'addproduct.html',params)

#ajax func
def selectcategory(request):
    catId = request.GET.get('cat_id')
    subcat = subcategory.objects.filter(catId=catId)
    print(subcat)
    return render(request, 'subdropdown.html',{'subcategory':subcat})

def manageproduct(request):
    allproduct = product.objects.all()
    params = {'product':allproduct}
    return render(request, 'manageProduct.html',params)