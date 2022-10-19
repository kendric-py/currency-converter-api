from lxml import etree
import requests
from core import config as cfg


class ParserXmlRatesBank:
    def __get_currency_rates(self) -> str | None:
        """Получение свежей информации по курсам валют от ЦБ России"""

        response = requests.get(url=cfg.CENTRAL_BANK_LINK)
        return(response.text)

    def __write_new_rates(self, rates_bank: str) -> str:
        """Запись в файл новых курсов валют"""

        with open(file=cfg.CACHE_RATES_BANK_PATH, mode='w') as xml_file:
            return(xml_file.write(rates_bank))

    def __get_raw_data(self) -> list:
        tree: etree.ElementTree = etree.parse(cfg.CACHE_RATES_BANK_PATH)
        root = tree.getroot()
        raw_data = root.findall('Valute')
        return(raw_data)

    def __find_target_currency(self, currency_name: str) -> dict:
        """Делаем поиск по названию валюты, и возвращаем полный результат."""
        raw_data = self.__get_raw_data()
        print(raw_data)
        for currency in raw_data:
            print(currency.find('CharCode').text.lower(), currency_name.lower())
            if currency.find('CharCode').text.lower() != currency_name.lower():
                continue
            print(currency.find('Value').text)
            return(
                {
                    'num_code': currency.find('NumCode').text,
                    'var_code': currency.find('CharCode').text,
                    'nominal': int(currency.find('Nominal').text),
                    'name': currency.find('Name').text,
                    'value': float(currency.find('Value').text.replace(',', '.')),
                }
            )
        return({})
                
    def get_currency_rate(self, currency_name: str) -> dict | None:
        """Основной метод запуска поиска валюты."""
        rates_bank = self.__get_currency_rates()
        self.__write_new_rates(rates_bank=rates_bank)
        return(self.__find_target_currency(currency_name))
