from decimal import Decimal
import re

def generator_numbers(text: str):
    pattern = r"\d+\.\d+|\d+" 
    matches = re.findall(pattern, text)
    for match in matches:
        yield Decimal(match)

def sum_profit(text: str, generator_func):
    return sum(generator_func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")