from pprint import pprint

from config import request_web_site, url_web_site, config
from support import write_json_catalog, write_json_book, check_tag

html = request_web_site(url_web_site, config)


def get_data_catalog(html_site):
    content_catalog = []
    main_block = html_site.find('div', class_='AllGenres_genres-container__59GUx')
    sub_block = main_block.find_all('div', class_='Column_column__LjrSZ')
    for item in sub_block[:10]:
        title_catalog = item.find('a', class_='Column_title__M1cS5').get_text(strip=True)
        link_catalog = 'https://www.litres.ru' + item.find('a', class_='Column_title__M1cS5')['href']
        content_catalog.append({
            'title': title_catalog,
            'link': link_catalog
        })
    return content_catalog


# data_catalog = get_data_catalog(html)


def get_data_books(obj):
    content_books = []
    name, link = obj
    html_code = request_web_site(link, config)
    main_block = html_code.find('div', class_='ArtsGrid_artsGrid__rA8I8 ArtsGrid_artsGrid__adaptive__308LV')
    blocks = main_block.find_all('div', class_='ArtsGrid_artWrapper__LXa0O')
    for item in blocks:
        try:
            title = check_tag(item.find('p', class_='ArtInfo_title__h_5Ay'))
            img_link = item.find('img', class_='AdaptiveCover_image__eAZyi')['src']
            author = check_tag(item.find('a', class_='ArtInfo_author__0W3GJ'))
            price_bad = check_tag(item.find('strong', class_='ArtPriceFooter_ArtPriceFooterPrices__final__7AMjB'))
            estimation = check_tag(item.find('div', class_='ArtRating_rating__ntve8'))
            estimation_quantity = check_tag(item.find('div', class_='ArtRating_votes__MIJS1'))  # .replace(',', '.')
            type_book = item.find('img', class_='Label_icon__NDQ19')['title']
            price = ''.join(list(filter(lambda i: i.isdigit(), price_bad)))
            link_detail = 'https://www.litres.ru' + item.find('a')['href']
            content_books.append({
                name: {
                    'title': title,
                    'img_link': img_link,
                    'author': author,
                    'price': price,
                    'estimation': estimation,
                    'estimation_quantity': estimation_quantity,
                    'type_book': type_book,
                    'link_detail': link_detail
                }
            })
        except Exception as error:
            print(error)

    return content_books


def start_func_get_data_books(obj):
    data = []
    for item in obj:
        send = [item['title'], item['link']]
        data.append(get_data_books(send))

    good_data = []
    for item in data:
        for dict_element in [a for a in item]:
            good_data.append(dict_element)

    return good_data


# data_books = start_func_get_data_books(data_catalog)
#
# write_json_catalog(data_catalog)
# write_json_book(data_books)

