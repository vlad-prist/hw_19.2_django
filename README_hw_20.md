# Домашняя работа 20.1

# Задание 1.
В файле config/setting.py прописаны настройки для подключения к БД в PostgresQL.
В PostgresQL создана БД "prod_cat"

# Задание 2.
В приложении созданы модели Product, Category.

# Задание 3.
Для каждой модели описаны поля.
А также проведена настройка в файле config/setting.py для MEDIA-файлов.
в config/urls.py добавлено:
"+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"

# Задание 4.
Созданы миграции для действующих моделей.
Также создано изменение в модель класса Product (сейчас закоментировано). 
Для данного изменения создана миграция и потом откачена миграция до состояния 0001_initials.
Сохранена вся история миграций проекта для сохранения целостности базы данных проекта (по заданию).

# Задание 5.
Создана админка
в файле admin.py заполнены настройки для отображения, фильтрации и поиска.

# 6. Shell / Фикстуры 

1. Приложен скрин с командами shell

2. для фикстуры dumpdata применены кодировки:

python -Xutf8 manage.py dumpdata catalog.Category --indent=2 --exclude auth.permission --exclude contenttypes -o category.json

python -Xutf8 manage.py dumpdata catalog.Product --indent=2 --exclude auth.permission --exclude contenttypes -o products.json

Созданные json-файлы с фикстурами помещены в папку catalog/fixtures

3. Создана кастомная команда:
catalog/management/commands/use_command.py
в которой прописаны статик-методы на распаковку json-файлов и добавление данных из них в новый список.
Написан метод handle, в котором приписано удаление существующих данных из таблиц в БД, 
и заполняет БД данными из json-файлов.

# Дополнительное задание.
1. Добавлена выборка последних двух товаров в консоль командой 
print(Product.objects.all().order_by('-created_at')[:2])
(По заданию нужно было вывести последние пять товаров, но у меня только 4 товара)

2. 

