

from decimal import Decimal, InvalidOperation

# ---------- the data the program remembers ----------
weekly_amount = None      # how much each member pays per week
members = []              # list of names, in the order they joined
paid = {}                 # name -> how much they paid this week
week = 1                  # current week number
payouts = []              # list of (week, name, amount)
started = False           # becomes True after the first payment


# ---------- small helper functions ----------
def read_amount(text):
    """Turn text like '50' or '30.50' into a Decimal. Returns None if bad."""
    try:
        amount = Decimal(text)
    except InvalidOperation:
        print("That is not a valid number.")
        return None
    if not amount.is_finite():
        print("That is not a valid number.")
        return None
    if amount != amount.quantize(Decimal("0.01")):
        print("Use at most 2 decimal places.")
        return None
    return amount


def find_member(name):
    """Look for a member ignoring upper/lower case. Returns the real name or None."""
    for m in members:
        if m.lower() == name.strip().lower():
            return m
    return None


def money(amount):
    """Show a Decimal with 2 decimal places."""
    return f"{amount:.2f}"


# ---------- the main actions ----------
def create_group():
    global weekly_amount
    if weekly_amount is not None:
        print("A group already exists.")
        return
    amount = read_amount(input("Weekly contribution (GHS): "))
    if amount is None:
        return
    if amount <= 0:
        print("The weekly contribution must be more than zero.")
        return
    weekly_amount = amount
    print("Group created. Weekly contribution is GHS", money(weekly_amount))


def add_member():
    if weekly_amount is None:
        print("Create the group first.")
        return
    if started:
        print("Cannot add members after the group has started.")
        return
    name = input("Member name or ID: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    if find_member(name) is not None:
        print("That member already exists.")
        return
    members.append(name)
    paid[name] = Decimal("0")
    print(name, "added.")


def record_payment():
    global started
    if weekly_amount is None:
        print("Create the group first.")
        return
    if len(members) < 2:
        print("Add at least 2 members first.")
        return
    if len(payouts) == len(members):
        print("The cycle is finished. Everyone has been paid.")
        return

    name = find_member(input("Member name: "))
    if name is None:
        print("Unknown member.")
        return

    amount = read_amount(input("Amount paid (GHS): "))
    if amount is None:
        return
    if amount <= 0:
        print("Amount must be more than zero.")
        return

    still_owes = weekly_amount - paid[name]
    if amount > still_owes:
        print(name, "only owes", money(still_owes), "this week. Payment rejected.")
        return

    paid[name] = paid[name] + amount
    started = True
    print("Payment recorded.", name, "now owes", money(weekly_amount - paid[name]))


def close_week():
    global week
    if weekly_amount is None:
        print("Create the group first.")
        return
    if len(members) < 2:
        print("Add at least 2 members first.")
        return
    if len(payouts) == len(members):
        print("The cycle is finished. Everyone has been paid.")
        return

    # check who has not paid in full
    someone_owes = False
    for m in members:
        owed = weekly_amount - paid[m]
        if owed > 0:
            print(m, "owes", money(owed))
            someone_owes = True

    if someone_owes:
        print("Week", week, "is NOT closed. No payout.")
        return

    # everyone paid, so pay the next person in order
    pot = weekly_amount * len(members)
    winner = members[len(payouts)]
    payouts.append((week, winner, pot))
    print("Week", week, "closed.", winner, "receives GHS", money(pot))

    if len(payouts) == len(members):
        print("Everyone has received the pot. The cycle is finished!")
    else:
        week = week + 1
        for m in members:
            paid[m] = Decimal("0")
        print("Week", week, "begins. Next to receive:", members[len(payouts)])


def show_report():
    if weekly_amount is None:
        print("Create the group first.")
        return
    print()
    print("------ REPORT ------")
    print("Weekly contribution: GHS", money(weekly_amount))
    print("Members:", len(members))

    if len(payouts) == len(members) and len(members) > 0:
        print("The cycle is finished.")
    else:
        print("Current week:", week)
        if len(members) > 0:
            print("Next to receive:", members[len(payouts)])
        print("Paid in full:")
        found = False
        for m in members:
            if paid[m] == weekly_amount:
                print("  ", m)
                found = True
        if not found:
            print("   nobody yet")
        print("Still owing:")
        found = False
        for m in members:
            owed = weekly_amount - paid[m]
            if owed > 0:
                print("  ", m, "owes", money(owed))
                found = True
        if not found:
            print("   nobody")

    print("Payout history:")
    if len(payouts) == 0:
        print("   none yet")
    for p in payouts:
        print("   Week", p[0], "-", p[1], "received GHS", money(p[2]))
    print("--------------------")
    print()


# ---------- the menu ----------
def main():
    while True:
        print("1. Create group")
        print("2. Add member")
        print("3. Record payment")
        print("4. Close week")
        print("5. Show report")
        print("6. Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            create_group()
        elif choice == "2":
            add_member()
        elif choice == "3":
            record_payment()
        elif choice == "4":
            close_week()
        elif choice == "5":
            show_report()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")
        print()


main()
