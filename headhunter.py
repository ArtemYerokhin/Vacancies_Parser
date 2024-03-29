import requests
from bs4 import BeautifulSoup


ITEMS = 100  # количество вакансий на странице
TEXT = 'Data Scientist'  # текст запроса
URL = f'https://hh.ru/search/vacancy?text={TEXT}&order_by=relevance&L_save_area=true&items_on_page={ITEMS}'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def extract_last_page():
  hh_request = requests.get(URL, headers=headers)
  hh_soup = BeautifulSoup(hh_request.text, 'lxml')
  pages = []
  # переключатель страниц
  paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

  for page in paginator:
    pages.append(int(page.find('a').text))
  # последняя страница
  return pages[-1]


def extract_job(html):
  title = html.find('a').text
  link = html.find('a')['href']
  company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).find('a').text
  company = company.replace(u'\xa0', u' ')
  location = html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
  location = location.partition(',')[0]
  return {'Заголовок': title, 'Компания': company, 'Расположение': location, 'Ссылка': link}


def extract_hh_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print('Парсинг hh.ru, страница:', page+1)
    result = requests.get(f'{URL}&page={page}', headers=headers)
    soup = BeautifulSoup(result.text, 'lxml')
    results = soup.find_all('div', {'class': 'serp-item'})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = extract_last_page()
  jobs = extract_hh_jobs(last_page)
  return jobs
