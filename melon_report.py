"Reads melon_details.csv and prints report"


f = open("melon_details.csv")

counter = 0

melon_dict = {}

for lines in f:
    lines = lines.strip()
    columns = lines.split(',')
    dict_key = columns[0]
    melon_dict[dict_key] = {}
    if counter == 0:
        header_row = columns
    else:
        for i in range(1,len(columns)):
            melon_dict[dict_key][header_row[i]] = columns[i]
    counter +=1


print melon_dict


