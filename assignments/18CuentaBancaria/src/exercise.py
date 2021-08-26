def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingreso = float(input("Dame los ingresos: "))
    egreso = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))

    saldo_bruto = (saldo + ingreso - egreso - (cheques * 13))
    saldo_final = saldo_bruto - ((saldo_bruto * 7.5) / 100)

    print("El saldo final de la cuenta es:", saldo_final)

if __name__ == '__main__':
    main()
