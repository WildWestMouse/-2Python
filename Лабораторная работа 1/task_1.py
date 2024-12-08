from xmlrpc.client import boolean
import doctest


class Door:
    """Дверь"""

    def __init__(self, door_status: boolean, door_lock: boolean, pincode: list):
        self.door_status = door_status
        self.door_lock = door_lock
        self.pincode = pincode

    def switch_status(self):
        """Метод открывает/закрывает дверь"""
        if self.door_status is True:
            self.door_status = False
        else:
            self.door_status = True

    def set_pincode(self, code):
        """Метод устанавливает код на дверь"""
        if self.door_lock is False:
            raise ValueError("It doesn't even has a lock")
        else:
            self.pincode = code

class Trashcan:
    """Мусорное ведро"""
    def __init__(self, trashcan_capacity, trashcan_occupied: float):
        if not trashcan_capacity < 0:
            self.trashcan_capacity = trashcan_capacity
            if not trashcan_capacity < 0:
                self.trashcan_occupied = trashcan_occupied
            else:
                raise TypeError("Не бывает отрицательной занятости")
        else:
            raise TypeError("Не бывает отрицательной вместимости")

    def clear(self):
        """Метод очистки мусорного ведра"""
        self.trashcan_occupied = 0

    def add_trash(self, trash_volume):
        """Метод добавляет мусор в мусорное ведро"""
        self.trashcan_occupied += trash_volume
        if self.trashcan_occupied > self.trashcan_capacity:
            raise TypeError("Мусорная корзина переполнена!")

    def calculate_unnecessary_trash(self):
        """Метод высчитывает объём лишнего мусора"""
        if self.trashcan_occupied >= self.trashcan_capacity:
            unnecessary_trash = self.trashcan_occupied - self.trashcan_capacity
        else:
            raise TypeError("Мусорная корзина не переполнена!")
        return  unnecessary_trash


if __name__ == "__main__":
    doctest.testmod()

class Order:
    """Заказ в каком-нибудь кафе"""
    def __init__(self, order_list: list, order_value: float):
        if not order_value < 0:
            self.order_list = order_list
            self.order_value = order_value
            self.order_status = True
        else:
            raise TypeError("Отрицательная цена?")

    def add_to_order(self, new_order_list, new_order_value):
        """Метод добавляет к существующему заказу новые позиции"""
        if self.order_status is True:
            self.order_list += new_order_list
            self.order_value += new_order_value
        else:
            raise TypeError("Заказ уже закрыт.")

    def close_order(self):
        """Метод закрывает заказ"""
        if self.order_status is True:
            self.order_status = False
        else:
            raise TypeError("Заказ уже закрыт.")

    def reorder(self):
        """Метод заказывает тот же заказ ещё раз"""
        if self.order_status is False:
            self.order_status = True
        else:
            raise TypeError("Заказ ещё не закрыт. Оплатите заказ.")

        if __name__ == "__main__":
            doctest.testmod()