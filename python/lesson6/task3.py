class Worker:
    def __init__(self, name, surname, worker_position, income):
        self.name = name
        self.surname = surname
        self.position = worker_position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{self._income['wage'] + self._income['bonus']}"


position = Position('Andrey', 'Burov', 'Java Developer', {'wage': 20000, 'bonus': 5000})
print(position.get_full_name())
print(position.get_total_income())
