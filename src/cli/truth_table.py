from texttable import Texttable

from src.truth_table.table import table_type, generate_combinations, evaluate_expressions, is_valid


def create_text_table(header, rows):
    table = Texttable()
    table.set_cols_align("c" * len(header))
    table.set_max_width(0)
    table.add_rows([header] + rows)

    return table


def generate_truth_table(prepositions, premises, conclusion):
    expressions = premises + conclusion
    combinations = generate_combinations(prepositions)
    values = evaluate_expressions(prepositions, expressions, combinations)

    expanded_expressions = values.keys()

    # Orients values in rows
    rows = list(zip(*values.values()))
    header = list(map(lambda x: str(x), expanded_expressions))
    results = [['V' if value else 'F' for value in row] for row in rows]

    print(create_text_table(header, results).draw())
    print(f'Tipo de tabela: {table_type(rows)}')

    if conclusion:
        print(f'{"O argumento é válido" if is_valid(values, premises, conclusion[0]) else "O argumento é inválido"}')
