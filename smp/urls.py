from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name ="home"),
    path('portfolio/', views.portfolio, name ="portfolio"),
    path('watchlist/', views.watchlist, name ="watchlist"),
    path('price_prediction/', views.price_prediction, name ="price_prediction"),
    path('signup/', views.signup, name="signup")
]
