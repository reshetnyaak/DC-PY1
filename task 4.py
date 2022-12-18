import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=",", new_line="\n") -> list[dict]:
    with open(file) as f:
        data = f.readlines()
        data = [line.rstrip() for line in data]

    list_of_lists = [val.split(",") for val in data]

    headlines_list = list_of_lists[0]
    list_dict = []
    for string in list_of_lists[1:]:
        dict_ = {headlines_list[element]: string[element] for element in range(len(headlines_list))}
        list_dict.append(dict_)

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
