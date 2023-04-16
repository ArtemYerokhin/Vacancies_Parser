from headhunter import get_jobs as get_hh_jobs
from habr import get_jobs as get_habr_jobs
from save import save_to_csv


if __name__ == '__main__':
  hh_jobs = get_hh_jobs()
  habr_jobs = get_habr_jobs()
  jobs = hh_jobs + habr_jobs
  save_to_csv(jobs)
