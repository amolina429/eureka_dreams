from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def common_views(request):
    template_name = 'general_data/categories.html'
    return render(request, template_name)