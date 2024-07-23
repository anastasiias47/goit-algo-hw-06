from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not (len(value) == 10):
            raise Exception("not valid number")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phones_to_add: str):
        self.phones.append(Phone(phones_to_add))

    def remove_phone(self, phone_to_remove: str):
        self.phones.remove(Phone(phone_to_remove))

    def edit_phone(self, old_phone, new_phone):
        if old_phone not in map(lambda phone: phone.value, self.phones):
            raise ValueError('No such number for this person')
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone_to_find):
        if phone_to_find in map(lambda phone: phone.value, self.phones):
            return Phone(phone_to_find)
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        else:
            return None

    def delete(self, name):
        del self.data[name]

    def __str__(self):
        output_string = ""
        for key in self.data.keys():
            output_string += f"{key}: Phones ({'; '.join(p.value for p in self.data[key].phones)})\n"

        return output_string

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

print(book)

# Додавання запису John до адресної книги

 # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
print(john)
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john_record.find_phone("5555555555")
print(f"{john_record.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")