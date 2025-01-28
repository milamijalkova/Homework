def calculate_net_salary():
    try:
        gross = float(input("Enter the gross salary: "))
        children = int(input("Enter the number of children: "))

        if gross < 0 or children < 0:
            raise ValueError("Gross salary and number of children must be non-negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    if gross < 2000:
        child_tax_cut = 0.01 * children
    else:
        child_tax_cut = 0.005 * children

    effective_tax_rate = max(tax_rate - child_tax_cut, 0)

    net_salary = gross * (1 - effective_tax_rate)

    print(f"Net salary: {net_salary:.2f}")


calculate_net_salary()