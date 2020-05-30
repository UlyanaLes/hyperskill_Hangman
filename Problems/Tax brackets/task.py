def tax(ic, percent):
    print(f'The tax for {ic} is {percent}%. That is {income * percent / 100:.0f} dollars!')


income = int(input())

if 0 < income <= 15527:
    tax(income, 0)
elif 15527 < income <= 42707:
    tax(income, 15)
elif 42707 < income <= 132406:
    tax(income, 25)
elif income > 132406:
    tax(income, 28)
