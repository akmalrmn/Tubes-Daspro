def csv_to_list(csv_path, row, collumns):
    i = 0
    csv_list = [[None for j in range(collumns)] for i in range(row)]
    with open(csv_path, 'r') as csv:
        lines = csv.readlines()
        for baris in lines:
            kata_grup = []
            kata = ''
            for huruf in baris:
                if huruf == ';':
                    kata_grup += [kata]
                    kata = ''
                elif huruf == '\n':
                    kata_grup += [kata]
                    csv_list[i] = kata_grup
                    i += 1
                    break
                else:
                    kata += huruf
            else:
                kata_grup += [kata]
                csv_list[i] = kata_grup
    return csv_list
