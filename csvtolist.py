def csv_to_list(csv_path):
  csv_list = []
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
                  csv_list += [kata_grup]
                  break
              else:
                  kata += huruf
          else:
              kata_grup += [kata]
              csv_list += [kata_grup]
  return csv_list

