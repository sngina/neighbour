from business.forms import NeighbourhoodForm
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse ,Http404 
from .models import  Neighbourhood ,User , Business
from django.contrib.auth.decorators import login_required
from .forms import NeighbourhoodForm ,UserForm ,BusinessForm , ProfileForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def post_neighbourhood(request):
    jirani = Neighbourhood.objects.all()
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST , request.FILES)
        if form.is_valid():
            nform = form.save()
            nform.user= request.user
            nform.save()
            return redirect('homepage')

    return render(request , 'profile/index.html' ,{"jirani":jirani})

#function for searching 
