# Python Introduction Tasks

This directory contains beginner Python exercises focused on arithmetic operations, variable assignments, and user input. These tasks are part of the `alx_be_python` repository under the `python_introduction` directory.

---

## 📘 Task 0: Basic Arithmetic Exercise

**File:** `basic_operations.py`

### Objective

Practice basic arithmetic operations in Python by performing predefined calculations.

### Instructions

* Define `number1 = 10` and `number2 = 5`
* Perform:

  * Addition
  * Subtraction (`number1 - number2`)
  * Multiplication
* Print the results in this format:

```
Addition of 10 and 5 is 15
Subtraction of 10 and 5 is 5
Multiplication of 10 and 5 is 50
```

### How to Run

```bash
python3 basic_operations.py
```

---

## 📘 Task 1: Simple Interest Calculator

**File:** `simple_interest.py`

### Objective

Calculate simple interest using the formula: `I = P * R * T`

### Instructions

* Define:

  * `principal = 1000`
  * `rate = 0.05`
  * `time = 3`
* Compute `interest = principal * rate * time`
* Print:

```
The simple interest is: 150.0
```

### How to Run

```bash
python3 simple_interest.py
```

---

## 📘 Task 2: Calculate the Area of a Rectangle

**File:** `rectangle_area.py`

### Objective

Use arithmetic to calculate the area of a rectangle.

### Instructions

* Define:

  * `length = 10`
  * `width = 5`
* Compute `area = length * width`
* Print:

```
The area of the rectangle is: 50
```

### How to Run

```bash
python3 rectangle_area.py
```

---

## 📘 Task 3: Convert Hours to Seconds

**File:** `hours_to_seconds.py`

### Objective

Convert a number of hours into seconds.

### Instructions

* Define: `hours = 2`
* Use: `seconds = hours * 3600`
* Print:

```
2 hour(s) is 7200 seconds.
```

### How to Run

```bash
python3 hours_to_seconds.py
```

---

## 📘 Task 4: User Input Age Calculator

**File:** `future_age_calculator.py`

### Objective

Use user input and arithmetic to calculate the user’s age in 2050.

### Instructions

* Ask: `How old are you? `
* Add 27 to user input (since 2050 - 2023 = 27)
* Print:

```
In 2050, you will be [age] years old.
```

### Example

```
How old are you? 30
In 2050, you will be 57 years old.
```

### How to Run

```bash
python3 future_age_calculator.py
```

---

## 📘 Task 5: Personal Finance Calculator #advanced

**File:** `finance_calculator.py`

### Objective

Calculate monthly and projected annual savings based on user income and expenses.

### Instructions

* Ask the user:

  * `Enter your monthly income: `
  * `Enter your total monthly expenses: `
* Compute:

  * `monthly_savings = income - expenses`
  * `annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)`
* Print:

```
Your monthly savings are $1000.
Projected savings after one year, with interest, is: $12600.
```

### Example

```
Enter your monthly income: 5000
Enter your total monthly expenses: 4000
Your monthly savings are $1000.
Projected savings after one year, with interest, is: $12600.
```

### How to Run

```bash
python3 finance_calculator.py
```

---

Happy Coding! 🚀
