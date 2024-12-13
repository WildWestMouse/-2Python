import doctest


class Door:
    def __init__(self, door_status: bool, door_lock: bool, pincode: list):
        """
        Данный класс описывает дверь
        :param door_status:
        :param door_lock:
        :param pincode:

        >>> door = Door(True, True, [3, 4, 5, 0])
        >>> door.switch_status()
        >>> print(door.door_status)
        False
        >>> door.set_pincode([0, 5, 2, 7, 8])
        >>> print(door.pincode)
        [0, 5, 2, 7, 8]
        """
        self.door_status = door_status
        self.door_lock = door_lock
        self.pincode = pincode

    def switch_status(self) -> None:
        """
        Данный метод открывает/закрывает дверь
        :return:
        """
        if self.door_status is True:
            self.door_status = False
        else:
            self.door_status = True

    def set_pincode(self, code: list) -> None:
        """
        Данный метод описывает процедуру установки пин-кода на дверной замок
        :param code:
        :return:
        """
        if self.door_lock is False:
            raise ValueError("It doesn't even has a lock")
        else:
            self.pincode = code

class Trashcan:
    """
    Данный класс описывает мусорную корзину
    >>> trashcan = Trashcan(20, 10)
    >>> trashcan.clear()
    >>> print(trashcan.trashcan_occupied)
    0
    >>> trashcan.add_trash(15)
    >>> print(trashcan.trashcan_occupied)
    15
    >>> trashcan_1 = Trashcan(20, 40)
    >>> print(trashcan_1.calculate_unnecessary_trash())
    20
    """
    def __init__(self, trashcan_capacity, trashcan_occupied: float):
        if not trashcan_capacity < 0:
            self.trashcan_capacity = trashcan_capacity
            if not trashcan_capacity < 0:
                self.trashcan_occupied = trashcan_occupied
            else:
                raise TypeError("Не бывает отрицательной занятости")
        else:
            raise TypeError("Не бывает отрицательной вместимости")

    def clear(self) -> None:
        """
        Данный метод очищает мусорную корзину
        :return None:
        """
        self.trashcan_occupied = 0

    def add_trash(self, trash_volume: float) -> None:
        """
        Данный метод добавляет новый мусор в мусорную корзину
        :param trash_volume: Объём мусора, который мы помещаем в мусорное ведро
        :return None:
        """
        self.trashcan_occupied += trash_volume
        if self.trashcan_occupied > self.trashcan_capacity:
            raise TypeError("Мусорная корзина переполнена!")

    def calculate_unnecessary_trash(self) -> float:
        """
        Данный метод вычисляет лишний мусор в мусорной корзине
        :return float:
        """
        if self.trashcan_occupied >= self.trashcan_capacity:
            unnecessary_trash = self.trashcan_occupied - self.trashcan_capacity
        else:
            raise TypeError("Мусорная корзина не переполнена!")
        return  unnecessary_trash


class Order:
    """
    Данный класс описывает заказ в ресторане или кафе
        >>> order = Order(['Бургер', 'Кола 0,5 л', 'Картошка фри'], 512)
        >>> order.close_order()
        >>> print(order.order_status)
        False
        >>> order.reorder()
        >>> print(order.order_status)
        True
        >>> order.add_to_order(['Куриный суп'], 300)
        >>> print(order.order_list)
        ['Бургер', 'Кола 0,5 л', 'Картошка фри', 'Куриный суп']
        """
    def __init__(self, order_list: list, order_value: float):
        if not order_value < 0:
            self.order_list = order_list
            self.order_value = order_value
            self.order_status = True
        else:
            raise TypeError("Отрицательная цена?")

    def add_to_order(self, new_order_list: list, new_order_value: float) -> None:
        """
        Данный метод добавляет позиции к заказу вместе с их ценой
        :param new_order_list: Позиции меню, что добавляются к заказу
        :param new_order_value: Цена позиций, что добавляются к заказу
        :return None:
        """
        if self.order_status is True:
            self.order_list += new_order_list
            self.order_value += new_order_value
        else:
            raise TypeError("Заказ уже закрыт.")

    def close_order(self) -> None:
        """
        Данный метод закрывает заказ
        :return None:
        """
        if self.order_status is True:
            self.order_status = False
        else:
            raise TypeError("Заказ уже закрыт.")

    def reorder(self) -> None:
        """
        Данный метод совершает новый заказ на основе прошлого
        :return None:
        """
        if self.order_status is False:
            self.order_status = True
        else:
            raise TypeError("Заказ ещё не закрыт. Оплатите заказ.")

if __name__ == "__main__":
    doctest.testmod()