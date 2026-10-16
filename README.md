# Susu_Challenge
This repo is for the Zhuwa Academy coding challenge

# Susu Contribution Management System

## What I Built

I built a simple Python command-line program for managing one rotating susu contribution group.

The program allows a group administrator to:

- Create a susu group with a fixed weekly contribution.
- Add members to the group.
- Record member contributions.
- Accept partial payments.
- Prevent overpayments.
- Close a week when all members have paid in full.
- Automatically calculate the weekly payout.
- Pay members in the order they joined.
- Move to the next week after a successful payout.
- View the current contribution status and payout history.

The program uses Python's `Decimal` type for money calculations to avoid common floating-point rounding problems.

## How the Program Works

A group is created with a fixed weekly contribution.

For example:

- Weekly contribution: GHS 100
- Members: Alice and Bob
- Weekly pot: GHS 200

If Alice pays GHS 100 and Bob pays GHS 100, the week can be closed and the next member in the rotation receives the GHS 200 pot.

If a member has not paid the full amount, the week cannot be closed and no payout is made.

## Requirements

You need:

- Python 3
- `pytest` for running the automated tests

No external database or web server is required.

## Project Files

```text
susu-project/
│
├── susu.py
├── test_susu.py
├── README.md
└── NOTES.md
```

## How to Run the Program

Open a terminal in the project folder and run:

```bash
python susu.py
```

The program will display a menu:

```text
1. Create group
2. Add member
3. Record payment
4. Close week
5. Show report
6. Quit
```



## Important Validation Rules

The program rejects:

- A weekly contribution of zero or less.
- Empty member names.
- Duplicate members.
- Payments of zero or less.
- Payments greater than the amount a member still owes.
- Payments from unknown members.
- Adding new members after the group has started.
- Closing a week when a member still owes money.

Member names are checked without considering uppercase or lowercase letters. For example, `Alice` and `alice` are treated as the same member.

## Money Handling

The program uses Python's `Decimal` class rather than `float` for financial calculations.

Amounts are limited to two decimal places, for example:

```text
100.00
50.50
25.75
```

This helps keep the contribution and payout calculations accurate.

## Limitations

This is a simple command-line prototype.

It currently:

- Stores data only while the program is running.
- Does not use a database.
- Does not have user accounts or authentication.
- Supports one group at a time.
- Does not have a graphical or web interface.
- Ends the rotation after every member has received the pot once.

These limitations were intentional so that the core susu contribution logic could be implemented clearly first.