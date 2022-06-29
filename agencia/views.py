from django.http import HttpResponse
from django.shortcuts import render, redirect


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from agencia.forms import User_registration
# Create your views here.


def bienvenida(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'bienvenida.html')


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message': f'Bienvenido {username}!'}
                return render(request, 'bienvenida.html', context=context)
            else:
                context = {
                    'errors': f'No existe usuario con esas credenciales'}
                form = AuthenticationForm()
                return render(request, 'login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors': errors, 'form': form}
            return render(request, 'login.html', context=context)

    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('Bienvenida')


def register_view(request):
    if request.method == 'POST':
        form = User_registration(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            context = {
                'message': f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'bienvenida.html', context=context)
        else:
            errors = form.errors
            form = User_registration()
            context = {'errors': errors, 'form': form}
            return render(request, 'register.html', context=context)
    else:
        form = User_registration()
        context = {'form': form}
        return render(request, 'register.html', context=context)
