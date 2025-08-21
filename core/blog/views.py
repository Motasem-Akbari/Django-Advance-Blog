from django.shortcuts import render

# Create your views here.


def indexView(request):
    name = "Motasem"
    context = {"name": name}
    return render(request, "index.html", context)