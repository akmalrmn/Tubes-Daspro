def list_to_csv(my_list,path,filename):
    # Membuat string CSV dari list
    csv_string = ''
    for sublist in my_list:
        line = ''
        for element in sublist:
            line += str(element) + ';'
        for i in range(len(line)-1):
            csv_string += line[i]
        csv_string += '\n'

    # Menyimpan string ke dalam file CSV
    with open(f'{path}/{filename}', 'w') as file:
        file.write(csv_string)