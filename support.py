import json


def check_tag(tag):
    if tag is None:
        return ''

    return tag.get_text(strip=True)


def write_json_catalog(obj):
    with open('catalog.json', mode='w', encoding='utf-8') as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)


def write_json_book(obj):
    with open('books.json', mode='w', encoding='utf-8') as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)


def read_json_file(path_file):
    with open(path_file, mode='r', encoding='UTF-8') as file:
        content = json.load(file)
        return content


def check_user_name(obj):
    user_status = obj.split(' ')
    if len(user_status) == 3:
        return 200
    else:
        return 404
