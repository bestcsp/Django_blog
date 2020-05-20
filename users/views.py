from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,ProfileUpdateForm,UserUpdateForm
from blog.models import Post

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"acccount is created of {username}")
            return redirect('home')
    
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})
    
@login_required
def profile(request):
    if request.method=='POST':
        
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            print(u_form.errors)
            u_form.save()
            p_form.save()
            messages.success(request,f"profile is updated ")
            return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form,'p_form':p_form}
    
    return render(request,'users/profile.html',context)

def HandleSearch(request):
    # posts=Post.objects.all()
    query=request.GET['search']
    if len(query)>80:
        posts=Post.objects.none()
    else:
        postsTitle=Post.objects.filter(title__icontains=query)
        postsContent=Post.objects.filter(content__icontains=query)
        posts=postsTitle.union(postsContent)
        context={'posts':posts,'query':query}
    if posts.count()==0:
        messages.warning(request,"Search wisely")
    return render(request,'blog/search.html',context)


