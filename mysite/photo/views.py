from django.shortcuts import render, redirect
from .models import Photo, Comment

# Create your views here.
def list(request):
    photos = Photo.objects.all()

    return render(request, "photo/list.html", {"photos":photos})

def create(request):
    if(request.method == "POST"):
        # POST방식으로 들어왔을 때
        # 데이터를 저장
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        Photo.objects.create(title=title, content=content, image=image)

        return redirect("photos:list")
    else:
        # GET방식으로 들어왔을 때
        # 입력할 수 있게 폼을 제공
        return render(request, "photo/create.html")

def detail(request, id):
    photo = Photo.objects.get(pk=id)

    return render(request, "photo/detail.html", {"photo":photo})

def update(request,id):
    if(request.method == "POST"):
        photo = Photo.objects.get(pk=id)
    
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        photo.title = title
        photo.content = content
        photo.save()
        
        return redirect("photos:detail", photo.id)
    
    else:
        photo = Photo.objects.get(id=id)
        return render(request, "photo/update.html", {"photo":photo} )
    
def delete(request, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect("photos:list")
    
def comment(request, id):
    photo = Photo.objects.get(pk=id)
    content = request.POST.get("content")

    Comment.objects.create(photo=photo, content=content)

    return redirect("photos:detail", photo.id)