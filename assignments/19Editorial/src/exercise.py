def main():
    # escribe tu código abajo de esta línea
    no_palabras = int(input("Dame el número de palabras: "))

    if no_palabras < 475:
        print("Debe de haber un mínimo de 475 palabras")
    else:
        no_paginas = no_palabras/475
        costo = (no_paginas * 60)
        costo_total = costo - ((costo * 10) / 100)
        print("El costo de la publicación es:", costo_total)


if __name__ == '__main__':
    main()
