idade: int
salario: float
nome: str
sexo: str

idade = 25
salario = 5800.5
altura = 1.74
sexo = 'Masculino'
nome = "Jason"

print(f"O Funcionario {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")
print("o Funcionario {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format (nome, sexo, salario, idade))