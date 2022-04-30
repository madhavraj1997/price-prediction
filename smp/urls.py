
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views  

urlpatterns = [
    
    path('', views.home, name ="home"),
    path('portfolio/', views.portfolio, name ="portfolio"),
    path('watchlist/', views.watchlist, name ="watchlist"),
    path('price_prediction/', views.price_prediction, name ="price_prediction"),
    path('signup/', views.signup, name="signup"),
    path('/logout/', views.logoutuser, name="logout"),
    path('stockform/', views.Stockform, name="stockform"),
    path('add-stock/', views.add_stock, name="add_stock"),
    path('add-portfolio/', views.add_portfolio, name="add_portfolio"),
    path('add-watchlist/', views.add_watchlist, name="add_watchlist"),

    # path('accounts/', include('django.contrib.auth.urls')),



    # reset password url
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"), name= "password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_done.html"), name= "password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_confirm.html"), name= "password_reset_confirm"),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_complete.html"), name= "password_reset_complete"),

]

  