from django.shortcuts import render,get_object_or_404,redirect
from .models import Item

def create_item(request):
    if request.method =='Post':
        name=request.POST.get('name')
        description=request.POST.get('description')
        Item.objects.create(name=name,description=description)
        return redirect('item_list')
    return render(request,'item_form.html')

#read
def read_item(request):
    items=Item.objects.all()
    return render(request,'item_list.html',{'items':items})

def update_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.methos=='POST':
        item.name=request.POST.get('name')
        item.description=request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request,'item_form.html',{'item':item})

# Create your views here.
#delete
def delete_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('item_list')
    return render(request,'item_confirm_delete.html',{'item':item})
