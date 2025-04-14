product_names = input_data.get("product_names", [])
another_column = input_data.get("another_column", [])

# Ujistíme se, že vstupní data jsou seznamy, jinak je převedeme
if isinstance(product_names, str):
    product_names = product_names.split(",")
if isinstance(another_column, str):
    another_column = another_column.split(",")

# Ověření, že všechny seznamy mají stejnou délku
max_length = max(len(product_names), len(another_column))

# Doplníme chybějící hodnoty prázdným textem, aby měly seznamy stejnou délku
product_names += [""] * (max_length - len(product_names))
another_column += [""] * (max_length - len(another_column))

name_rows = []

for p, mid in zip(product_names, another_column):
    # Ošetření prázdných hodnot
    p = p.strip() if p else "N/A"
    mid = mid.strip() if mid else "N/A"

    # Pokud another_column obsahuje "Shoes", vrátíme jen product_names
    if "Shoes" in mid:
        name_value = p
    else:
        name_value = f"{p} {mid}"

    name_rows.append(name_value)