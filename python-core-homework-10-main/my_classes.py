from collections import UserDict


class Field:
    def __init__(self, value:str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number format")
        super().__init__(value)
        self.value = value    
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone:str): 
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.phones.append(Phone(new_phone))

    def find_phone(self, phone:str):
        for x in self.phones:
            if x.value == phone:
                return x
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self[str(record.name)] = record

    def find(self, name) -> Record:
        if name in self.keys():
            found_rec = self.get(name)
            return found_rec
            
    def delete(self, name):
        if name in self.keys():
            self.pop(name)
