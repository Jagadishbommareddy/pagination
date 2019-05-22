from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator
# # Create your views here.
#
# user_list = User.objects.all()
# paginator = Paginator(user_list, 10)
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from .serializers import *
from django.http import HttpResponse, JsonResponse
from .pagination import *
from django.views.decorators.csrf import csrf_exempt
# def index(request):
#     user_list = User.objects.all()
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(user_list, 5)
#     print (paginator)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)
#
#     return render(request, 'user_list.html', { 'users': users })
@csrf_exempt
def index(request):
    #data = json.loads(request.body.decode('utf-8'))
    #offset, limit = get_offset(data)
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    user = UserSerilaizer(users,many=True)
    return JsonResponse({"response": user.data, "status": "success"})