import csv



def get_csv_data(file_path):
    rows = []
    # open the CSV file
    data_file = open(file_path)
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


# login_data = list(map(lambda x: x != ["email", "password", "message"], csv.reader(open("./test_data/login_data.csv"))))