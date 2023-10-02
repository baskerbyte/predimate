from src.data.encode import wrap_formula
from src.truth_table.draw import draw_table
from src.truth_table.table import generate_combinations, evaluate_expressions, extract_expressions

print("Menu Principal:")
print("1 - Tabela Verdade")
print("0 - Sair")

menu = int(input("Escolha uma opção: "))

args = []
conclusion = None

while True:
    premise = input("Digite uma premissa (ou 0 para pular): ")

    if premise == "0":
        conclusion_ipt = input("Digite a conclusão: ")

        if conclusion_ipt != "0":
            conclusion = conclusion_ipt

        break

    args.append(premise)

formulas = []

for arg in args:
    wrapped = wrap_formula(arg)

    if wrapped is None:
        quit(f"Argumento \"{arg}\" inválido")

    formulas.append(wrap_formula(arg))

if conclusion is not None:
    conclusion = wrap_formula(conclusion)

if menu == 1:
    expressions = []
    premises = []

    for formula in formulas:
        extracted = extract_expressions(formula)

        for expr in extracted:
            if expr not in expressions and not isinstance(expr, str):
                expressions.append(expr)

            if expr not in premises and isinstance(expr, str):
                premises.append(expr)

    if conclusion is not None and not isinstance(conclusion, str):
        expressions.extend(list(filter(lambda x: not isinstance(x, str), extract_expressions(conclusion))))

    premises.sort()

    combinations = generate_combinations(premises)
    rows = evaluate_expressions((premises, expressions), combinations)

    print(
        draw_table(
            premises + list(map(lambda x: str(x), expressions)),
            [['V' if value else 'F' for value in row] for row in rows]
        )
    )
