from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response, views, status

#-------------HOMEPAGE-------------#


def index_page(request):

    return render(request, "pages/homepage/index.html", {})



#-------------DASHBOARD-------------#

def dashboard_page(request):
    return render(request, "pages/dashboard/dashboard.html", {
        'user': request.user,
    })


#-------------GATEWAY-------------#

def register_page(request):

    return render(request, "pages/gateway/register.html", {})


def register_success_page(request):

    return render(request, "pages/gateway/register_success.html", {})


def login_page(request):

    return render(request, "pages/gateway/login.html", {})

def logout_page(request):

    return render(request, "pages/gateway/logout.html", {})


def post_logout_api(request):
    try:
        logout(request)
        return JsonResponse({
             "was_logged_out": True,
             "reason": None,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
             "was_logged_out": False,
             "reason": str(e),
        })
