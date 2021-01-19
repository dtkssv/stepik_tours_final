from django.shortcuts import render


# Create your views here.
def mainview(request):
    return render(request, 'index.html')


def departureview(request):
    return render(request, 'departure.html')


def tourview(request):
    return render(request, 'tour.html')
