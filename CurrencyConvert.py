from requests import get
from pprint import PrettyPrinter

base_url = "https://api.currencyapi.com"
API_KEY = 'cur_live_RxcC9qL51N4gx0Pa5vqKdoGvmn17F9fhsDgTdt8h'
printer = PrettyPrinter()


def GetCurrencies():
    endpoint = f'/v3/currencies?apikey={API_KEY}'
    url = base_url + endpoint
    data = get(url).json()['data']
    data = list(data.items())
    data.sort()
    return data


def print_currencies() -> None:
    currencies = GetCurrencies()
    for name, currency in currencies:
        name = currency['name']
        _id = currency['code']
        symbol = currency.get("symbol_native", "")
        print(f'{_id} - {name} - {symbol}')


def exchange_rate(currency1, currency2):
    endpoint = f'/v3/latest?apikey={API_KEY}&currencies={currency2}&base_currency={currency1}'
    url = base_url + endpoint
    response = get(url).json()
    error = response.get('errors', None)
    if error:
        print('Invalid currency')
        return
    rate = list(response['data'].values())[0]['value']
    print(f'{currency1} -> {currency2} is {rate}')
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)

    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return

    converted_amount = rate*amount
    print(f'{amount} {currency1} is equal to {converted_amount} {currency2}')
    return converted_amount


def main() -> None:
    while True:
        print('\n1. Currencies list')
        print('2. Exchange rate')
        print('3. Convert currency')
        print('q. Quit currency exchange')
        choice = input("Enter your choice: ")
        if choice == '1':
            print_currencies()
        elif choice == '2':
            currency1 = input("Base currency: ").upper()
            currency2 = input("Currency: ").upper()
            exchange_rate(currency1, currency2)
        elif choice == '3':
            currency1 = input("Base currency: ").upper()
            currency2 = input("Currency: ").upper()
            amount = input("Enter the amount: ")
            convert(currency1, currency2, amount)
        elif choice == 'q':
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
