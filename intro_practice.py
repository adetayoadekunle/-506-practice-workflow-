# intro_practice.py

# Importing packages
import pandas as pd
import numpy as np

# Variables
number_var = 26
string_var = "Hello,Tayo!"
list_var = [1, 2, 3, 4, 5]
dict_var = {
    'key1': 'value1',
    'key2': [1, 2, 3],
    'key3': {
        'nested_key1': 'nested_value1',
        'nested_key2': 123
    }
}

# Print statements for variables
print("Number Variable:", number_var)
print("String Variable:", string_var)
print("List Variable:", list_var)
print("Dictionary Variable:", dict_var)

# Function definition
def calculate_discount(price, discount_rate):
    """
   Discount based on discount_rate and price
  If/return statement (I think?)
    """
    if discount_rate < 0 or discount_rate > 100:
        return Incorrect discount rate.  Should be between 0 and 100"
    discount_amount = price * (discount_rate / 100)
    final_price = price - discount_amount
    return final_price

# Function call and print statement
price_example = 120  # Example price
discount_rate_example = 30  # Example discount rate
final_price = calculate_discount(price_example, discount_rate_example)
print("Final Price after Discount:", final_price)
