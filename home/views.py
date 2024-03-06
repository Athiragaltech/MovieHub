from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect

from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from . models import movie
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    data ={
        'mov' :movie.objects.all()

    }
    return render(request,'index.html',data)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request,'contact.html')

def contact1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        director = request.POST.get('director')
        screen= request.POST.get('screen')
        img_file = request.FILES.get('img')
        if img_file:
            file_path = f"uploads/{img_file.name}"
            default_storage.save(file_path, ContentFile(img_file.read()))
            query = movie(name=name, director=director,screen=screen,img=file_path)
            query.save()
           
           
            return HttpResponse(f'<script>alert("File Added successfully!"); window.location.href = "/";</script>')

           
        return render(request, 'contact.html')

    return HttpResponse("Method Not Allowed", status=405)

def view(request):
    data ={
        'mov' :movie.objects.all()

    }
    
    return render(request,'view.html',data)
def delete(request,id):
    dlt=movie.objects.get(id=id)
    dlt.delete()
    return HttpResponse(f'<script>alert("File Deleted successfully!"); window.location.href = "/";</script>')
         
    return render(request, 'index.html')
def edit(request,id):
    data={
        "data":movie.objects.get(id=id)
        }
    return render(request,'edit.html',data)





def update(request,id):

    if request.method=="POST":
        name=request.POST.get('name')
        director=request.POST.get('director')
        screen=request.POST.get('screen')
        img_file = request.FILES.get('img')
        edit = movie.objects.get(id=id)
        if edit.img:
            default_storage.delete(edit.img.name)
        if img_file:
            file_path = f"uploads/{img_file.name}"
            default_storage.save(file_path, ContentFile(img_file.read()))
        else:
            file_path = None  

        edit.name = name
        edit.director = director
        edit.screen=screen
        edit.img = file_path
               
        edit.save()
        return HttpResponse(f'<script>alert("File Updated successfully!"); window.location.href = "/";</script>')
        return render(request, 'index.html')
    

def continu(request, id):
    # mo = movie.objects.get(id=id)
    data={
        'mov':movie.objects.get(id=id)
    }
    return render(request, 'readmore.html', data)
    

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['uname']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return redirect('index.html')
#         else:
#             # Return an 'invalid login' error message.
#             return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
#     else:
#         return render(request, 'login.html')
    