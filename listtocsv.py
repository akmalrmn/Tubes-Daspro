def list_to_csv(my_list, filename):
    # Membuat string CSV dari list
    csv_string = ''
    for sublist in my_list:
        line = ''
        for element in sublist:
            line += str(element) + ','
        csv_string += line[:-1] + '\n'

    # Menyimpan string ke dalam file CSV
    with open(filename, mode='w') as file:
        file.write(csv_string)
