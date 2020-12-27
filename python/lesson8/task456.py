from abc import ABC


class Warehouse:
    printers = []
    scanners = []
    xeroxes = []

    def put(self, office_equipment):
        if type(office_equipment) is Printer:
            self.printers.append(office_equipment)
        if type(office_equipment) is Scanner:
            self.scanners.append(office_equipment)
        if type(office_equipment) is Xerox:
            self.xeroxes.append(office_equipment)

    def borrow_printer(self):
        if len(self.printers) > 0:
            return self.printers.pop()
        else:
            return None

    def borrow_scanner(self):
        if len(self.scanners) > 0:
            return self.scanners.pop()
        else:
            return None

    def borrow_xerox(self):
        if len(self.xeroxes) > 0:
            return self.xeroxes.pop()
        else:
            return None


class OfficeEquipment(ABC):
    def __init__(self, name):
        if not name:
            raise ValueError("empty name")
        self.name = name

    def __str__(self):
        return f"name = {self.name}"


class Printer(OfficeEquipment):
    def __init__(self, name, is_coloured):
        super(Printer, self).__init__(name)
        self.is_coloured = is_coloured

    def __str__(self):
        return f"Printer with {super(Printer, self).__str__()} and is_coloured = {self.is_coloured}"


class Scanner(OfficeEquipment):
    def __init__(self, name, resolution):
        super(Scanner, self).__init__(name)
        self.resolution = resolution

    def __str__(self):
        return f"Scanner with {super(Scanner, self).__str__()} and resolution = {self.resolution}"


class Xerox(OfficeEquipment):
    def __init__(self, name, max_format):
        super(Xerox, self).__init__(name)
        self.max_format = max_format

    def __str__(self):
        return f"Xerox with {super(Xerox, self).__str__()} and max_format = {self.max_format}"


warehouse = Warehouse()
while True:
    action = input("Enter an action (put, get, quit): ")
    if action == "quit":
        break
    elif action == "put":
        device = input("Enter a device (printer, xerox, scanner): ")
        if device == "printer":
            p_name = input("Enter a name: ")
            p_is_coloured = input("Is coloured? ")
            warehouse.put(Printer(p_name, p_is_coloured))
        elif device == "xerox":
            p_name = input("Enter a name: ")
            p_max_format = input("Enter max format: ")
            warehouse.put(Xerox(p_name, p_max_format))
        elif device == "scanner":
            p_name = input("Enter a name: ")
            p_resolution = input("Enter resolution: ")
            warehouse.put(Scanner(p_name, p_resolution))
        else:
            print("Unknown device type")
    elif action == "get":
        device = input("Enter a device (printer, xerox, scanner): ")
        if device == "printer":
            print(warehouse.borrow_printer())
        elif device == "scanner":
            print(warehouse.borrow_scanner())
        elif device == "xerox":
            print(warehouse.borrow_xerox())
        else:
            print("Unknown device type")
    else:
        print("Unknown action type")
