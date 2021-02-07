from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import tours
from random import choice


def mainview(request):
    random_tour_1 = []
    i = 0
    while i < 6:
        a = choice(list(tours.values()))
        if a not in random_tour_1:
            random_tour_1.append(a)
            i += 1

    context = {
        "random_tour_1": random_tour_1
    }
    return render(request, 'index.html', context=context)


def departureview(request, departure):
    sort_tours = []
    naprav = str()
    if departure == 'nsk':
        naprav = 'Новосибирска'
    elif departure == 'ekb':
        naprav = 'Екатеренбурга'
    elif departure == 'msk':
        naprav = 'Москвы'
    elif departure == 'spb':
        naprav = 'Петербурга'
    elif departure == 'kazan':
        naprav = 'Казани'

    for tour in tours.keys():
        a = tours.get(tour)
        if a['departure'] == departure:
            sort_tours.append(a)
    col = len(sort_tours)

    min_price = sort_tours[1].get('price')
    for tour in sort_tours:
        if tour.get('price') < min_price:
            min_price = tour.get('price')
    max_price = sort_tours[1].get('price')
    for tour in sort_tours:
        if tour.get('price') > max_price:
            max_price = tour.get('price')
    min_nights = sort_tours[1].get('nights')
    for tour in sort_tours:
        if tour.get('nights') < min_nights:
            min_nights = tour.get('nights')
    max_nights = sort_tours[1].get('nights')
    for tour in sort_tours:
        if tour.get('nights') > max_nights:
            max_nights = tour.get('nights')

    context = {
        "sort_tours": sort_tours,
        "naprav": naprav,
        "col": col,
        "min_price": min_price,
        "max_price": max_price,
        "min_nights": min_nights,
        "max_nights": max_nights,
    }
    return render(request, 'departure.html', context=context)


def tourview(request, tour):
    tour = tours.get(tour)
    if not tour:
        return HttpResponseNotFound("Такого тура нет")

    context = {
        "tour": tour
    }
    return render(request, 'tour.html', context=context)
