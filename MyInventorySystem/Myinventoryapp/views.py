from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages

# Create your views here.

def view_supplier(request, id):
    supplier_objects = Supplier.objects.all()
    x = get_object_or_404(Account, pk=id)
    return render(request, 'Myinventoryapp/view_supplier.html', {'supplier':supplier_objects, 'x':x})

def view_bottles(request, id):
    bottle_objects = WaterBottle.objects.all()
    x = get_object_or_404(Account, pk=id)
    return render(request, 'Myinventoryapp/view_bottles.html', {'bottles':bottle_objects, 'x':x})

def view_bottle_details(request, id, pk):
    x = get_object_or_404(Account, pk=id)
    b = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'Myinventoryapp/view_bottle_details.html', {'x':x, 'b':b})

def delete_bottle(request, id, pk):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles', id=id)

def add_bottle(request, id):
    if(request.method=="POST"):
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        mouthsize = request.POST.get('msize')
        color = request.POST.get('color')
        supplier = request.POST.get('supplier')
        currentquantity = request.POST.get('cquantity')
        checkSupplier = Supplier.objects.get(name=supplier)
        WaterBottle.objects.create(SKU=sku, brand=brand, cost=cost, size=size, mouth_size=mouthsize, color=color, supplied_by=checkSupplier, current_quantity=currentquantity)
        return redirect('view_supplier', id=id)
    else:
        supplier_objects = Supplier.objects.all()
        x = get_object_or_404(Account, pk=id)
        return render(request, 'Myinventoryapp/add_bottle.html', {'suppliers':supplier_objects, 'x':x})

def login(request):
    if(request.method=="POST"):
        username = request.POST.get('uname')
        password = request.POST.get('pword')
        checkUsername = Account.objects.filter(username = f'{username}')
        checkPassword = Account.objects.filter(password = f'{password}')
        if str(username) in str(checkUsername):
            if str(checkUsername) == str(checkPassword):
                x = get_object_or_404(Account, username=username)
                return redirect('view_supplier', id=x.pk)
            else:
                messages.warning(request, "Invalid login.")
                return render(request, 'Myinventoryapp/login.html')
        else:
                messages.warning(request, "Invalid login.")
                return render(request, 'Myinventoryapp/login.html')
    else:
        return render(request, 'Myinventoryapp/login.html')
    
def signup(request):
    if(request.method=="POST"):
        username = request.POST.get('uname')
        password = request.POST.get('pword')
        username_list = Account.objects.all().values('username')
        if username not in str(username_list): 
            Account.objects.create(username=username, password=password)
            messages.success(request, "Account created successfully.")
            return redirect('login')
        else:
            messages.warning(request, "Account already exists.")
            return render(request, 'Myinventoryapp/signup.html')
    else:
        return render(request, 'Myinventoryapp/signup.html')
    
def manage_account(request, id):
    x = get_object_or_404(Account, pk=id)
    return render(request, 'Myinventoryapp/manage_account.html', {'x':x})

def change_password(request, id):
    if(request.method=="POST"):
        current_password = request.POST.get('current_pword')
        new_password = request.POST.get('new_pword')
        retyped_password = request.POST.get('retyped_pword')
        checkPassword = Account.objects.filter(password = f'{current_password}')
        if current_password in str(checkPassword):
            if str(new_password) == str(retyped_password):
                Account.objects.filter(pk=id).update(password=new_password)
                return redirect('manage_account', id=id)
            else:
                messages.warning(request, "Invalid input.")
                x = get_object_or_404(Account, pk=id)
                return render(request, 'Myinventoryapp/change_password.html', {'x':x})
        else:
                messages.warning(request, "Invalid input.")
                x = get_object_or_404(Account, pk=id)
                return render(request, 'Myinventoryapp/change_password.html', {'x':x})
    else:
        x = get_object_or_404(Account, pk=id)
        return render(request, 'Myinventoryapp/change_password.html', {'x':x})
    
def delete_account(request, id):
    Account.objects.filter(pk=id).delete()
    return redirect('login')