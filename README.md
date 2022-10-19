# currency-converter-api
a service that provides currency conversion


.env
DATABASE_URL = link connect DB

CENTRAL_BANK_LINK="http://www.cbr.ru/scripts/XML_daily.asp"

CACHE_RATES_BANK_PATH="../data/cache"


#START

pip install -r requirements.txt

alembic revision -m="initial" --autogenerate

alembic upgrade head

cd ./src

uvicorn app.py --reload
