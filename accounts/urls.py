from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import login_request,register_request
from .views import logout_view

urlpatterns = [
    path('register/',register_request, name="Registro"),
    path('login/', login_request, name="Login"),
    #path('logout/', LogoutView.as_view(template_name="templates/accounts/logout.html"), name="Logout"),#
    path('logout/', logout_view, name='logout'),
    ]