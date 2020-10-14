"""
Author: Brady Trenary
Program: basic_IO.py

"""
FILE_NAME = 'student_into.txt'
MAX = 50
MIN = 1
IOERROR_MES = 'Cannot open file on file system'


def write_to_file(*args):
    try:

        with open(FILE_NAME, 'a') as f:
            f.write(f'{args[1]}, {args[0]}:\t')
            for i in args[2]:
                f.write(f'{i}\t')
            f.write('\n')
    except IOError:
        print('Cannot open file on file system')


def get_student_info(**kwargs):
    print(f"Welcome, {kwargs['first_name']} {kwargs['last_name']}!")
    scores = []
    num = 0
    while num != -1:
        try:
            num = float(input(f"Enter a score between {MIN} and {MAX}, (-1 to exit)"))
            if num == -1:
                break
            elif num < MIN or num > MAX:
                raise ValueError(f"Score must be between {MIN} and {MAX}")
            else:
                scores.append(num)
        except ValueError as err:
            print(err)
    write_to_file(kwargs['first_name'], kwargs['last_name'], scores)


def read_from_file():
    try:
        with open(FILE_NAME, 'r') as f:
            read_line = f.read()
            print(read_line)
    except IOError:
        print(IOERROR_MES)


if __name__ == '__main__':
    get_student_info(first_name='Brady', last_name='Trenary')
    get_student_info(first_name='Tyler', last_name='Durden')
    get_student_info(first_name='Marla', last_name='Singer')
    get_student_info(first_name='Anthony', last_name='Rizzo')
    input('hold....')
    read_from_file()
    input('Press any key to end')
