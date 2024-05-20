from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicle, Chalan
from .form import VehicleForm, ChalanForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
#vehical View
@login_required
def VehicalFormView(request):
    form=VehicleForm()
    if request.method =='POST':
        form=VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False) 
            vehicle.owner = request.user      
            vehicle.save()
                #form.save()
            #return HttpResponse('Vehical Data Added')
            return redirect('vehicle_list')
    template_name='testapp/vehical_form.html'
    context={'form':form}
    return render (request,template_name,context)
@login_required
def VehicalUpdateView(request,pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            #return HttpResponse('Data Updated Successfully')
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    
    template_name = 'testapp/vehical_form.html'
    context = {'form': form}
    return render(request, template_name, context)
    


def VehicalDetailsView(request):
    form=Vehicle.objects.all()
    #form=Vehicle.objects.filter(owner=request.user)
    template_name='testapp/vehical_show.html'
    context={'form':form}
    return render (request,template_name,context)

#Chalan View
@login_required
def ChalanFormView(request):
    form=ChalanForm()
    if request.method =='POST':
        form=ChalanForm(request.POST)
        if form.is_valid():
                form.save()
                #return HttpResponse('chalan Data Added')
                return redirect('chalan_list')
    template_name='testapp/chalan_form.html'
    context={'form':form}
    return render (request,template_name,context)
@login_required
def ChalanUpdateView(request,pk):
    chalan = get_object_or_404(Chalan, pk=pk)
    
    if request.method == 'POST':
        form = ChalanForm(request.POST, instance=chalan)
        if form.is_valid():
            form.save()
            #return HttpResponse('Chalan Updated Successfully')
            return redirect('chalan_list')
    else:
        form = ChalanForm(instance=chalan)
    
    template_name = 'testapp/chalan_form.html'
    context = {'form': form}
    return render(request, template_name, context)
    
@login_required
def ChalanDetailsView(request):
    form=Chalan.objects.all()
    #form=Chalan.objects.filter(vehicle__owner=request.user)
    template_name='testapp/chalan_show.html'
    context={'form':form}
    return render (request,template_name,context)


# Create your views here.
def RegisterView(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            #return HttpResponse('Login successfully')
            return redirect ('login')
    template_name='testapp/signup.html'
    context={'form':form}
    return render(request, template_name, context)


def loginView(request):
    print('inside login')
    if request.method == 'POST':
        # print('USER IS POST')
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        # print(un,pw)
        user=authenticate(request,username=un,password=pw)
        print('Auth',user)
        users=User.objects.all()
        # print('***************************************************',users)
        print(user is  None)
        if user is not None:

            login(request,user)
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            #return HttpResponse('Login successfully')
            return redirect('vehicle_create')
        else:
            messages.error(request, 'Invalid username or password.')
    template_name='testapp/login.html'
    context={}
    return render(request, template_name, context)


def logoutView(request):

        logout(request)
        return redirect ('login')

# def redirect_to_login(request):
#     return redirect('login')

