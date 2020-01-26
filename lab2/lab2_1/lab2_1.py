import os.path

try:
    filename = input('Enter a file name: ')

except IOError:
    print('Check the availability of the file')

else:
    if os.path.isfile(filename):
        data_tuple = tuple(open(filename, 'r'))
        if len(data_tuple) > 0:
            data = [data_tuple[i].split() for i in range(len(data_tuple))]

            try:
                format_data = dict()

                for i in range(len(data_tuple)):
                    for j in range(i+1, len(data_tuple)):
                        if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                            number = float(data[i][2])
                            data[i][2] = number + float(data[j][2])
                            print(data[i][2], data[j][2])
                modify_data = data[::-1]
                data_dict = dict()
                for i in range(len(data_tuple)):
                    data_dict[modify_data[i][0]+ ' '+modify_data[i][1]] = modify_data[i][2]

                for i in sorted(data_dict.keys()):
                    print(i, data_dict[i], end="\n")
            except:
                print('Check the correctness of the entered data')

        else:
            print('Check the length of the file')

    else:
        print('Check the file name')