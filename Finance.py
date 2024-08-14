def calculate_finance(monthly_income: float, tax_rate: float, other_expense: float, currency: str) -> None:
    monthly_tax: float = monthly_income * tax_rate/100
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    yearly_expense: float = other_expense * 12
    yearly_left = yearly_net_income - yearly_expense
    print('--------------------------')
    print(f'Monthly income: {currency}{monthly_income: ,.2f}')
    print(f'Monthly tax: {currency}{monthly_tax: ,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income: ,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax: ,.2f}')
    print(f'Yearly expense: {currency}{yearly_expense: ,.2f}')
    print(f'Yearly left income: {currency}{yearly_left: ,.2f}')
    print('--------------------------')


def get_amount(text: str) -> float:
    try:
        amount = float(input(text))
        if amount < 0:
            print("The amount must non negative")
            return get_amount(text)
        return amount
    except ValueError as e:
        print(e)
        return get_amount(text)


def finance() -> None:
    others: float = 0.0
    monthly_input = get_amount('Enter your monthly income: ')
    tax_rate = get_amount('Enter tax rate (%)')
    while 1:
        ans = input('Do you have other monthly expense (y/n): ')
        if ans == 'y':
            other = get_amount('Enter the expense: ')
            others += other
        else:
            break
    calculate_finance(monthly_input, tax_rate, others, currency='Euro')

