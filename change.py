def change():
    expense = 23.75
    money = 100
    change = money - expense
    print(f"Ingresar gasto:\n23.75\nDinero recibido\n100\n\nVuelto\n\nPesos:\n{int(change)}\nCentavos:\n{int((change - int(change))*100)}")
change()
