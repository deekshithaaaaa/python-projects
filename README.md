# ☕ Coffee Machine

A console-based Coffee Machine application built with **Python and Object-Oriented Programming (OOP)**.

The program allows users to buy coffee, check machine resources, fill resources, and manage collected money.

## Features

* ☕ Buy Espresso, Latte, or Cappuccino
* 💧 Check available water, milk, and coffee beans
* 💰 Process payments and calculate change
* 🪙 Track money collected by the machine
* 🔄 Fill machine resources
* 💵 Take money from the machine
* 🚪 Exit the machine safely
* ❌ Handle invalid coffee selections and commands

## OOP Concepts Used

This project was created to practice Python OOP concepts including:

* Classes and Objects
* Constructors (`__init__`)
* Instance Variables
* Composition
* Encapsulation
* Conditional logic and object interaction

## Coffee Menu

| Coffee     | Price | Water |  Milk | Coffee Beans | Cups |
| ---------- | ----: | ----: | ----: | -----------: | ---: |
| Espresso   |    40 | 20 ml |  0 ml |         20 g |    1 |
| Latte      |    50 | 20 ml | 40 ml |         20 g |    1 |
| Cappuccino |    60 | 20 ml | 30 ml |         20 g |    1 |

## Available Commands

```text
buy
remaining
take
fill
exit
```

### Example

```text
Enter command: buy

Choose: 1.Espresso 2.Latte 3.Cappuccino: 1

Enough resources
Enter the payment amount: 50

Change: 10
Espresso is ready
```

## Technologies

* Python
* Object-Oriented Programming

## How to Run

Clone the repository and run the Python file:

```bash
python coffee_machine.py
```

## Project Purpose

This project was built as a practical exercise to apply Python OOP concepts in a small real-world style application.
