data = ("Aleksei", "QA")

def print_person_data(first_name, last_name):
    print(first_name)
    print(last_name)

# распаковка кортежа
print_person_data(*data)