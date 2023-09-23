from src.data.encode import wrap_formula
from src.data.decode import interpret_formula

args = []

while True:
    premise = input("Digite uma premissa (ou 0 para sair): ")

    if premise == "0":
        break

    args.append(premise)

conclusion = input("Digite a conclusão: ")
formulas = []

args.append(conclusion)

for arg in args:
    wraped = wrap_formula(arg)

    if wraped is None:
        quit(f"Argumento \"{arg}\" inválido")

    formulas.append(wrap_formula(arg))

print(repr(formulas))

unwraped = []

for formula in formulas:
    unwraped.append(interpret_formula(formula))

print(unwraped)
