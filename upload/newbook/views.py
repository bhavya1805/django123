from django.shortcuts import render
from newbook.forms import bookform
from newbook.models import Book,CustomUser,order
from newbook.forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    return render(request,'home.html')
@login_required()
def upload(request):
    form=bookform()
    if(request.method=="POST"):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'upload.html',{'form':form})
@login_required()
def booklist(request):
    b=Book.objects.all()

    return render(request,'list.html',{'b':b})
@login_required()
def delete_book(request,p):
    b=Book.objects.get(pk=p)
    b.delete()
    return booklist(request)
@login_required()
def view_book(request,p):
    b=Book.objects.get(pk=p)
    return render(request,'book.html',{'b':b})
@login_required()
def edit_book(request,p):
    b=Book.objects.get(pk=p)
    form = bookform(instance=b)
    if (request.method == "POST"):
        form = bookform(request.POST,request.FILES,instance=b)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request, 'upload.html', {'form': form})

def signup(request):
    form=CustomUserCreationForm()     #Empty form Object
    if(request.method=="POST"):
        form=CustomUserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'signup.html',{'form':form})

def user_login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            request.session['user']=user.username
            return home(request)
        else:
            return HttpResponse("Invalid login details")
    return render(request,'login.html')
@login_required()
def user_logout(request):
    logout(request)
    return user_login(request)
@login_required()
def order_book(request,p):
    b=Book.objects.get(pk=p)
    p=request.session['user']
    u=CustomUser.objects.get(username=p)
    o=order(name=u.username,phno=u.phone,location=u.address,title=b.title,author=b.author)
    o.save()
    return order_status(request)

def order_status(request):
    return render(request,"status.html")
@login_required()
def search(request):
    if(request.method=="POST"):
        srch=request.POST['srh']
        if srch:
            match=Book.objects.filter(Q(title__icontains=srch)|Q(author__icontains=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                return search(request)
        else:
            messages.error(request, "NO results Found")
    return render(request,'search.html')