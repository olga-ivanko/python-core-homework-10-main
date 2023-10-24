from my_classes import Field, Name, Phone, Record, AddressBook


book = AddressBook()


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Use help."
        except KeyError:
            return "Unknown rec_id. Try another or use help."
        except ValueError:
            return "Unknown phone or wrong phone format"
    return inner


def func_normalize_phone(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+38")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )

    return new_phone


@user_error
def func_add(*args):
    rec_id = args[0].lower()
    phone = args[1]
    new_phone = func_normalize_phone(phone)
    new_record = Record(rec_id)
    new_record.add_phone(new_phone)

    if rec_id in book.keys():
        return f"Record alredy exist"
    elif new_phone == None: 
        return f"Check the phone: {phone}. Wrong format."
     
    book[rec_id] = new_record
    return f"Add record {rec_id = }, {new_phone = }"


@user_error
def func_change(*args):
    rec_id = args[0].lower()
    old_phone = func_normalize_phone(args[1])
    new_phone = func_normalize_phone(args[2])

    if old_phone == None: 
        return f"Check the phone: {args[1]}. Wrong format."    
    if new_phone == None: 
        return f"Check the phone: {args[2]}. Wrong format."
    book.find(rec_id).edit_phone(old_phone, new_phone)
    return f"Record {rec_id} is updated with nes phone: {book.get(rec_id).phones[0]}"

    
@user_error    
def func_phone(*args):
    rec_id = args[0]
    return f"Phone of {rec_id} is {book.get(rec_id).phones[0]}"
    

def func_hello(*args):
    return f"How can I help you?"


def func_show_all(*args):
    if len(book)==0:
        return f"Your contacts list is empty"
    f_string_generator = lambda d: "\n".join([f"{rec_id}: {phone.phones[0]}" for rec_id, phone in d.items()])
    result = f_string_generator(book) 
    return result
    

def unknown(*args):
    return "Unknown command. Try again."


def func_good_bye(*args):
    print(f"Good bye!")
    exit()
        

FUNCTIONS = {"hello" : func_hello,
            "add" : func_add,
            "change" : func_change, 
            "phone" : func_phone,
            "show all" : func_show_all,
            "good bye" : func_good_bye, 
            "close" : func_good_bye, 
            "exit" : func_good_bye,
            "": func_good_bye}


def parser(text: str):
    for func in FUNCTIONS.keys():
        if text.startswith(func):
            return func, text[len(func):].strip().split()
    return unknown, []


def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input.lower())
        current_func = FUNCTIONS.get(func)
        print(current_func(*data))
        
        
if __name__ == '__main__':
    main()