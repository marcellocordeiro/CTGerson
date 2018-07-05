import json

def loadjson(filename):
    with open(filename) as f:
        data = json.load(f)
    
    return data

def dumpjson(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys = False, indent = 4)

def main():
    data = loadjson("users.json")

    data["users"].append({"admin": True, "name": "test", "login": "testlog", "password": "testpass"})
    dumpjson(data, "test.json")

    print(type(data))

    print(type(data["users"]))
    
    """ for el in data["users"]:
        print(type(el))
        print(type(el['type'])) """

if __name__ == "__main__":
    main()