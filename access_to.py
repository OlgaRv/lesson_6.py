# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:
## 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
## 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять
# и удалять пользователей из списка (представь, что это просто список экземпляров User).
## 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, name, access_level='User'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name, access_level='Admin'):
        super().__init__(user_id, name, access_level)
        self.__users_list = []

    def add_user(self, user):
        self.__users_list.append(user)

    def remove_user(self, user):
        self.__users_list.remove(user)

    def get_users_list(self):
        return self.__users_list

# Создание пользователей
user1 = User(1, 'Анна')
user2 = User(2, 'Пётр')
user3 = User(3, 'Мария')

admin = Admin(4, 'Степан')

# Добавление пользователей в список администратора
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Вывод списка пользователей, добавленных администратором
for user in admin.get_users_list():
    print(user.get_user_id(), user.get_name(), user.get_access_level())

print(admin.get_user_id(), admin.get_name(), admin.get_access_level())