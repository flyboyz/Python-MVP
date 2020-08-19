class User:
    def __init__(self, login, password=''):
        self.__login = login
        self.__password = password

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__password


class Model:
    def __init__(self):
        self.__user = None
        self.__users = [
            User('admin', 'admin'),
            User('test'),
        ]

    def login(self, login, password):
        has_logged = False

        for user in self.__users:
            if login == user.get_login() \
                    and password == user.get_password():
                self.__user = user
                has_logged = True

        if not has_logged:
            self.__user = None

    def message(self):
        return "You're log in." if self.__user is not None else "Wrong login or password!"


class Presenter:
    def __init__(self, model):
        self.model = model

    def login(self, login, password):
        self.model.login(login, password)

        return self.model


model = Model()
presenter = Presenter(model)

loginInput = input('Login: ')
passwordInput = input('Password: ')

model = presenter.login(loginInput, passwordInput)

print('{: ^30}'.format(model.message()))
