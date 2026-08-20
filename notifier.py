from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# Concepto Semana 1: Interfaz / Clase Abstracta (Contrato base común)
# Define qué debe hacer cada notificador sin acoplar la implementación.
# -------------------------------------------------------------------------
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass

# -------------------------------------------------------------------------
# Entregable 1 (Semana 3): Identificar clases concretas
# Cada clase implementa el contrato con su propia responsabilidad única (SOLID).
# -------------------------------------------------------------------------
class NotificadorEmail(Notificador):
    def enviar(self, mensaje: str) -> None:
        print(f"[EMAIL] Enviando correo: {mensaje}")

class NotificadorSMS(Notificador):
    def enviar(self, mensaje: str) -> None:
        print(f"[SMS] Enviando SMS: {mensaje}")

# Criterio de evaluación (Semana 3): Extensión con bajo impacto (WhatsApp)
class NotificadorWhatsApp(Notificador):
    def enviar(self, mensaje: str) -> None:
        print(f"[WHATSAPP] Enviando mensaje: {mensaje}")
