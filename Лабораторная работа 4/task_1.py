class Website:
    """
    Класс описывающий сайт в интернете
    """
    def __init__(self, link: str, year: int):
        """
        Это метод инициализации
        :param link: Аргумент являющийся ссылкой на сайт
        :param year: Аргумент являющийся годом основания сайта
        """
        self._link = link
        self._year = year
        self.status = True

    def close_site(self):
        """
        Метод закрывает сайт
        """
        if self.status is True:
            self.status = False

    def __str__(self):
        return f"Ссылка: {self.link}. Год создания: {self.year}. Статус: {self.status}"

    def __repr__(self):
        return f"{self.__class__.__name__}(link={self.link!r}, year={self.year!r})"

    @property
    def link(self) -> str:
        return self._link

    @property
    def year(self) -> int:
        return self._year

    @link.setter
    def link(self, link):
        if not isinstance(link, str):
            raise TypeError('Ссылка должна быть строкой')
        self._link = link

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            if year >= 0:
                self._year = year
            else:
                raise ValueError('Год должен быть положительным числом типа int')
        else:
            raise TypeError('Год должен быть положительным числом типа int')

site1 = Website('site.com', 1999)
print(site1.__str__())
site1.close_site()
print(site1.__str__())

class VKontakte(Website):
    """
    Дочерний класс сайта ВКонтакте
    """
    def __init__(self, link: str, year: int, online: int):
        """
        Метод инициализирует сайт
        :param link: Аргумент являющийся ссылкой на сайт
        :param year: Аргумент являющийся годом основания сайта
        :param online: Аргумент являющийся количеством людей онлайн
        """
        super().__init__(link, year)
        if isinstance(online, int):
            if online >= 0:
                self.online = online
            else:
                raise ValueError('Онлайн должен быть положительным числом типа int')
        else:
            raise TypeError('Онлайн должен быть положительным числом типа int')

    def close_site(self):
        """
        Метод закрывает сайт
        """
        if self.status is True:
            self.status = False
            self.online = 0

    def __str__(self):
        return f"Ссылка: {self.link}. Год создания: {self.year}. Статус: {self.status}. Текущий онлайн: {self.online}"

    def __repr__(self):
        return f"{self.__class__.__name__}(link={self.link!r}, year={self.year!r}, online={self.online!r})"

vkontakte = VKontakte('https://vk.com', 2006, 90000)
print(vkontakte.__str__())
vkontakte.close_site()
print(vkontakte.__str__())