from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from http.client import HTTPResponse
from django.http import HttpResponse
from itertools import product
from urllib.parse import uses_relative
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import ParameterSerializer, UserTSerializer
from .serializers import ChurchSerializer
from .models import UserT, Extended, User
from .models import Church
from .models import Parameter
from .forms import ParameterForm, UserTForm, ChurchForm, RegisterForm
from django.urls import reverse
from datetime import date

""""
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/', 
        'Detail View': '/usert-detail/<int:id>',
        'Create': '/usert-create/',
        'Update': '/usert-update/<int:id>',
        'Delete': '/usert-detail/<int:id>'
    }
    return Response(api_urls);
"""

"""
def inicio(request):
    return render(request, "pages/inicio.html")

def nosotros(request):
    return render(request, 'pages/nosotros.html')

#Funciones de nuestra pagina
def inicioH(request):
    return render(request, "real/index.html")


def signinUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            messages.success(request, (request, f'Usuario {name} Se ha creado el usuario exitosamente'))
            return redirect('feed')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request,'real/registro.html', context)

"""

def signin(request):
    return render(request, "real/siginUser.html")

def signinUser(request):
    formulario = UserTForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('login_user')
    return render(request, 'real/registro.html', {'formulario': formulario})
  
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.extension.isAdmin:
                return redirect('index')
            else:
                return redirect('userIndex')
        else:
            messages.success(request, ("Verifica el usuario o contraseña que ingresaste"))
            return redirect('login_user')
    else:
        return render(request, "real/login.html", {})

#funcion search bar
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Extended.objects.filter(user__first_name__contains=searched)
        return render(request, "users/search.html", {'searched':searched,'results':results})
    else:
        return render(request, "users/search.html", {})
    
def userIndex(request):

    user = request.user
    return render(request, "real/adminindex.html", {'extension': user.extension})

def logout_view(request):
    return logout(request, "real/index.html")


def inicioH(request):
    return render(request, "real/index.html")

# .only('ID_User','firstName', 'lastName', 'gender', 'phone', 'mail', 'id_church')
def users(request):
    users = Extended.objects.all()

    if request.method == "POST":
        searched = request.POST['searched']
        if searched:
            users = Extended.objects.filter(user__first_name__icontains=searched)
    return render(request, 'users/users.html', {'users': users})

def churchs(request):
    churchs = Church.objects.all()
    return render(request, 'users/churchs.html', {'churchs': churchs})

def parameters(request,pk):
    user = User.objects.get(pk=pk)
    extension = user.extension
    try:
        parameter = user.prueba
    except:
        return redirect(reverse('createParameter',kwargs={"pk":user.pk}))

    return render(request, 'users/parameters.html', {'parameter': parameter, 'extension': extension})

def admins(request):
    admins = UserT.objects.all()
    return render(request, 'users/users.html', {'admins': admins})

def createUser(request):
    formulario = RegisterForm(request.POST or None)
    print("ff")
    if formulario.is_valid():
        username = formulario.cleaned_data["username"]
        firstName = formulario.cleaned_data["firstName"]
        lastName = formulario.cleaned_data["lastName"]
        gender = formulario.cleaned_data["gender"]
        phone = formulario.cleaned_data["phone"]
        password = formulario.cleaned_data["password"]
        mail = formulario.cleaned_data["mail"]
        id_church = formulario.cleaned_data["id_church"]
        isAdmin = formulario.cleaned_data["isAdmin"]
        user=User()
        extended=Extended()

        user.username = username
        user.first_name = firstName
        user.last_name = lastName
        user.email = mail
        user.password = password
        user.set_password(user.password)
        user.save()

        extended.user = user
        extended.gender = gender
        extended.phone = phone 
        extended.id_church = id_church
        extended.isAdmin = isAdmin
        extended.save()

        return redirect('users')
    return render(request, 'users/createUser.html', {'formulario': formulario})

