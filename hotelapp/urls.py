from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name = ''),
    path('detail',HotelDetailsView.as_view(), name = 'detail'),
    path('ldetail',DetailsVeiw.as_view(), name = 'ldetail'),
    path('ddetail/<int:pid>',hotelRemoveList.as_view(), name = 'ddetail'),
    path('edetail/<int:pid>',EditHotel.as_view(), name = 'edetail'),







]