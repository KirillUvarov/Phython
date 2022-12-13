path = 'GB/Seminar/S_7/S_7_Task_1/'
file = 'database.txt'

def input_in_db(text):
    with open(path + file, 'w', encoding = 'UTF-8') as data_base:
        data_base.write(f'{text}\n')
        data_base.close
    # return 