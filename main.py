from factory import NotificadorFactory


def main() -> None:
    print("=================================================")
    print("   SISTEMA DE NOTIFICACIONES (FACTORY METHOD)   ")
    print("=================================================")
    print("Canales disponibles: email (real), sms, whatsapp")
    print("Escribe 'salir' para terminar el programa.\n")

    while True:
        canal = input("Ingrese el canal deseado: ").strip()

        if canal.lower() == "salir":
            print("\nFinalizando el sistema. ¡Hasta luego!")
            break

        # Validación de entrada vacía (Clean Code)
        if not canal:
            continue

        destinatario = ""
        if canal.lower() == "email":
            destinatario = input("Ingrese el correo destino: ").strip()

        mensaje = input(f"Ingrese el mensaje para [{canal}]: ").strip()

        try:
            # -----------------------------------------------------------------
            # Entregable 3 & 4 (Semana 3): Polimorfismo y desacoplamiento
            # El cliente solicita el objeto y lo usa sin conocer su clase concreta.
            # -----------------------------------------------------------------
            notificador = NotificadorFactory.crear_notificador(canal)
            notificador.enviar(mensaje, destinatario)
            print(">> Notificación procesada exitosamente.\n")

        except Exception as error:
            # Captura y muestra errores sin interrumpir la ejecución del programa
            print(f"[ERROR]: {error}\n")


if __name__ == "__main__":
    main()