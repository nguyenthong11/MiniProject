from Finance import finance
from WordCount import word_count
from SiteStatusCheck import check_url
import Morse_code
from CurrencyConvert import GetCurrencies, print_currencies, exchange_rate, convert


def main() -> None:
    while True:
        print('\n1. Income computation')
        print('2. Check URL status')
        print('3. Words count')
        print('4. Morse code convert')
        print('5. Currency rate convert')
        print('q. Exit')
        match input("Enter your choice: "):
            case '1':
                finance()
            case '2':
                check_url()
            case '3':
                word_count()
            case '4':
                while True:
                    print('1. Text to Morse')
                    print('2. Morse to text')
                    print('0. Return')
                    select = input("You select: ")
                    if select == '1':
                        t = input('Text: ')
                        print(Morse_code.text2morse(t))
                    elif select == '2':
                        t = input('Morse code: ')
                        print(Morse_code.morse2text(t))
                    elif select == '0':
                        break
                    else:
                        print("Invalid choice")
            case '5':
                exec(open("CurrencyConvert.py").read())
            case 'q':
                print('Exiting...')
                break
            case _:
                print("Invalid choice.")


if __name__ == '__main__':
    main()
