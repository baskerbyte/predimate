def draw_table(cols, rows):
    col_width = [max(len(col), max(len(row[i]) for row in rows)) for i, col in enumerate(cols)]

    header = " | ".join(f"{col:^{col_width[i]}}" for i, col in enumerate(cols))

    division = "\n" + "+".join("-" * len(element) for element in header.split("|")) + "\n"

    body = "\n".join(" | ".join(f"{cell:^{col_width[i]}}" for i, cell in enumerate(row)) for row in rows)

    return header + division + body
