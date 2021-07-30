from django.shortcuts import render,HttpResponseRedirect
from .forms import RTA_registration
from .models import User
# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = RTA_registration(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['Name']
            d = fm.cleaned_data['Driving_License_number']
            v = fm.cleaned_data['Vehicle_number']
            vc = fm.cleaned_data['Vehicle_color']
            m = fm.cleaned_data['Month_year_of_manufacture']
            i = fm.cleaned_data['Insurance_company_name']
            inf = fm.cleaned_data['Insurance_valid_from']
            inst = fm.cleaned_data['Insurance_valid_to']
            p = fm.cleaned_data['Pending_Challans']
            a = fm.cleaned_data['Address']
            reg = User(Name=n,Driving_License_number=d,Vehicle_number=v,Vehicle_color=vc,Month_year_of_manufacture=m,Insurance_company_name=i,
                       Insurance_valid_from=inf,Insurance_valid_to=inst,Pending_Challans=p,Address=a)
            reg.save()
            fm = RTA_registration()
    else:
        fm = RTA_registration()
    reg = User.objects.all()
    return render(request,'addandshow.html',{'form':fm,'w':reg})


def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = RTA_registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = RTA_registration(instance=pi)
    return render(request,'update.html',{'form':fm})



def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



