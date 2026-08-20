from notifier import Notificador, NotificadorEmail, NotificadorSMS, NotificadorWhatsApp


# -------------------------------------------------------------------------
# Entregable 2 (Semana 3): Crear una función fábrica (Factory Method)
# Objetivo: Centralizar la creación y encapsular las condiciones if/elif,
# evitando que los condicionales se dispersen por el resto del sistema.
# -------------------------------------------------------------------------
class NotificadorFactory:
    @staticmethod
    def crear_notificador(tipo: str) -> Notificador:
        tipo_normalizado = tipo.strip().lower()

        # La fábrica decide qué clase concreta instanciar según el parámetro
        if tipo_normalizado == "email":
            return NotificadorEmail()
        elif tipo_normalizado == "sms":
            return NotificadorSMS()
        elif tipo_normalizado == "whatsapp":
            return NotificadorWhatsApp()
        else:
            # Control de entradas inválidas sin romper el flujo del cliente
            raise ValueError(f"Tipo de notificador no válido: {tipo}")