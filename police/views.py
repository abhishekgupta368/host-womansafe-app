from django.shortcuts import render,HttpResponse,redirect
from .forms import PoliceSignInForm
from .forms import PoliceRegistration
from .models import Police,Location
from .CountryStateClass import CountryStateData
from datetime import datetime
import folium
import random
from django.core import serializers
from django.http import JsonResponse
import collections
import json

# Create your views here.
def LoadLogin(request):
    return redirect('LogIn')

def LogIn(request):
    context = {}
    if request.method == "POST":
        signIn = PoliceSignInForm(request.POST)
        try:
            u_name = Police.objects.get(username = request.POST['username'])
            if(u_name.password == request.POST['password']):
                request.session['username'] = u_name.username
                return redirect('home')
            else:
                signIn = PoliceSignInForm()
            context = {
                'form':signIn,
                'alert':"Username or Password Invalid"
            }
            return render(request, "index.html",context)
        except:
            signIn = PoliceSignInForm()
            context = {
                'form':signIn,
                'alert':"Username Not Register"
            }
            return render(request, "index.html",context)
    else:
        signIn = PoliceSignInForm()
        context = {
            'form':signIn
        }
        return render(request,'index.html',context)
        
    return HttpResponse("Error Arises")

def HomePage(request):
    context={
        'username':request.session['username']
    }
    return render(request,'home.html',context)

def sign_out(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('LogIn')

def genrateLocationUrl(latDes,lngDes):
    url = "https://www.google.com/maps/dir/?api=1"
    destination = "&destination=" + latDes + "," + lngDes
    return str(url+destination)

def get_complaint_location(request):
    location = Location.objects.all()
    url_list = []
    for data in location:
        url_list.append(genrateLocationUrl(data.latitude,data.longitude))
    
    final_location_data = zip(location,url_list)
    context = {
        'location':final_location_data
    }
    return render(request,"complaints.html",context)

def design_map(location_object,state_name):
    temp = CountryStateData().getCoodinates(state_name.capitalize())
    clst_map = folium.Map(temp,zoom_start=10)
    
    for data in location_object:
        tag = folium.Html("<b>"+str(data.android_id)+"</b>",script=True)
        pop_up = folium.Popup(tag,max_width=2650)
        folium.Marker(location=[data.latitude,data.longitude],popup =pop_up).add_to(clst_map)

    clst_map =clst_map._repr_html_()
    return clst_map

def empty_map():
    clst_map = folium.Map([20.5937,78.9629],zoom_start=5)
    clst_map =clst_map._repr_html_()
    return clst_map


def analysisHome(request):
    list_of_states = CountryStateData().getCityList()
    if(request.method=='POST'):
        start_date = datetime.strptime(request.POST['staring_date'], "%H:%M %m/%d/%Y")
        end_date = datetime.strptime(request.POST['ening_date'], "%H:%M %m/%d/%Y")
        state_name = request.POST['state_name'].lower()
        filtered_location = Location.objects.filter(timestamp__gte=start_date, timestamp__lte=end_date,state=state_name.lower())
        if(state_name is not None and start_date is not None and end_date is not None):
            context = {
                'locations': list_of_states,
                'map_obj':design_map(filtered_location,state_name)
            } 
            return render(request,"analysis.html",context) 
        else:
            print("empty state")
            context = {
                'locations': list_of_states,
                'map_obj':empty_map()
            } 
            return render(request,"analysis.html",context)
    else:
        context = {
                'locations': list_of_states,
                'map_obj':empty_map()
            } 
        return render(request,"analysis.html",context)

#--------------------------------------------------------------------
def register_to_system(request):
    if(request.method == 'POST'):
        PoliceReg = PoliceRegistration(request.POST)
        if(PoliceReg.is_valid()):
            PoliceReg.save()
            request.session['username'] = PoliceReg.cleaned_data['username']
            return redirect('home')
    else:
        PoliceForm = PoliceRegistration()
        context = {
            "policeForm":PoliceForm
        }
        return render(request,'registoration.html',context)
    
#-------------------------------------------------
def return_states_counts(request):
    if(request.method=='POST'):
        states = []
        start_date = datetime.strptime(request.POST['staring_date'], "%H:%M %m/%d/%Y")
        end_date = datetime.strptime(request.POST['ening_date'], "%H:%M %m/%d/%Y")
        filtered_location = Location.objects.filter(timestamp__gte=start_date, timestamp__lte=end_date)

        for data in filtered_location:
            states.append(data.state.capitalize())
        states = dict(collections.Counter(states))
        state_name = []
        state_cnt = []
        for name,cnt in states.items():
            state_name.append(str(name))
            state_cnt.append(int(cnt))

        # print(state_name)
        # print(state_cnt)

        context ={
            'states': state_name,
            'count':state_cnt
        }
        return render(request,'present_graph.html', context)
    else:
        context ={
            'states': [],
            'count':[]
        }
        return render(request,'present_graph.html',context)
##--------------------------------------------------------------------

def delete_complaint(request,id):
    Location.objects.filter(id=id).delete()
    return redirect('complaint_locations')