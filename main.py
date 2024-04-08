class Car():
    def __init__(self, make, model):
        self.public_make = make   # Открытый атрибут
        self._protected_model = model   # Защищенный атрибут
        self.__private_year = 2022    # Приватный атрибут

    def public_metod(self):
        return f"Это открытый метод. Машина {self.public_make} {self._protected_model}"

    def _protected_metod(self):
        return "Это защищённый метод"

    def __private_metod(self):
        return "Это приватный метод"


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        # Можно обратиться с открытому и защищённому атрибуту, но не к приватному
        details = f"{self.public_make} {self._protected_model} имеет батарею мощностью {self.battery_size} KWh"
        # Нельзя напрямую обратиться  к __private_year и __private_metod
        return details

tesla = ElectricCar('Tesla', 'Model S', 100)

print(tesla.public_make)
print(tesla.public_metod())

print(tesla._protected_model)
print(tesla._protected_metod())

print(tesla._Car__private_year)

print(tesla.get_details())



