def read_csv(file_path: str)->list|dict:
    import csv

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        # key- 1st column, value- list of items in other columns 
        # out = {row[0]:row[1:] for row in reader}

        # key- index, value- list of items in columns 
        # out = {i: row for i, row in enumerate(reader)}

        # 2D list, each item is line in csv
        out = [row for row in reader]

    return out

def save_as_csv(file_path: str, input: list|dict)->None:
    import csv

    file_extension = ".csv"
    if not file_path.endswith(file_extension): file_path += file_extension

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        # 2D list as input, each child list is a line
        writer.writerows(input)

        # for key, value in input.items():
            # dict with lists as values input, key is 1st columns + list values as others
            # writer.writerow([key]+value)

            # dict with lists as values input, keys discarded, list values as columns
            # writer.writerow(value)
