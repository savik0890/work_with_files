files_list = ['1.txt', '2.txt', '3.txt']

files_dict = []
for file in files_list:
    with open(file, 'r') as new_file:
        list = new_file.readlines()
        files_dict.append({'file': file, 'length': len(list), 'data': list})

files_dict = sorted(files_dict, key=lambda x: x['length'])

with open('new_file.txt', 'a') as final_file:
    for list in files_dict:
        final_file.write(list['file'] + '\n')
        final_file.write(str(list['length']) + '\n')
        final_file.write(''.join(list['data']) + '\n')
final_file.close()
