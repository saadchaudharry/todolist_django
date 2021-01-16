from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Tasks
from .form import Task_form
# Create your views here
@login_required
def index(request):
    obj=Tasks.objects.exclude(status='done').all().order_by('-complete_date')
    form =Task_form
    paginator = Paginator(obj, 8)
    page_name = request.GET.get('page', 1)
    try:
        page = paginator.page(page_name)
    except EmptyPage:
        page = paginator.page(1)
    context={'object':page,'form':form}
    return render(request,'index.html',context)

@login_required
def Impo(request):
    obj=Tasks.objects.filter(status='important').all().order_by('-complete_date')
    form =Task_form
    paginator = Paginator(obj, 8)
    page_name = request.GET.get('page', 1)
    try:
        page = paginator.page(page_name)
    except EmptyPage:
        page = paginator.page(1)
    context={'object':page,'form':form}
    return render(request,'index.html',context)

@login_required
def regull(request):
    obj=Tasks.objects.filter(status='regular').all().order_by('-complete_date')
    form =Task_form
    paginator = Paginator(obj, 8)
    page_name = request.GET.get('page', 1)
    try:
        page = paginator.page(page_name)
    except EmptyPage:
        page = paginator.page(1)
    context={'object':page,'form':form}
    return render(request,'index.html',context)

@login_required
def doon(request):
    obj=Tasks.objects.filter(status='done').all().order_by('-complete_date')
    form =Task_form
    paginator = Paginator(obj, 8)
    page_name = request.GET.get('page', 1)
    try:
        page = paginator.page(page_name)
    except EmptyPage:
        page = paginator.page(1)
    context={'object':page,'form':form}
    return render(request,'index.html',context)

@login_required
def date__get(request):
    getdate=request.POST.get('qq')
    obj=Tasks.objects.filter(complete_date=getdate).all().order_by('-complete_date')
    form =Task_form
    paginator = Paginator(obj, 8)
    page_name = request.GET.get('page', 1)
    try:
        page = paginator.page(page_name)
    except EmptyPage:
        page = paginator.page(1)
    context={'object':page,'form':form}
    return render(request,'index.html',context)



@login_required
def done_valiadereraaa(request):
    client_query = request.POST.get('qq')
    obj=Tasks.objects.get(id=client_query)
    obj.status = 'done'
    obj.save()

    return redirect('index')

@login_required
def order_valiadereraaa(request):
    form=Task_form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return redirect('index')
