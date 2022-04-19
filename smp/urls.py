from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home, name ="home"),
    path('portfolio/', views.portfolio, name ="portfolio"),
    path('watchlist/', views.watchlist, name ="watchlist"),
    path('price_prediction/', views.price_prediction, name ="price_prediction"),
]
