# Development Notes

## Assumptions and Decisions

### 1. One Group

The program manages only one susu group at a time.

This keeps the scope small and focuses on the main contribution and payout process.

### 2. Fixed Weekly Contribution

When the group is created, the weekly contribution is fixed.

For example, if the group is created with a contribution of GHS 100, every member is expected to contribute GHS 100 each week.

### 3. Minimum of Two Members

The program requires at least two members before payments can be recorded or a week can be closed.

A susu rotation would not make practical sense with only one member.

### 4. Member Order Determines Payout Order

Members receive the weekly pot in the same order in which they joined.

For example:

```text
1. Alice
2. Bob
3. Charles
```

The payout order will be:

```text
Week 1 → Alice
Week 2 → Bob
Week 3 → Charles
```

### 5. Partial Payments Are Allowed

Members do not have to pay the entire weekly contribution at once.

For example, if the weekly contribution is GHS 100, a member can first pay GHS 40 and later pay the remaining GHS 60.

The week can only be closed after every member has paid the full GHS 100.

### 6. No Overpayments

A member cannot pay more than the amount they still owe.

For example, if a member owes GHS 60, a payment of GHS 70 is rejected.

The payment is not partially accepted.

### 7. Members Cannot Be Added After Payments Start

Once the first valid payment has been recorded, new members cannot be added.

This prevents the group membership and expected weekly pot from changing after the contribution cycle has started.

### 8. One Rotation Cycle

The current version ends the cycle after every member has received the pot once.

For example, with three members:

```text
Week 1 → Member 1
Week 2 → Member 2
Week 3 → Member 3
```

After the third payout, the program reports that the cycle is finished.

A future version could allow the rotation to automatically start again.

### 9. No Persistent Storage

All information is stored in Python variables while the program is running.

If the program is closed, the group information, payments, and payout history are lost.

A future version could use SQLite, PostgreSQL, or another database to permanently store the information.

### 10. Money Uses Decimal

The program uses Python's `Decimal` type instead of floating-point numbers.

This was chosen because the application handles money and should avoid floating-point rounding problems.

### 11. Two Decimal Places

Amounts are limited to two decimal places because the contribution amounts are in Ghana cedis.

Examples of valid amounts:

```text
100
50.50
25.75
```

An amount such as:

```text
20.555
```

is rejected.

## What I Learned

This project helped me practise:

- Python functions
- Variables and global state
- Lists and dictionaries
- Loops
- Conditional statements
- Input validation
- Exception handling
- The `Decimal` type
- Basic automated testing
- Designing a simple command-line application

## Future Improvements

If I continued developing the project, I would consider adding:

1. Persistent database storage.
2. Multiple susu groups.
3. Member IDs and contact information.
4. Login and administrator accounts.
5. Transaction records.
6. Payment dates and timestamps.
7. A database-backed API.
8. A web or mobile interface.
9. Better reporting and financial summaries.
10. Notifications for members who have outstanding contributions.
11. Ability to restart a completed rotation cycle.
12. Stronger audit and transaction history.

## Development Approach

I intentionally kept the first version simple and focused on the core business rules.

The goal was to make sure that contributions, partial payments, validation, weekly closing, and payouts work correctly before introducing more advanced features such as databases, authentication, or a graphical interface.