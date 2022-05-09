from django.urls import path
from . import views

urlpatterns = [
   
    #Paths de nuestra pagina
    #path('signin', views.signin, name='signin'),
    path('logout', views.logout_view, name='logout'),
    path('', views.login_user, name='login_user'),
    path('signinUser', views.signinUser, name='signinUser'),
    path('admin/index', views.inicioH, name='index'),
    path('admin/users', views.users, name='users'),
    path('admin/users/create', views.createUser, name='createUser'),
    path('admin/users/update/<int:pk>', views.updateUser, name='updateUser'),
    path('admin/users/delete/<int:pk>', views.deleteUser, name='deleteUser'),
    path('admin/churchs', views.churchs, name='churchs'),
    path('admin/churchs/create', views.createChurch, name='createChurch'),
    path('admin/churchs/update/<int:pk>', views.updateChurch, name='updateChurch'),
    path('admin/churchs/delete/<int:pk>', views.deleteChurch, name='deleteChurch'),
    path('admin/parameters/<int:pk>', views.parameters, name='parameters'),
    path('admin/parameters/create/<int:pk>', views.createParameter, name='createParameter'),
    path('admin/parameters/update/<int:pk>', views.updateParameter, name='updateParameter'),
    #path('admin/users/update/parameters/<int:pk>', views.updateParameterUser, name='updateParameterUser'),
    path('admin/parameters/delete/<int:pk>', views.deleteParameter, name='deleteParameter'),
    path('user/index',views.userIndex, name='userIndex'),
    #funcion search
    path('admin/users/search', views.search, name='search'),
    path('admin/registro', views.registro, name="registro"),
    #-----Dashboardlinks-----
    path('admin/users/dashboardr/<int:pk>', views.dashreloj, name='dashboardr'),
    path('users/dashboardr/<int:pk>', views.dashreloju, name='dash'),
    
] 

