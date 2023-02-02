from logging import exception
import time
import random
import click


class recipe:
    def __init__(self, name: str, size: str, ingridients: list) -> None:
        """_summary_

        Args:
            name (str): название пиццы
            size (str): Размер. XL или L
            ingridients (list):список инградиентов

        Raises:
            exception: неверный размер
        """
        if size not in ["L", "XL"]:
            raise exception("No such size! Only L or XL.")

        self.size = size
        self.name = name
        self.ingridients = ingridients

    def dict(self) -> dict:
        """Возвращает словарь - рецепт пиццы

        Returns:
            dict: {name: [ingredients]}
        """
        return {self.name: self.ingridients}

    def __eq__(self, __o: object) -> bool:
        return (
            self.size == __o.size
            and self.name == __o.name
            and self.ingridients == __o.ingridients
        )


def log(sent="() c"):
    """Измеряет время выполнения функции и выводит в консоль

    Args:
        sent (str, optional): Кастомная строка вывода. Меняет () на время выполнения. Defaults to "() c".
    """

    def decor(func):
        def wrapper(*args, **kwargs):
            t = time.time()
            f_out = func(*args, **kwargs)
            t = time.time() - t
            time_log = sent.replace("()", str(t))
            print(time_log)
            return f_out

        return wrapper

    return decor


ord = click.Group()


@ord.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """готовит пиццу

    Args:
        pizza (str): название пиццы
        delivery (bool): нужна ли доставка
    """

    @log("Приготовили за  () с!")
    def make(t):
        time.sleep(t)

    @log("Доставили за  () с!")
    def deliver(t):
        time.sleep(t)

    make(1)

    if delivery:
        deliver(0.5)


@ord.command()
def menu():
    """Выводит меню ресторана"""
    print("- Margherita: tomato sauce, mozzarella, tomatoes")
    print("- Pepperoni: tomato sauce, mozzarella, pepperoni")


if __name__ == "__main__":
    ord()
