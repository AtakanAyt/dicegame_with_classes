class Player:
    def __init__(self, name):
        self._cookies = 0
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_cookies(self):
        return self._cookies

    def increase_cookies(self):
        self._cookies += 1

    def decrease_cookies(self):
        self._cookies -= 1

    def __eq__(self, name):
        return self._name == name
