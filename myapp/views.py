from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages
from .models import Profile, Image
from django.db.models import Q


# Create your views here.
def profile(request):
    if request.method == 'POST':
        p_form = ProfileForm(request.POST)
        if p_form.is_valid():
            name = p_form.cleaned_data['name']
            url = p_form.cleaned_data['url']
            phone = p_form.cleaned_data['phone']
            user = Profile(name=name, url=url, phone=phone)
            user.save()
            messages.success(request, f'** User information is saved!')


    p_form = ProfileForm()
    return render(request, 'home.html', {'form': p_form, 'home': 'active'})


def search_user(request):
    return render(request, 'search_user.html', {'search': 'active'})


def search(request):
    template = 'search_user.html'
    result = {}
    query = request.GET.get('q', None)

    if query:
        result = Profile.objects.filter(name__icontains=query)
        if not result:
            messages.error(request, '***No resulting search found***')

    context = {'people': result, 'search': 'active'}
    return render(request, template, context)


def get_image(request):
    return render(request, 'images.html', {'image': 'active'})

def show_image(request):
    image = Image.objects.all()
    return render(request, 'show_image.html', {'images': image, 'image': 'active'})
