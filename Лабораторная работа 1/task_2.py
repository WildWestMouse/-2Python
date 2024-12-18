from task_1 import Door, Trashcan, Order

if __name__ == "__main__":
    door = Door(True, True, [1,2,3,4])
    order = Order(['Чизбургер','5 за 200'], 512)
    trashcan = Trashcan(100, 92)

    try:
        door.door_lock = False
        door.set_pincode([2,3])
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        trashcan.add_trash(100)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        order.reorder()
    except TypeError:
        print('Ошибка: неправильные данные')
