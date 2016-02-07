API Crawler
=============
This project crawls [APIs.guru](https://apis-guru.github.io/api-models/) for the API name, description, url, and provider name for the listed APIs.

To see the crawler's output, git clone this repo, then:

```
cd apicrawler
mkvirtualenv apicrawler
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

and navigate to localhost:8000/server in your browser.
