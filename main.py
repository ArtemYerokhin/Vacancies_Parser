from headhunter import get_jobs as get_hh_jobs
from habr import get_jobs as get_habr_jobs
import csv


if __name__ == '__main__':
    hh_jobs = get_hh_jobs()
    habr_jobs = get_habr_jobs()
    jobs = hh_jobs + habr_jobs

    file = open('vacancies.csv', mode='w', encoding='utf-8-sig', newline='',)
    writer = csv.writer(file, delimiter =';')
    writer.writerow(['Заголовок', 'Компания', 'Информация', 'Ссылка'])
    for job in jobs:
        writer.writerow(list(job.values()))
    file.close()
    print('Файл vacancies.csv успешно записан')