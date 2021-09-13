
class A:
    def _private(self):
        print('Это приватный метод')


class B:
    def __private(self):
        """Даёт  большую защиту: становится недоступным по этому имени"""
        print('Это приватный метод')