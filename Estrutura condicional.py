hora: int

hora = int(input("digite uma hora do dia: "))

if hora < 12:
        print("Bom dia")
elif hora < 18:
        print("Boa tarde")
else:
        print("Boa Noite")
