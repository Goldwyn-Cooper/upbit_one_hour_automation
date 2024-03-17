# 📌 Upbit 1 Hour Automation
> [UPBIT Flask
](https://github.com/Goldwyn-Cooper/flask_with_gunicorn_in_docker_for_upbit)의 cron job 수행

## 📦 Tech Stack
![Python](https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/githubactions-2088FF.svg?&style=for-the-badge&logo=githubactions&logoColor=white)
![Telegram](https://img.shields.io/badge/telegram-26A5E4.svg?&style=for-the-badge&logo=telegram&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?&style=for-the-badge&logo=pandas&logoColor=white) 

## 🏁 Start
### Install & Test
```shell
$ python3 -m venv venv
$ source venv/bin/activate
# pip install requests python-dotenv pyupbit -q
# pip freeze > requirements.txt
$ pip install -r requirements.txt
# touch .env  # dotenv 혹은 환경변수 설정 필요
$ python tests.py # 단위 테스트
```
### GitHub Secrets for GitHub Actions
> `Settings` > `Security` > `Secrets and variables` > `Actions` > `Secrets` > `New repository secret`

## 📚 Reference
### Unittest
- https://www.daleseo.com/python-unittest-testcase/
- https://docs.python.org/3/library/unittest.html
### Cron Job
- https://crontab.guru/
- https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule