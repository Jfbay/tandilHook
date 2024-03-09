from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required

from .models import Lure, Cloth, Tool
from .forms import LureForm, ClothForm, ToolForm, LoginForm, RegisterForm




# SITE -----------------//////////////////////////

def home(request):
    return render(request, 'myhtmls/index.html')
def aboutUs(request):
    return render(request, 'myhtmls/aboutus.html')
def products(request):
    return render(request, 'myhtmls/products.html')
def contactUs(request):
    return render(request, 'myhtmls/contact.html')

# REGISTRATION AND LOG IN -----------------//////////////////////////
# LOGIN------------------
def logIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('User has been authenticated')
                else:
                    return HttpResponse('The user is not active.')
            else:
                return HttpResponse('Oops! There is an error in the information you gave. Please, check for any mistakes')
    else:
        form = LoginForm()
        return render(request, 'home')
def loginhtml(request):
    return render(request, 'loginhtml')
# LOGOUT------------------
def logoutuser(request):
    logout(request)
    return redirect(request, 'home')

# REGISTRATION------------------
def createUser(request):
    data = {
        'form': RegisterForm()
    }
    print('DATA>>>>>>>>>>>>>>>>>', data)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('LLEGAMOS A ARMAR EL FORM')
        if form.is_valid():
            print('EL FORM ES VALIDO')
            form.save()
            print('SE GUARDO EL FORM EL FORM')
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
    return render(request, 'registration/registration.html', data)

# PRODUCTS -----------------//////////////////////////
def lures(request):
    lures = Lure.objects.all()
    return render(request, 'myhtmls/products/lures.html', {'lures': lures})
def clothing(request):
    clothing = Cloth.objects.all()
    return render(request, 'myhtmls/products/clothing.html', {'clothing': clothing})
def tools(request):
    tools = Tool.objects.all()
    return render(request, 'myhtmls/products/tools.html', {'tools': tools})


# EDIT PRODUCTS -----------------//////////////////////////
# ------CREATE
@permission_required('app_tandilHook.add_lure')
def addLure(request):
    productform = LureForm(request.POST or None, request.FILES or None)
    if productform.is_valid():
        productform.save()
        return redirect('lures')
    return render(request, 'myhtmls/modifyproducts/add/addlure.html', {'productform': productform})

@permission_required('app_tandilHook.add_cloth')
def addCloth(request):
    productform = ClothForm(request.POST or None, request.FILES or None)
    if productform.is_valid():
        productform.save()
        return redirect('clothing')
    return render(request, 'myhtmls/modifyproducts/add/addcloth.html', {'productform': productform})

@permission_required('app_tandilHook.add_tool')
def addTool(request):
    productform = ToolForm(request.POST or None, request.FILES or None)
    if productform.is_valid():
        productform.save()
        return redirect('tools')
    return render(request, 'myhtmls/modifyproducts/add/addtool.html', {'productform': productform})


# ------EDIT
@permission_required('app_tandilHook.edit_lure')
def editLure(request, id):
    lure = Lure.objects.get(id=id)
    productform = LureForm(request.POST or None, request.FILES or None, instance=lure)
    if productform.is_valid and request.POST:
        productform.save()
        return redirect('lures')
    return render(request, 'myhtmls/modifyproducts/edit/editlure.html', {'productform': productform})

@permission_required('app_tandilHook.edit_cloth')
def editCloth(request, id):
    cloth = Cloth.objects.get(id=id)
    productform = ClothForm(request.POST or None, request.FILES or None, instance=cloth)
    return render(request, 'myhtmls/modifyproducts/edit/editcloth.html', {'productform': productform})

@permission_required('app_tandilHook.edit_tool')
def editTool(request, id):
    tool = Tool.objects.get(id=id)
    productform = ToolForm(request.POST or None, request.FILES or None, instance=tool)
    return render(request, 'myhtmls/modifyproducts/edit/edittool.html',  {'productform': productform})


# ------DELETE
@permission_required('app_tandilHook.delete_lure')
def deleteLure(request, id):
    lure = Lure.objects.get(id=id)
    lure.delete()
    return redirect('lures')

@permission_required('app_tandilHook.delete_cloth')
def deleteCloth(request, id):
    cloth = Cloth.objects.get(id=id)
    cloth.delete()
    return redirect('clothing')

@permission_required('app_tandilHook.delete_tool')
def deleteTool(request, id):
    tool = Tool.objects.get(id=id)
    tool.delete()
    return redirect('tool')