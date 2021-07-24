from business.forms import NeighbourhoodForm
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse ,Http404 
from .models import  Neighbourhood ,User , Business
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_neighbourhood(request):
    jirani = Neighbourhood.objects.all()
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST , request.FILES)
        if form.is_valid():
            nform = form.save()
            nform.user= request.user
            nform.save()
            return redirect('homepage')

