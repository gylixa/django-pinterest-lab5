# site_1/views.py
from django.shortcuts import render
import os
from django.conf import settings

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

def read_file_page(request):
    filename = ''
    content = ''
    error = ''

    if request.method == 'POST':
        filename = request.POST.get('filename', '').strip()

        if not filename:
            error = 'Имя файла не может быть пустым.'
        else:
            # Ограничиваем чтение только определённой папкой, например — media или files
            # Создайте папку `files` в корне проекта: test_1/files/
            file_path = os.path.join(settings.BASE_DIR, 'files', filename)

            # Защита от path traversal (.., /, \ и т.д.)
            if '..' in filename or filename.startswith('/') or filename.startswith('\\'):
                error = 'Недопустимое имя файла.'
            elif not os.path.isfile(file_path):
                error = f'Файл "{filename}" не найден в папке "files".'
            else:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    error = 'Ошибка: файл не является текстовым (неподдерживаемая кодировка).'
                except Exception as e:
                    error = f'Ошибка при чтении файла: {e}'

    return render(request, 'read_file.html', {
        'filename': filename,
        'content': content,
        'error': error
    })