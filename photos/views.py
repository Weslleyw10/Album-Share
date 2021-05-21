from django.shortcuts import render, redirect
from .models import *

from slugify import slugify

# Create your views here.
def gallery(request):
    categories = Category.objects.all()

    category = request.GET.get('category')

    if category == None:        
        photos = Photo.objects.all()    
    else:
        photos = Photo.objects.filter(category__slug=category)
    


    context = {
        "categories": categories,
        "photos": photos
    }

    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(slug=pk)
    context = {"photo": photo}

    return render(request, 'photos/photo.html', context)

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        files = request.FILES.get('image')

        category = data['category']
        category_new = data['category_new']
        slug = slugify(data['name'], to_lower=True)

        print('slug', slug)

        print('data', data)
        print('files', files)

        if category != 'none':
            category = Category.objects.get(id=category)
        
        elif category_new != '':
            slug = slugify(category_new, to_lower=True)
            category, created = Category.objects.get_or_create(
                name=category_new,
                slug = slug
            )

        else:
            category = None


        photo = Photo.objects.create(
            category=category,
            name = data['name'],
            slug = slug,
            description=data['description'],
            image=files
        )

        return redirect('gallery')


    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