def updateUser(request, pk):
    user = User.objects.get(pk=pk)
    extension=user.extension
    initial = {
        "username":user.username,
        "firstName":user.first_name,
        "lastName":user.last_name,
        "gender":extension.gender,
        "phone":extension.phone,
        "password":user.password,
        "mail":user.email,
        "id_church":extension.id_church,
        "isAdmin":extension.isAdmin
    }

    formulario = RegisterForm(request.POST or None, initial=initial)
    if formulario.is_valid() and request.POST:
        user.username = formulario.cleaned_data["username"]
        user.first_name = formulario.cleaned_data["firstName"]
        user.last_name = formulario.cleaned_data["lastName"]
        extension.gender = formulario.cleaned_data["gender"]
        extension.phone = formulario.cleaned_data["phone"]
        user.password = formulario.cleaned_data["password"]
        user.email = formulario.cleaned_data["mail"]
        extension.id_church = formulario.cleaned_data["id_church"]
        extension.isAdmin = formulario.cleaned_data["isAdmin"]
        user.save()
        extension.save()
        return redirect('users')
    return render(request, 'users/updateUser.html', {'formulario': formulario})

def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('users')

def createChurch(request):
    formulario = ChurchForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('churchs')
    return render(request, 'users/createChurch.html', {'formulario': formulario})

def updateChurch(request, pk):
    user = Church.objects.get(id_church=pk)
    formulario = ChurchForm(request.POST or None, request.FILES or None, instance=user)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('churchs')
    return render(request, 'users/updateChurch.html', {'formulario': formulario})

def deleteChurch(request, pk):
    user = Church.objects.get(id_church=pk)
    user.delete()
    return redirect('churchs')

def createParameter(request,pk):
    formulario = ParameterForm(request.POST or None)
    user = User.objects.get(pk=pk)
    extension = user.extension
    if Parameter.objects.filter(ID_User=user).exists():
        return redirect(reverse('parameters',kwargs={"pk":user.pk}))
    if formulario.is_valid():
        parametros = formulario.save(commit=False)
        parametros.lastupdate = date.today()
        parametros.ID_User = user
        parametros.save()
        return redirect(reverse('parameters',kwargs={"pk":user.pk}))
    return render(request, 'users/createParameter.html', {'formulario': formulario, 'extension': extension})

def updateParameter(request, pk):
    user = User.objects.get(pk=pk)
    parametro = user.prueba
    formulario = ParameterForm(request.POST or None, instance=parametro)
    if formulario.is_valid() and request.POST:
        formulario.instance.lastupdate = date.today()
        formulario.save()
        return redirect(reverse('parameters',kwargs={"pk":user.pk}))
    return render(request, 'users/updateParameter.html', {'formulario': formulario, 'extension': user.extension})

# def updateParameterUser(request, pk):
#     user = User.objects.get(pk=pk)
#     formulario = ParameterForm(request.POST or None, request.FILES or None, instance=user)
#     if formulario.is_valid() and request.POST:
#         formulario.save()
#         return redirect('parameters')
#     return render(request, 'users/updateParameter.html', {'formulario': formulario})

def deleteParameter(request, pk):
    user = Parameter.objects.get(id_parameter=pk)
    user.delete()
    return redirect('parameters')

def registro(request):
    formulario = RegisterForm(request.POST or None)
    if formulario.is_valid():
        username = formulario.cleaned_data["username"]
        firstName = formulario.cleaned_data["firstName"]
        lastName = formulario.cleaned_data["lastName"]
        gender = formulario.cleaned_data["gender"]
        phone = formulario.cleaned_data["phone"]
        password = formulario.cleaned_data["password"]
        mail = formulario.cleaned_data["mail"]
        id_church = formulario.cleaned_data["id_church"]
        user=User()
        extended=Extended()

        user.username = username
        user.first_name = firstName
        user.last_name = lastName
        user.email = mail
        user.password = password
        user.set_password(user.password)
        user.save()

        extended.user = user
        extended.gender = gender
        extended.phone = phone 
        extended.id_church = id_church
        extended.save()

        return redirect('login_user')
    return render(request, 'real/registro.html', {'formulario': formulario})

#--------------------- Dashboard functions ---------------------------

def dashB(request,pk):
    #user = UserT.objects.get(ID_User=pk)
    parameters = Parameter.objects.get(ID_User=pk)
    return render(request, "real/dashboard.html", {'parameters': parameters})

def color_advmmse(unit):
    if unit <= 18:
        return 'progress-bar bg-danger'
    elif unit <25:
        return 'progress-bar bg-warning'
    else:
        return 'progress-bar bg-success'

def color_advgijon(unit):
    if unit <= 7:
        return 'progress-bar bg-success'
    elif unit <10:
        return 'progress-bar bg-warning'
    else:
        return 'progress-bar bg-danger'

def color_advclock(unit):
    if unit >= 2:
        return 'progress-bar bg-success'
    elif unit ==1:
        return 'progress-bar bg-warning'
    else:
        return 'progress-bar bg-danger'

