from factory import NotificadorFactory

def main() -> None:
    print("==========================================")
    print("   SISTEMA DE NOTIFICACIONES DINÁMICO    ")
    print("==========================================")
    print("Canales disponibles: email, sms, whatsapp")
    print("Escribe 'salir' para terminar el programa.\n")

    while True:
        canal = input("Ingrese el canal de envío deseado: ").strip()

        if canal.lower() == "salir":
            print("\nFinalizando el sistema. ¡Hasta luego!")
            break

        # Validación de entrada vacía (Código Limpio: evitar procesar datos nulos)
        if not canal:
            print("Por favor, ingrese un canal válido.\n")
            continue

        mensaje = input(f"Ingrese el mensaje a enviar por [{canal}]: ").strip()

        try:
            # -----------------------------------------------------------------
            # Entregable 3 (Semana 3): Usar el objeto sin conocer su clase exacta
            # El cliente solo le pide a la fábrica el objeto correspondiente.
            # -----------------------------------------------------------------
            notificador = NotificadorFactory.crear_notificador(canal)

            # Entregable 4 / Polimorfismo: Se ejecuta .enviar() de forma genérica
            notificador.enviar(mensaje)
            print(">> Notificación procesada exitosamente.\n")

        except ValueError as error:
            # Manejo de excepciones para entradas no válidas
            print(f"[ERROR]: {error}\n")

if __name__ == "__main__":
    main()