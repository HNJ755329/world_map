from django.shortcuts import render

# Create your views here.

# Create your views here.
def maps_index(request):
    prop = request.GET.get(key="prop", default="GDP")
    #posts = Post.objects.all()
    context = {
        "prop": prop,
    }
    return render(request, "maps_index.html", context)

def maps_full(request):
    prop = request.GET.get(key="prop", default="GDP")
    color = request.GET.get(key="color", default="Red")
    year = request.GET.get(key="year", default="2019")
    #posts = Post.objects.all()
    context = {
        "prop": prop,
        "color": color,
        "year": year,
    }
    return render(request, "maps_full.html", context)