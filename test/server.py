import json


def main():
    #validate
        output = []
        output.append({"descricao": "1 - invalid login", "test": "ccal", "valid": validateusername("ccal")})
        output.append({"descricao": "2 - valid login", "test": "ccal2", "valid": validateusername("ccal2")})
        output.append({"descricao": "3 - invalid password", "test": "piza", "valid": validatepassword("ccal2", "piza")})
        output.append({"descricao": "4 - valid password", "test": "pizza", "valid": validatepassword("ccal2", "pizza")})
        
        dumpjson(output, "validate.json")

    #validate2
        output2 = []
        
        index = validateusername("ccal")
        if index == -1:
            status = False
        else:
            status = True
        output2.append({"descricao": "1 - invalid login", "test": "ccal", "valid": status})

        index = validateusername("ccal2")
        if index == -1:
            status = False
        else:
            status = True
        output2.append({"descricao": "2 - valid login", "test": "ccal2", "valid": status})

        output2.append({"descricao": "3 - invalid password", "test": "piza", "valid": validatepassword(index, "piza")})
        output2.append({"descricao": "4 - valid password", "test": "pizza", "valid": validatepassword(index, "pizza")})
        
        dumpjson(output2, "validate2.json")

    #registerDeleteUsers
        registeruser(False, "Eudson", "emas", "cheeseburguer")
        deleteuser("vvs3")

    #registerDeleteBuses
        registerbus("003", "AA", "543", "PGC-7504")
        deletebus("002")

    #registerOccurences
        registeroccurence("004", "01/08/2018", "15:24", False, "", "", "", False, "")
	


#read from and write to json file
def loadjson(filename):
    with open(filename) as f:
        data = json.load(f)
    
    return data

def dumpjson(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys = False, indent = 4)


#validate
def validateusername(username):
    userslist = loadjson("users.json")["users"]
    found = False

    for user in userslist:
        if user["login"] == username:
            found = True
            break
	
    return found

def validatepassword(username, password):
    userslist = loadjson("users.json")["users"]
    return userslist["login" == username]["password"] == password


#validate2
def validateusername2(username):
    userslist = loadjson("users.json")["users"]

    for i, user in enumerate(userslist):
        if user["login"] == username:
            return i
	
    return -1

def validatepassword2(index, password):
    userslist = loadjson("users.json")["users"]
    return userslist[index]["password"] == password


#registerDeleteUsers
def registeruser(admin, name, login, password):
    userslist = loadjson("users.json")["users"]
    userslist.append({"admin": admin, "name": name, "login": login, "password": password})
    dumpjson(userslist, "usersTest.json")

def deleteuser(login):
    userslist = loadjson("users.json")["users"]
    index = -1
    
    for i, user in enumerate(userslist):
        if user["login"] == login:
            index = i

    if index != -1:
        userslist.pop(index)
        dumpjson(userslist, "usersTest.json") #TODO: - change file name to "users.json" !!
        return True

    return False


#registerDeleteBuses
def registerbus(id, company, linenumber, plate):
    buseslist = loadjson("buses.json")["buses"]
    buseslist.append({"busid": id, "company": company, "linenumer": linenumber, "plate": plate})
    dumpjson(buseslist, "busTest.json")

def deletebus(id):
    buseslist = loadjson("buses.json")["buses"]
    index = -1
    
    for i, bus in enumerate(buseslist):
        if bus["busid"] == id:
            index = i

    if index != -1:
        buseslist.pop(index)
        dumpjson(buseslist, "busTest.json") #TODO: - change file name to "buses.json" !!
        return True

    return False


#registerOccurences
def registeroccurence(busid, date, alerttime, responded, responsetime, responderlogin, finishtime, successfull, notes):
    occurenceslist = loadjson("occurences.json")["occurences"]
    
    if responded:
        occurenceslist.append({"busid": busid, "date": date, "alerttime": alerttime, "responded": responded, "responsetime": responsetime, "responderlogin": responderlogin, "finishtime": finishtime, "successfull": successfull, "notes": notes})
    else:
        occurenceslist.append({"busid": busid, "date": date, "alerttime": alerttime, "responded": responded})

    dumpjson(occurenceslist, "occurencesTest.json") #TODO: - change file name to "occurences.json" !!



if __name__ == "__main__":
    main()
