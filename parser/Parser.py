from datetime import datetime
from typing import Optional

from bs4 import BeautifulSoup as bs
import requests

from .Models import ShedulePage


class Parser:
    @classmethod
    def get_page(cls, group: str, date: Optional[str] = None):
        self = cls()
        url = self.create_shedule_link(group, date)
        res = requests.get(url)
        res.encoding = "utf-8"
        soup = bs(res.text, "lxml")
        soup = soup.find(class_="расписание").findAll("tr")
        return ShedulePage(soup)

    @staticmethod
    def create_shedule_link(group: str, date: Optional[str] = None):
        url = "https://расписание.нхтк.рф/"
        if date:
            url += f".архив/{date}/"
        url += f"{group}.html"
        return url

    @classmethod
    def get_groups(cls, date: Optional[str] = None):
        self = cls()
        url = "https://расписание.нхтк.рф/"
        if date:
            url += f".архив/{date}/"
        url += "группы.html"
        return self.parse_groups(url)

    @staticmethod
    def parse_groups(url: str):
        res = requests.get(url)
        res.encoding = "utf-8"
        soup = bs(res.text, "lxml")
        soup = soup.find(class_="колонки-группы").findAll("p")
        return {
            "groups": [i.text for i in soup]
        }

    @classmethod
    def get_archives(cls, year: Optional[int] = None):
        self = cls()
        if year is None:
            year = datetime.today().year
        url = f"https://расписание.нхтк.рф/.архив/{year}.html"
        return self.parse_archives(url)

    @staticmethod
    def parse_archives(url: str):
        res = requests.get(url)
        res.encoding = "utf-8"
        soup = bs(res.text, "lxml")
        soup = soup.findAll("li")
        return {
            "archives": [i.text for i in soup]
        }
