from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator
# # Create your views here.
#
# user_list = User.objects.all()
# paginator = Paginator(user_list, 10)
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    print (paginator)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'user_list.html', { 'users': users })