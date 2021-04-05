from django.shortcuts import render, redirect

from calculator.models import User


def main(request):
    return render(request, 'calculator/main.html', {})


def create(request):
    if (request.method == 'POST'):
        user = User()
        # request로 받은 값을 저장하는 내용을 적어주세요.
    return redirect('calculator:calculator')


def calculator(request):
    # users의 모든 내용을 가져오는 query를 적어주세요.
    return render(request, 'calculator/mycalculator.html', {'users': users})
