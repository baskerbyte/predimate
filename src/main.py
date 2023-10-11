from data.encode import encode_expression
from truth_table.draw import draw_table
from truth_table.table import generate_combinations, evaluate_expressions, table_type


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


def parse_input(item, prepositions, expressions,):
    wrapped = encode_expression(item)

    if wrapped is None:
        quit(f"Argumento \"{item}\" inválido")

    if wrapped not in expressions:
        expressions.append(wrapped)

    for prep in list(filter(lambda char: char.isalpha() and char != 'v', item)):
        if prep not in prepositions:
            prepositions.append(prep.upper())


def get_input_list(prompt, prepositions, expressions, repeat=True):
    if repeat:
        while True:
            item = input(prompt)

            if item == "0":
                break

            parse_input(item, prepositions, expressions)
    else:
        item = input(prompt)

        if item == "0":
            return

        parse_input(item, prepositions, expressions)
    prepositions.sort()


def main():
    print_main_header()

    while True:
        menu = get_menu_choice()

        if menu != 0:
            prepositions = []
            expressions = []

            get_input_list("Digite uma premissa (ou 0 para pular): ", prepositions, expressions,)
            get_input_list("Digite a conclusão (ou 0 para pular): ", prepositions, expressions, False)

            if menu == 1:
                combinations = generate_combinations(prepositions)
                values = evaluate_expressions(prepositions, expressions, combinations)
                expanded_expressions = [result.pop(0) for result in values]

                rows = list(zip(*values))
                rows = [list(combinations[i]) + list(rows[i]) for i in range(len(rows))] if rows else combinations

                header = prepositions + list(map(lambda x: str(x), expanded_expressions))
                results = [['V' if value else 'F' for value in row] for row in rows]

                print(f"\n{draw_table(header, results)}")
                print(f'Tipo de tabela: {table_type(rows)}')
        else:
            break


if __name__ == "__main__":
    main()
