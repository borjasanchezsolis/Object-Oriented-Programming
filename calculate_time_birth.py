from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        year, month, day = input('Date of birth: ').split('-')
    except ValueError:
        sys.exit('Invalid Date')

    print(minutes_lived(year, month, day))


def minutes_lived(year, month, day):
    try: 
        dte = date(int(year), int(month), int(day))
    except ValueError:
        return 'Invalid Date'
    tday = date.today()
    difference = tday - dte
    minutes = int(difference.total_seconds() / 60)
    msg = p.number_to_words(minutes, andword='') + ' minutes'
    return msg.capitalize()


if __name__ == '__main__':
    main()