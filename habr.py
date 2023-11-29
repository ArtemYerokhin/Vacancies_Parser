import requests
from bs4 import BeautifulSoup


TEXT = 'Data Scientist'  # текст запроса
URL = f'https://career.habr.com/vacancies?q={TEXT}&type=all'
MAX_PAGE = 5
headers = {
'Host': 'career.habr.com',
'User-Agent': 'Safari',
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive'
}

def extract_job(html):
  title = html.find('div', {'class': 'vacancy-card__title'}).find('a').text
  link = 'https://career.habr.com' + html.find('a')['href']
  company = html.find('div', {'class': 'vacancy-card__company-title'}).find('a').text
  info = html.find('div', {'class': 'vacancy-card__meta'}).text
  return {'Заголовок': title, 'Компания': company, 'Информация': info, 'Ссылка': link}


def extract_habr_jobs(MAX_PAGE):
  jobs = []
  for page in range(1, MAX_PAGE+1):
    print('Парсинг career.habr.com, страница:', page)
    result = requests.get(f'{URL}&page={page}', headers=headers)
    soup = BeautifulSoup(result.text, 'lxml')
    check = soup.find('div', {'class': 'no-content__title'})
    if check == '<div class="no-content__title">Поиск не дал результатов</div>':
      break
    results = soup.find_all('div', {'class': 'vacancy-card__info'})
    for result in results:
      job = extract_job(result)
      jobs.append(job) 
  return jobs
  
  
def get_jobs():
  jobs = extract_habr_jobs(MAX_PAGE)
  return jobs
