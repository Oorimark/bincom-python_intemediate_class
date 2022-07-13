from select import error

def loading(msg = ""):
    print(f"loading... 📍 \n{msg}")
     
def search_not_found():
    print("No item matches this search!")

def InvalidOption():
    raise error("Invalid option type")

def pretty_print(msg = ""):
    print("==========")

def pretty_output(key, result, unit = ""):
    print(f" > {key} is {result} {unit}")