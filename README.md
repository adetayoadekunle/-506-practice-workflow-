# -506-practice-workflow-
This assignment is a primer for 504/507 Fall semester classes to practice a basic development workflow.
# 506 Practice Workflow

This repository is a practice assignment for the 504/507 Fall semester classes to get familiar with a basic development workflow.

## Variables

The Python file `intro_practice.py` contains the following variables:

- **`number_var`**: An integer variable assigned the value `42`.
- **`string_var`**: A string variable assigned the value `"Hello, world!"`.
- **`list_var`**: A list variable assigned the values `[1, 2, 3, 4, 5]`.
- **`dict_var`**: A dictionary with the following key-value pairs:
  - `'key1'`: `'value1'`
  - `'key2'`: `[1, 2, 3]` (a list)
  - `'key3'`: `{ 'nested_key1': 'nested_value1', 'nested_key2': 123 }` (a nested dictionary)

## Function

The Python file defines a function called `calculate_discount(price, discount_rate)` that performs the following:

- **Parameters:**
  - `price`: The original price before discount.
  - `discount_rate`: The discount rate (in percentage) to be applied.

- **Functionality:**
  - The function checks if the `discount_rate` is between `0` and `100`. If not, it returns an error message.
  - It calculates the discount amount and then computes the final price after applying the discount.

- **Example Usage:**

  ```python
  price_example = 100  # Example price
  discount_rate_example = 15  # Example discount rate
  final_price = calculate_discount(price_example, discount_rate_example)
  print("Final Price after Discount:", final_price)
