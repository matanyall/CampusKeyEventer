#!/usr/bin/python
from eventer import functions
from os.path import exists
import os
import sys
import argparse

# parser = argparse.ArgumentParser(description='Start Campus Key Eventer')
# # parser.add_argument('student', metavar='[name, ID, email]', type=list, help='student using Eventer')
# # dest="add_student"
# parser.add_argument('-s', '--student', action='store', nargs='+', default=False, help='Add student info, default student if not specified')
# args = parser.parse_args()
# if args.student == ['default']:
#     print("Using default student")
# elif args.student:
#     print(args.student)
# else:
#     print("Using no student")

def arg_parse_initializer():
    parser = argparse.ArgumentParser(description='Start Campus Key Eventer')
    parser.add_argument('-s', '--student', action='store', nargs='+', default=False,
        help='Add student info, default student if not specified')
    return parser.parse_args()


def main():
    args = arg_parse_initializer()
    if args.student == ['default']:
        print("Using default student")
        functions.make_student("firstname lastname", "12345", "firstname@corn.com")
        print(functions.student_list)
    elif args.student:
        print(args.student)
        functions.make_student(args.student[0], args.student[1], args.student[2])
        print(functions.student_list)
    else:
        print("Using no student")
        
    
    if not exists('generated_files/map_secret.html'):
        functions.heatmap_gen()

    
    




if __name__ == "__main__":
    main()