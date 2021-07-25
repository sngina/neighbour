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
            nform = form.save(commit=False)
            nform.user= request.user
            nform.save()
            return redirect('homepage')
    form = NeighbourhoodForm()

    return render(request , 'profile/index.html' ,{"jirani":jirani , "form":form})

#function for searching 
def search(request):

    if 'business' in request.Get and request.GET["business"]:
        search_term = request.GET.get("business")
        search_business = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request , 'profile/search.html' , {"message":message ,"search_profile":search_business})

    else:
        message = "No Business searched yet!"
        return render(request , 'profile/search.html')
def userpage(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request,"profile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })
