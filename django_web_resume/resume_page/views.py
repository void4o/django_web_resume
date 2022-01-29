from django.shortcuts import render


def show_title(req):
    return render(req, 'main.html')


def show_weapons(req):
    return render(req, 'weapons_page.html')
