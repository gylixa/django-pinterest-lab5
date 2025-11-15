# site_1/views.py
from django.shortcuts import render

def index_page(request):
    projects = [
        {
            'name': 'Солнечный Город',
            'image': 'images/1.png',  
            'address': {'Город': 'Москва', 'Улица': 'Солнечная', 'Дом': '15'},
            'characteristics': ['Экологичный', 'Современный', 'Семейный'],
            'type': 'Жилой комплекс',
        },
        {
            'name': 'Небесная Гавань',
            'image': 'images/2.png',
            'address': {'Город': 'Санкт-Петербург', 'Улица': 'Набережная', 'Дом': '22'},
            'characteristics': ['Роскошный', 'Вид на море', 'Инновационный'],
            'type': 'Апартаменты',
        },
        {
            'name': 'Тихий Лес',
            'image': 'images/3.png',
            'address': {'Город': 'Казань', 'Улица': 'Лесная', 'Дом': '7'},
            'characteristics': ['Уютный', 'Природный', 'Спокойный'],
            'type': 'Коттеджный поселок',
        },
    ]
    return render(request, 'index.html', {'projects': projects})

def home_page(request):
    projects = [
        {'name': 'Проект дома А52', 'area': 52.02, 'price': 'от 2 900 000'},
        {'name': 'Проект дома Б102', 'area': 101.41, 'price': 'от 5 610 000'},
        {'name': 'Проект В200', 'area': 200.8, 'price': 'от 11 000 000'},
    ]
    return render(request, 'home.html', {'projects': projects})