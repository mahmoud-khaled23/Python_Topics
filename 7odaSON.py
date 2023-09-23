
import json


class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name, self.age, self.weight)

    def data_dict(self):
        return {"name": self.name,
                       "age": self.age,
                       "weight": self.weight}

    def save_to_json(self, filename):
        person_dict = {"name": self.name,
                       "age": self.age,
                       "weight": self.weight}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent=3))

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())

        self.name = data["name"]
        self.age = data["age"]
        self.weight = data["weight"]


def add_to_json(data, filename):
    # file_data = filename
    with open(filename, 'r+') as f:
        file_data = json.load(f)
        print(f'first occ: {file_data}')
        file_data["person"].append(data)
        print(f'second occ: {file_data}')
        f.seek(0)
        json.dump(file_data, f, indent=4)


p1 = Person("sisi", 34, 77)
p2 = Person("bora3ey", 22, 63)
p3 = Person("sawsan", 40, 58)
p4 = Person("fwaaz", 40, 89)
p5 = Person("3absy", 56, 58)
p1.print_info()

# add_to_json(p1.data_dict(), "El-sisi info.json")
with open("El-sisi info.json", 'w') as file:
    json.dump({"person": [p1.data_dict()]}, file, indent=4)

add_to_json(p2.data_dict(), "El-sisi info.json")
add_to_json(p3.data_dict(), "El-sisi info.json")
add_to_json(p4.data_dict(), "El-sisi info.json")
add_to_json(p5.data_dict(), "El-sisi info.json")
