import csv

def save_to_csv(jobs):
  file = open('vacancies.csv', mode='w')
  writer = csv.writer(file)
  writer.writerow(['Заголовок', 'Компания', 'Информация', 'Ссылка'])
  for job in jobs:
    writer.writerow(list(job.values()))
  return
