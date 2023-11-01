from texttable import Texttable

from src.data.encode import encode_expression
from src.cli.truth_table import generate_truth_table


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


def parse_input(item, prepositions, expressions):
    wrapped = encode_expression(item)

    if wrapped is None:
        quit(f"Argumento \"{item}\" inválido")

    if wrapped not in expressions:
        expressions.append(wrapped)

    for prep in list(filter(lambda char: char.isalpha() and char != 'v', item)):
        if prep not in prepositions:
            prepositions.append(prep.upper())


def get_input_list(prompt, repeat=True):
    prepositions, expressions = [], []

    while True:
        item = input(prompt)

        if item == "0":
            break

        parse_input(item, prepositions, expressions)

        if not repeat:
            break

    prepositions.sort()

    return prepositions, expressions


def main():
    print_main_header()

    while True:
        menu = get_menu_choice()

        if menu == 0:
            return

        (prepositions, premises) = get_input_list("Digite uma premissa (ou 0 para pular): ")
        (_, conclusion) = get_input_list("Digite a conclusão (ou 0 para pular): ", False)

        if menu == 1:
            generate_truth_table(prepositions, premises, conclusion)
        else:
            break


if __name__ == "__main__":
    main()
