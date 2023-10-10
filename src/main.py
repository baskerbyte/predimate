from data.encode import encode_expression
from truth_table.draw import draw_table
from truth_table.table import generate_combinations, evaluate_expressions, extract_expressions, table_type


def print_main_header():
    header = """
      _____              _ _                 _       
     |  __ \            | (_)               | |      
     | |__) | __ ___  __| |_ _ __ ___   __ _| |_ ___ 
     |  ___/ '__/ _ \/ _` | | '_ ` _ \ / _` | __/ _ \\
     | |   | | |  __/ (_| | | | | | | | (_| | ||  __/
     |_|   |_|  \___|\__,_|_|_| |_| |_|\__,_|\__\___|
    """

    print(header)


def get_menu_choice():
    print("\nMenu Principal:")
    print("1 - Tabela Verdade")
    print("0 - Sair\n")

    return int(input("Escolha uma opção: "))


def get_input_list(prompt):
    items = []

    while True:
        item = input(prompt)

        if item == "0":
            break

        wrapped = encode_expression(item)

        if wrapped is None:
            quit(f"Argumento \"{item}\" inválido")

        items.append(wrapped)
    return items


def map_expressions(args, conclusion):
    expressions = []
    premises = []

    if conclusion is not None and conclusion != "0":
        args.append(encode_expression(conclusion))

    for arg in args:
        extracted = extract_expressions(arg)

        for expr in extracted:
            if expr not in expressions and not isinstance(expr, str):
                expressions.append(expr)

            if expr not in premises and isinstance(expr, str):
                premises.append(expr)

    premises.sort()

    return premises, expressions


def main():
    print_main_header()

    while True:
        menu = get_menu_choice()

        if menu != 0:
            args = get_input_list("Digite uma premissa (ou 0 para pular): ")
            conclusion = input("Digite a conclusão (ou 0 para pular): ")

            if menu == 1:
                premises, expressions = map_expressions(args, conclusion)
                combinations = generate_combinations(premises)
                rows = evaluate_expressions((premises, expressions), combinations)

                header = premises + list(map(lambda x: str(x), expressions))
                results = [['V' if value else 'F' for value in row] for row in rows]

                print(f"\n{draw_table(header, results)}")
                print(f'Tipo de tabela: {table_type(rows)}')
        else:
            break


if __name__ == "__main__":
    main()
