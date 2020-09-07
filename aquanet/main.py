import requests
from bs4 import BeautifulSoup
import csv
from mixin.page_data_mixin import PageDataMixin

""" Header of csv file """
with open('aquanet_2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Код', 'Артикул', 'Бренд', 'Коллекция', 'Установка', 'Ширина', 'Высота',
                     'Глубина', 'Материал', 'Дизайн', 'Цвет', 'Миксер', 'Гибкая подводка', 'Режимы', 'Радиус',
                     'Термостат', 'Размер верхнего душа', 'Вес', 'Режимы верхнего душа'])


""" Headers by client request """
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
           "Connection": "keep-alive",
           "Cookie": "roistat_is_need_listen_requests=0; PHPSESSID=dkqigsqjnpog23oi06ve8e78cn; BITRIX_SM_SALE_UID=53262055; activity=0|20; _gcl_au=1.1.1930093311.1581921401; BITRIX_SM_VREGION_SUBDOMAIN=spb; BITRIX_SM_VREGION_SUBDOMAIN=spb; roistat_visit=778381; roistat_first_visit=778381; roistat_marker_old=; _ga=GA1.2.550948518.1581921402; _gid=GA1.2.680255184.1581921402; tmr_reqNum=5; tmr_lvid=76a44c8277ca4aa4a4b803049f61ad74; tmr_lvidTS=1581921402025; _ym_uid=1581921402466203911; _ym_d=1581921402; leadhunter_expire=1; _gat=1; _ym_visorc_23245510=w; _ym_isad=2; _fbp=fb.1.1581921402948.1181980815; ___dc=c8ad68ce-ab99-43f6-9729-12c2fe7a6b8b; tmr_detect=0%7C1581921404947; BX_USER_ID=0662459c6c9a798caa9c90b46efe2528; _gat_UA-44466602-1=1",
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
    with open('aquanet_2.csv', 'a') as f:
        writer = csv.writer(f)
        # Нет шапки, для значений
        writer.writerow([data['uls_code'],
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
                         data['radius_l'],
                         data['termo'],
                         data['size_top'],
                         data['weigth'],
                         data['watering_mode_top']])


def get_page_data(response):
    """ Method of parse data """
    soup = BeautifulSoup(response, 'lxml')
    divs = soup.find_all('div', class_='item')

    urls = []

    for div in divs:
        """ First page """
        name = div.select_one('p').get('title')
        url = div.select_one('a').get('href')
        urls.append('https://www.aquanet.ru' + url)
        price = div.select_one('div.price').text

    for url in urls:
        """ 
            Page of each products
            Request & pars param's 
        """
        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        
        uls_code = PageDataMixin(soup.select_one, 'ul.item_props', 'li', {'data-id': '470'}, 'p').find_paragraph()
        print(uls_code)
        art = PageDataMixin(soup.select_one, 'ul.item_props', 'li', {'data-id': '125'}, 'p').find_paragraph()
        print(art)

        try:
            brand = soup.select_one('ul.item_props').find('li', attrs={'data-id': '126'}).find('a').text
        except:
            brand = 'empty'
        try:
            collections = soup.select_one('ul.item_props').find('li', attrs={'data-id': '226'}).find('a').text
        except:
            collections = 'empty'
        try:
            install = soup.select_one('ul.item_props').find('li', attrs={'data-id': '137'}).find('p').find_next('p').text
        except:
            install = 'empty'
        try:
            width = soup.select_one('ul.item_props').find('li', attrs={'data-id': '132'}).find('p').find_next('p').text
        except:
            width = 'empty'
        try:
            height = soup.select_one('ul.item_props').find('li', attrs={'data-id': '133'}).find('p').find_next('p').text
        except:
            height = 'empty'
        try:
            depth = soup.select_one('ul.item_props').find('li', attrs={'data-id': '134'}).find('p').find_next('p').text
        except:
            depth = 'empty'
        try:
            material = soup.select_one('ul.item_props').find('li', attrs={'data-id': '127'}).find('p').find_next('p').text
        except:
            material = 'empty'
        try:
            design = soup.select_one('ul.item_props').find('li', attrs={'data-id': '148'}).find('p').find_next('p').text
        except:
            design = 'empty'
        try:
            color = soup.select_one('ul.item_props').find('li', attrs={'data-id': '128'}).find('p').find_next('p').text
        except:
            color = 'empty'
        try:
            mixer = soup.select_one('ul.item_props').find('li', attrs={'data-id': '298'}).find('p').find_next('p').text
        except:
            mixer = 'empty'
        try:
            flexible_connection = soup.select_one('ul.item_props').find('li', attrs={'data-id': '283'}).find('p').find_next('p').text
        except:
            flexible_connection = 'empty'
        try:
            watering_mode = soup.select_one('ul.item_props').find('li', attrs={'data-id': '303'}).find('p').find_next('p').text
        except:
            watering_mode = 'empty'
        try:
            radius_l = soup.select_one('ul.item_props').find('li', attrs={'data-id': '306'}).find('p').find_next('p').text
        except:
            radius_l = 'empty'
        try:
            termo = soup.select_one('ul.item_props').find('li', attrs={'data-id': '155'}).find('p').find_next('p').text
        except:
            termo = 'empty'
        try:
            size_top = soup.select_one('ul.item_props').find('li', attrs={'data-id': '562'}).find('p').find_next('p').text
        except:
            size_top = 'empty'
        try:
            weigth = soup.select_one('ul.item_props').find('li', attrs={'data-id': '589'}).find('p').find_next('p').text
        except:
            weigth = 'empty'
        try:
            watering_mode_top = soup.select_one('ul.item_props').find('li', attrs={'data-id': '303'}).find('p').find_next('p').text
        except:
            watering_mode_top = 'empty'

        data = {'uls_code': uls_code.strip(),
                'art': art.strip(),
                'brand': brand.strip(),
                'collections': collections.strip(),
                'install': install.strip(),
                'width': width.strip(),
                'height': height.strip(),
                'depth': depth.strip(),
                'material': material.strip(),
                'design': design.strip(),
                'color': color.strip(),
                'mixer': mixer.strip(),
                'flexible_connection': flexible_connection.strip(),
                'watering_mode': watering_mode.strip(),
                'radius_l': radius_l.strip(),
                'termo': termo.strip(),
                'size_top': size_top.strip(),
                'weigth': weigth.strip(),
                'watering_mode_top': watering_mode_top.strip()}
        write_csv(data)


def main():
    pattern = 'https://www.aquanet.ru/catalog/verkhnie_dushi/?PAGEN_1={}'

    for i in range(1, 16):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()