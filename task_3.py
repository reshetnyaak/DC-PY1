OUTPUT_FILE = "output.csv"

headers_list = ['longtitude', 'latitude', 'housing_median_age', 'total_rooms']
data = [
    ['-112.050000', '37.370000', '27.0000', '38885.000'],
    ['-112.050000', '37.370000', '27.0000', '38885.000'],
    ['-112.050000', '37.370000', '27.0000', '38885.000']
]


def concatenate_list_elements(lst: list, delimiter: str) -> str:
    return delimiter.join(map(str, lst)) + '\n'


def to_csv_file(file_name: str, headers: [list], data: [list[list]], delimiter: str):
    with open(file_name, 'w') as out:
        out.write(concatenate_list_elements(headers, delimiter))
        for line in data:
            out.write(concatenate_list_elements(line, delimiter))


to_csv_file(OUTPUT_FILE, headers_list, data, ',')
