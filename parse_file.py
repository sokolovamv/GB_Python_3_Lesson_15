import argparse
import logging
import task_1

FORMAT = '{levelname:<8} - {asctime} - строка {lineno:03d} -  функция "{funcName}()", сообщение: {msg}'

logging.basicConfig(
    filename="task_1.log",
    encoding='utf-8',
    format=FORMAT,
    style='{',
    level=logging.NOTSET
)

def main():
    parser = argparse.ArgumentParser(description='Person of company')
    parser.add_argument('surname', help='surname')
    parser.add_argument('name', help='name')
    parser.add_argument('father_name', help='father_name')
    parser.add_argument('age', help='age', type=int)
    args = parser.parse_args()

    try:
        person = task_1.Person(args.surname, args.name, args.father_name, args.age)
        person.birthday()
        print(person.get_age())

    except task_1.InvalidNameError:
        logging.error(f'Invalid name. Name should be a non-empty string.')
    except task_1.InvalidAgeError:
        logging.error(f'Invalid age. Age should be a positive integer.')
    except task_1.InvalidIdError:
        logging.error(f'Invalid id. Id should be a 6-digit positive integer between 100000 and 999999.')

if __name__ == '__main__':
    main()

# ввести в командной  строке: python3 parse_file.py "Alice" "Smith" "Johnson" 30