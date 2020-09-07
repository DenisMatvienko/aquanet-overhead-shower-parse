import requests
from bs4 import BeautifulSoup
import csv
from mixin.page_data_mixin import PageDataMixin, MainPageData

""" Header of csv file outside iteration"""
with open('aquanet.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Наименование', 'Код', 'Артикул', 'Бренд', 'Коллекция', 'Установка', 'Ширина', 'Высота',
                     'Глубина', 'Материал', 'Дизайн', 'Цвет', 'Миксер', 'Гибкая подводка', 'Режимы', 'Радиус',
                     'Термостат', 'Размер верхнего душа', 'Вес', 'Режимы верхнего душа', 'URL'])


""" Headers by client request """
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
           "Connection": "keep-alive",
           "Cookie": "roistat_is_need_listen_requests=0; PHPSESSID=dkqigsqjnpog23oi06ve8e78cn;"
                     "BITRIX_SM_SALE_UID=53262055; activity=0|20; _gcl_au=1.1.1930093311.1581921401;"
                     " BITRIX_SM_VREGION_SUBDOMAIN=spb; BITRIX_SM_VREGION_SUBDOMAIN=spb; roistat_visit=778381;"
                     " roistat_first_visit=778381; roistat_marker_old=; _ga=GA1.2.550948518.1581921402;"
                     " _gid=GA1.2.680255184.1581921402; tmr_reqNum=5; tmr_lvid=76a44c8277ca4aa4a4b803049f61ad74;"
                     " tmr_lvidTS=1581921402025; _ym_uid=1581921402466203911; _ym_d=1581921402; leadhunter_expire=1;"
                     " _gat=1; _ym_visorc_23245510=w; _ym_isad=2; _fbp=fb.1.1581921402948.1181980815; "
                     "___dc=c8ad68ce-ab99-43f6-9729-12c2fe7a6b8b; tmr_detect=0%7C1581921404947;"
                     " BX_USER_ID=0662459c6c9a798caa9c90b46efe2528; _gat_UA-44466602-1=1",
           "Host": "www.aquanet.ru",
           "Referer": "https://www.aquanet.ru/catalog/verkhnie_dushi/",
           "TE": "Trailers",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}


def get_html(url):
    """ Get method of request on site """
    r = requests.get(url, headers=headers)
    return r.text


def write_csv(data):
    """ Write data after pars """
    with open('aquanet.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['uls_code'],
                         data['art'],
                         data['brand'],
                         data['collections'],
                         data['install'],
                         data['width'],
                         data['height'],
                         data['depth'],
                         data['material'],
                         data['design'],
                         data['color'],
                         data['mixer'],
                         data['flexible_connection'],
                         data['watering_mode'],
                         data['radius'],
                         data['termo'],
                         data['size_top'],
                         data['weigth'],
                         data['watering_mode_top'],
                         data['url']])


def get_page_data(response):
    """ Method of parse data """
    soup = BeautifulSoup(response, 'lxml')
    divs = soup.find_all('div', class_='item')

    urls = []

    for div in divs:
        """ First page """
        url = MainPageData(div.select_one, 'a', 'href').find_main_page_data()
        urls.append('https://www.aquanet.ru' + url)

    for url in urls:
        """ 
            Page of each products
            Request & pars param's
            Use PageDataMixin, for created short entry of exceptions
            Use methods find_paragraph & find_links, for different param's of search text on page
        """
        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')

        """ Get properties from each pages """
        name = soup.find('div', id='content').select_one('h1').text.strip()
        uls_code = PageDataMixin(soup.select_one, {'data-id': '470'}).find_paragraph()
        art = PageDataMixin(soup.select_one, {'data-id': '125'}).find_paragraph()
        brand = PageDataMixin(soup.select_one, {'data-id': '126'}).find_links()
        collections = PageDataMixin(soup.select_one, {'data-id': '226'}).find_links()
        install = PageDataMixin(soup.select_one, {'data-id': '137'}).find_paragraph()
        width = PageDataMixin(soup.select_one, {'data-id': '132'}).find_paragraph()
        height = PageDataMixin(soup.select_one, {'data-id': '133'}).find_paragraph()
        depth = PageDataMixin(soup.select_one, {'data-id': '134'}).find_paragraph()
        material = PageDataMixin(soup.select_one, {'data-id': '127'}).find_paragraph()
        design = PageDataMixin(soup.select_one, {'data-id': '148'}).find_paragraph()
        color = PageDataMixin(soup.select_one, {'data-id': '128'}).find_paragraph()
        mixer = PageDataMixin(soup.select_one, {'data-id': '298'}).find_paragraph()
        flexible_connection = PageDataMixin(soup.select_one, {'data-id': '283'}).find_paragraph()
        watering_mode = PageDataMixin(soup.select_one, {'data-id': '303'}).find_paragraph()
        radius = PageDataMixin(soup.select_one, {'data-id': '306'}).find_paragraph()
        termo = PageDataMixin(soup.select_one, {'data-id': '155'}).find_paragraph()
        size_top = PageDataMixin(soup.select_one, {'data-id': '562'}).find_paragraph()
        weigth = PageDataMixin(soup.select_one, {'data-id': '589'}).find_paragraph()
        watering_mode_top = PageDataMixin(soup.select_one, {'data-id': '303'}).find_paragraph()

        # Write data to dict and get to the write csv func
        data = {'name': name,
                'uls_code': uls_code,
                'art': art,
                'brand': brand,
                'collections': collections,
                'install': install,
                'width': width,
                'height': height,
                'depth': depth,
                'material': material,
                'design': design,
                'color': color,
                'mixer': mixer,
                'flexible_connection': flexible_connection,
                'watering_mode': watering_mode,
                'radius': radius,
                'termo': termo,
                'size_top': size_top,
                'weigth': weigth,
                'watering_mode_top': watering_mode_top,
                'url': url}
        write_csv(data)


def main():
    pattern = 'https://www.aquanet.ru/catalog/verkhnie_dushi/?PAGEN_1={}'

    for i in range(1, 16):
        """ Loop requests to get response data from page on 15 pages   """
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()