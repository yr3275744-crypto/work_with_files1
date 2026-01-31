#question 1
def search_str_in_file(file_name:str, string:str):
    result = []
    with open(file_name, "r") as file:
        for line in file:
            if line.startswith(string):
                result.append(line)
    return result

#question 2
def print_file(file_name:str):
    with open(file_name, "r") as file:
        for line in file:
            print("/" * len(line.strip()), "**", line.strip(), "**")
