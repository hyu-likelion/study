from django.shortcuts import render, redirect

from calculator.models import User


def main(request):
    return render(request, 'calculator/main.html', {})


def create(request):
    if (request.method == 'POST'):
        user = User()
        user.name = request.POST['name']
        user.save()
    return redirect('calculator:calculator')


def calculator(request):
    users = User.objects.all()
    return render(request, 'calculator/mycalculator.html', {'users': users})
