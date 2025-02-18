class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    _IP = 0

    def __new__(cls, *args, **kwargs):
        cls._IP += 1
        return super().__new__(cls)

    def __init__(self):
        self.buffer = []
        self.ip = self._IP
        self.router = None

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer); """
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер;
        """
        information = self.buffer[:]
        self.buffer[:] = []
        return information

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """

    def __init__(self):
        self.buffer = []
        self.linked_servers = []

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру """
        if server not in self.linked_servers:
            self.linked_servers.append(server)
            server.router = self

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера """
        if server in self.linked_servers:
            self.linked_servers.remove(server)
            server.router = None

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться) """
        for message in self.buffer:
            for server in self.linked_servers:
                if message.ip == server.ip:
                    server.buffer.append(message)
        self.buffer[:] = []


class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip