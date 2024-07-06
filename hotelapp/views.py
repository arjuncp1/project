from django.shortcuts import render, redirect
from django.views import View
from .forms import HotelDetailsFrom
from .models import Hotel

# Create your views here.



    
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class HotelDetailsView(View):
    def get(self, request):
        form = HotelDetailsFrom()
        return render(request, 'hoteldetails.html',{'form': form})
    
    def post(self, request):
        form_data = HotelDetailsFrom(data =request.POST)
        if form_data.is_valid():
            name = form_data.cleaned_data.get('name')
            place = form_data.cleaned_data.get('place')
            phone = form_data.cleaned_data.get('phone')
            email = form_data.cleaned_data.get('email')
            Hotel.objects.create(name = name, place= place, phone = phone, email = email)
            return redirect('')
        
        return render(request, 'hoteldetails.html',{'form': form_data})

class DetailsVeiw(View):
    def get(self, request):
        data = Hotel.objects.all()
    
        return render(request, 'detailsview.html',{'data': data})
    
    
class hotelRemoveList(View):
    def get(self, request, **kwrgs):
        pid = kwrgs.get('pid')
        hotel = Hotel.objects.get(id = pid) 
        hotel.delete()
        return redirect('ldetail')
    



class EditHotel(View):
    def get(self, request,**kwrgs):
        pid = kwrgs.get('pid')
        hotel = Hotel.objects.get(id = pid)
        form = HotelDetailsFrom(initial={'name':hotel.name, 'place':hotel.place, 'phone': hotel.phone,'email':hotel.email})
        return render(request, 'edithotel.html',{'form': form})
    
    def post(self , request , **kwrgs):
        pid = kwrgs.get('pid')
        hotel = Hotel.objects.get(id = pid)
        form_data = HotelDetailsFrom(data = request.POST)
        if form_data.is_valid():
            name = form_data.cleaned_data.get('name')
            place = form_data.cleaned_data.get('place')
            phone = form_data.cleaned_data.get('phone')
            email = form_data.cleaned_data.get('email')

            hotel.name = name
            hotel.place = place
            hotel.phone = phone
            hotel.email = email
            hotel.save()

            return redirect('ldetail')


        
        return render(request, 'edithotel.html',{'form': form_data})
    































    