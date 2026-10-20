def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formatea el nombre completo de una persona eliminando espacios sobrantes
    y capitalizando correctamente cada palabra.

    :param nombre: Nombre de la persona (puede ser compuesto)
    :param apellido1: Primer apellido
    :param apellido2: Segundo apellido
    :return: Cadena con el nombre completo correctamente formateado
    """
    nombre_formateado = nombre.strip().title()
    apellido1_formateado = apellido1.strip().title()
    apellido2_formateado = apellido2.strip().title()

    return f"{nombre_formateado} {apellido1_formateado} {apellido2_formateado}"


def main() -> None:
    nombre: str = input()
    apellido1: str = input()
    apellido2: str = input()

    nombre_completo: str = formatear_nombre(nombre, apellido1, apellido2)
    print(nombre_completo)


if __name__ == "__main__":
    main()