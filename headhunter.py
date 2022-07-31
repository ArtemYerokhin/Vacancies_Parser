import requests
from bs4 import BeautifulSoup

ITEMS = 100  #vacancies on a page
TEXT = 'Python'  #query text
URL = f'https://hh.ru/search/vacancy?text={TEXT}&order_by=relevance&L_save_area=true&items_on_page={ITEMS}'
headers = {
'Host': 'hh.ru',
'User-Agent': 'Safari',
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive'
}


def extract_last_page():

  hh_request = requests.get(URL, headers=headers)
  
  hh_soup = BeautifulSoup(hh_request.text, 'lxml')
  
  pages = []
  
  #page switcher
  paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

  for page in paginator:
    pages.append(int(page.find('a').text))
  
  #last page
  return pages[-1]

def extract_job(html):
  title = html.find('a').text
  link = html.find('a')['href']
  company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).find('a').text
  company = company.replace(u'\xa0', u' ')
  location = html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
  location = location.partition(',')[0]
  return {'title': title, 'company': company, 'location': location, 'link': link}

def extract_hh_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print('Parsing hh.ru page:', page+1)
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