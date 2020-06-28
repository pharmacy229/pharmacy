from med.forms import medicineform
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from med.models import medicine, blog, subscribe, contactus, upload
from med.forms import SubscribeForm, contactusForm, uploadForm
from cart.forms import CartAddProductForm

# Create your views here.

class homeview(TemplateView):
    template_name="home.html"
class aboutview(TemplateView):
    template_name="about.html"
class contactusview(TemplateView):
    template_name="contactus.html"    


def product_list(request):
    products = medicine.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'medicine.html', context)


 
    
class blogview(ListView):
    template_name="blog.html"  
    def get_queryset(self):
        return blog.objects.all()
class signinview(TemplateView):
    template_name="signin.html"   
class suscribeview(TemplateView):
    template_name="suscribe.html"    
class uploadview(TemplateView):
    template_name="upload.html"        
class blogdetailview(TemplateView):
    template_name="blogdetail.html"    
class blog1view(TemplateView):
    template_name="blog1.html"
class blog2view(TemplateView):
    template_name="blog2.html"
class cartdetailview(TemplateView):
    template_name="cartdetail.html"
def insertsubscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/suscribe/')
            except:
                pass
    else:
        form = SubscribeForm()
    return render(request, 'subscribe.html', {'form': form}) 
    
def insertcontactus(request):
    if request.method == "POST":
        form = contactusForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/contact/')
            except:
                pass
    else:
        form = contactusForm()
    return render(request, 'contactus.html', {'form': form})     
    

def insertupload(request):
    if request.method == "POST":
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/upload/')
            except:
                pass
    else:
        form = uploadForm()
    return render(request, 'upload.html', {'form': form}) 
    
    
def insert(request):
    if request.method=='POST':
        form=medicineform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/medicine/')
            except:
                pass
        else:
            form=medicineform()
        return render(request,'medicine.html',{'form':form})
        

def showblog(request, id):
    pro = blog.objects.filter(id=id)
   
    context = {
        'pro': pro,
        
    }
    return render(request, "blogdetail.html", context)        
    