def parameter_advclock(unit):
    if unit >= 2:
        return 100
    elif unit ==1:
        return 60
    else:
        return 30

def color_advglobalsppb(unit):
    if unit >= 8:
        return 'progress-bar bg-success'
    else:
        return 'progress-bar bg-warning'

def color_advfrailtycfs(unit):
    if unit == 0:
        return 'progress-bar bg-success'
    elif unit <=2:
        return 'progress-bar bg-warning'
    else:
        return 'progress-bar bg-danger'

def color_advhigheststrong(unit):
    if unit <= 27:
        return 'progress-bar bg-success'
    elif unit <=20:
        return 'progress-bar bg-warning'
    else:
        return 'progress-bar bg-danger'

def color_advgds(unit):
    if unit <= 5:
        return 'progress-bar bg-success'
    elif unit <= 9:
        return 'progress-bar bg-warning'
    else:
        return 'progress-bar bg-danger'

def color_advlwb(unit):
    if unit <= 6:
        return 'progress-bar bg-warning'
    elif unit <= 3:
        return 'progress-bar bg-danger'
    else:
        return 'progress-bar bg-success'

def dashreloj(request,pk):
    # parameters = Parameter.objects.get(ID_User=pk)
    # users = Extended.objects.get(user=pk)
    user = User.objects.get(id=pk)
    extension = user.extension
    try:
        parameters = Parameter.objects.get(ID_User=pk)
    except:
        return redirect(reverse('userIndex',kwargs={"pk":user.pk}))
        #print('not_argument_available')
    #fin
    parameters = Parameter.objects.get(ID_User=pk)
    dic_parameters = { 'totalmmse': (parameters.totalmmse * 100)/30, 'gijon': (parameters.gijon * 100)/17, 'clock': parameter_advclock(parameters.clock), 'globalsppb': (parameters.globalsppb * 100)/15, 'frailtycfs': ((parameters.frailtycfs * 50)/5)+50, 'higheststrong': (parameters.higheststrong * 100)/45, 'gds': ((parameters.gds * 100)/15)+2, 'lwb': (parameters.lwb * 100)/10}
    dic_color = {'totalmmse': color_advmmse(parameters.totalmmse), 'gijon': color_advgijon(parameters.gijon), 'clock': color_advclock(parameters.clock), 'globalsppb': color_advglobalsppb(parameters.globalsppb), 'frailtycfs': color_advfrailtycfs(parameters.frailtycfs), 'higheststrong': color_advhigheststrong(parameters.higheststrong), 'gds': color_advgds(parameters.gds), 'lwb': color_advlwb(parameters.lwb)}
    return render(request, "real/dashboard.html", {'parameters': parameters, 'dic_parameters': dic_parameters, 'color_adv': dic_color, 'extension': extension})

def dashreloju(request,pk):
    # parameters = Parameter.objects.get(ID_User=pk)
    # users = Extended.objects.get(user=pk)
    user = User.objects.get(id=pk)
    extension = user.extension
    try:
        parameters = Parameter.objects.get(ID_User=pk)
    except:
        return redirect(reverse('userIndex',kwargs={"pk":user.pk}))
        #print('not_argument_available')
    #fin
    parameters = Parameter.objects.get(ID_User=pk)
    dic_parameters = { 'totalmmse': (parameters.totalmmse * 100)/30, 'gijon': (parameters.gijon * 100)/17, 'clock': parameter_advclock(parameters.clock), 'globalsppb': (parameters.globalsppb * 100)/15, 'frailtycfs': ((parameters.frailtycfs * 50)/5)+50, 'higheststrong': (parameters.higheststrong * 100)/45, 'gds': ((parameters.gds * 100)/15)+2, 'lwb': (parameters.lwb * 100)/10}
    dic_color = {'totalmmse': color_advmmse(parameters.totalmmse), 'gijon': color_advgijon(parameters.gijon), 'clock': color_advclock(parameters.clock), 'globalsppb': color_advglobalsppb(parameters.globalsppb), 'frailtycfs': color_advfrailtycfs(parameters.frailtycfs), 'higheststrong': color_advhigheststrong(parameters.higheststrong), 'gds': color_advgds(parameters.gds), 'lwb': color_advlwb(parameters.lwb)}
    return render(request, "real/dash.html", {'parameters': parameters, 'dic_parameters': dic_parameters, 'color_adv': dic_color, 'extension': extension})


