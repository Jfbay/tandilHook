from django.shortcuts import render, redirect

from .models import Lure, Cloth, Tool
from .forms import LureForm, ClothForm, ToolForm



# SITE -----------------//////////////////////////

def base(request):
    return render(request, 'myhtmls/base.html')
def index(request):
    return render(request, 'myhtmls/index.html')
def aboutUs(request):
    return render(request, 'myhtmls/aboutus.html')
def products(request):
    return render(request, 'myhtmls/products.html')
def contactUs(request):
    return render(request, 'myhtmls/contact.html')

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
def addLure(request):
    productform = LureForm(request.POST or None, request.FILES or None)
    if productform.is_valid():
        productform.save()
        return redirect('lures')
    return render(request, 'myhtmls/modifyproducts/add/addlure.html', {'productform': productform})

def addCloth(request):
    productform = ClothForm(request.POST or None, request.FILES or None)
    if productform.is_valid():
        productform.save()
        return redirect('clothing')
    return render(request, 'myhtmls/modifyproducts/add/addcloth.html', {'productform': productform})

def addTool(request):
    productform = ToolForm(request.POST or None, request.FILES or None)
    if productform.is_valid():
        productform.save()
        return redirect('tools')
    return render(request, 'myhtmls/modifyproducts/add/addtool.html', {'productform': productform})


# ------EDIT
def editLure(request, id):
    lure = Lure.objects.get(id=id)
    productform = LureForm(request.POST or None, request.FILES or None, instance=lure)
    if productform.is_valid and request.POST:
        productform.save()
        return redirect('lures')
    return render(request, 'myhtmls/modifyproducts/edit/editlure.html', {'productform': productform})
def editCloth(request, id):
    cloth = Cloth.objects.get(id=id)
    productform = ClothForm(request.POST or None, request.FILES or None, instance=cloth)
    return render(request, 'myhtmls/modifyproducts/edit/editcloth.html', {'productform': productform})
def editTool(request, id):
    tool = Tool.objects.get(id=id)
    productform = ToolForm(request.POST or None, request.FILES or None, instance=tool)
    return render(request, 'myhtmls/modifyproducts/edit/edittool.html',  {'productform': productform})


# ------DELETE
def deleteLure(request, id):
    lure = Lure.objects.get(id=id)
    lure.delete()
    return redirect('lures')
def deleteCloth(request, id):
    cloth = Cloth.objects.get(id=id)
    cloth.delete()
    return redirect('clothing')
def deleteTool(request, id):
    tool = Tool.objects.get(id=id)
    tool.delete()
    return redirect('tool')