product_names = input_data["product_names"]
another_column = input_data["another_column"]
primary_colours = input_data["primary_colours"]

# Ujistíme se, že vstupní data jsou seznamy, jinak je rozdělíme podle čárky
if isinstance(product_names, str):
    product_names = product_names.split(",")
if isinstance(another_column, str):
    another_column = another_column.split(",")
if isinstance(primary_colours, str):
    primary_colours = primary_colours.split(",")

# Ověření, že všechny seznamy mají stejnou délku
min_length = min(len(product_names), len(another_column), len(primary_colours))
product_names = product_names[:min_length]
another_column = another_column[:min_length]
primary_colours = primary_colours[:min_length]

full_name_rows = []

for p, mid, c in zip(product_names, another_column, primary_colours):
    # Ošetření prázdných hodnot
    p = p.strip() if p else "N/A"
    mid = mid.strip() if mid else "N/A"
    c = c.strip() if c else "N/A"

    # Formátování třetího sloupce (primary_colours) - správné spojení slov
    c_formatted = "/ ".join([word.strip().title() for word in c.split("/")])

    # Pokud another_column obsahuje "Shoes", spojíme pouze product_names a primary_colours
    if "Shoes" in mid:
        full_name_value = f"{p} {c_formatted}"
    else:
        full_name_value = f"{p} {mid} {c_formatted}"

    full_name_rows.append(full_name_value)

return {"full_name": full_name_rows}

