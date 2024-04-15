class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = "User"

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'Admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь добавлен")

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"Пользователь {user} удален")

users = []
admin = Admin("a1", "Гоша")
user1 = User("u1", "Степа")

print(user1.get_name())
admin.add_user(users, user1)