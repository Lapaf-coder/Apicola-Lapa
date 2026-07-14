from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_usuario(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')

    return render(request, 'login.html')


def cerrar_sesion(request):

    logout(request)

    return redirect('login')


@login_required
def dashboard(request):

    datos = {
        "colmenas": 0,
        "produccion": 0,
        "inventario": 0,
        "ventas": 0,
    }

    return render(
        request,
        'dashboard.html',
        datos
    )