## Урок 8. Сериализация

### Задачи:

Задание №4

* Прочитайте созданный в прошлом задании csv файл без
  использования csv.DictReader.
* Дополните id до 10 цифр незначащими нулями.
* В именах первую букву сделайте прописной.
* Добавьте поле хеш на основе имени и идентификатора.
* Получившиеся записи сохраните в json файл, где каждая строка
  csv файла представлена как отдельный json словарь.
* Имя исходного и конечного файлов передавайте как аргументы
  функции.

Задание №5

* Напишите функцию, которая ищет json файлы в указанной директории и сохраняет
  их содержимое в виде одноимённых pickle файлов.

Задание №6

* Напишите функцию, которая преобразует pickle файл
  хранящий список словарей в табличный csv файл.
* Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
* Функция должна извлекать ключи словаря для заголовков
  столбца из переданного файла.

Задание №7

* Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
* Распечатайте его как pickle строку.

_Домашнее задание:_

Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.

* Для дочерних объектов указывайте родительскую директорию.
* Для каждого объекта укажите файл это или директория.
* Для файлов сохраните его размер в байтах, а для директорий размер
  файлов в ней с учётом всех вложенных файлов и директорий.
* Соберите из созданных на уроке и в рамках домашнего задания функций
  пакет для работы с файлами разных форматов.
