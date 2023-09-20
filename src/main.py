from extractor import wrap_formula

premise = ""
formulas = []

while premise != "0":
    premise = input("Digite uma premissa (ou 0 para sair): ")

    if premise != "0":
        formulas.append(wrap_formula(premise))

conclusion = input("Digite a conclusão: ")
formulas.append(wrap_formula(conclusion))

print(formulas)
