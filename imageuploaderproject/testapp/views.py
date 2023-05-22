from django.shortcuts import render
from .models import Image
from .forms import ImageForm
# Create your views here.

def home_page_view(request):
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    img = Image.objects.all()
    return render(request, 'testapp/home.html', {'form':form, 'img':img})
