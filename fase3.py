# ============================================================
# HUYENDO DEL PROFESOR
# Aplicación de POO: Encapsulamiento, Herencia,
# Polimorfismo y Composición
# ============================================================


# ---------------- CLASE BASE ----------------

class Jugador:
    """Clase base para todos los jugadores."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion_total = 0
        self.nivel_actual = 1
        self.vidas = 3

        # Atributo privado para encapsulamiento
        self.__record_maximo = 0

    # Método público para acceder al atributo privado
    def obtener_record(self):
        return self.__record_maximo

    # Método que puede ser modificado por polimorfismo
    def actualizar_puntuacion(self, puntos):
        """Suma puntos y actualiza el récord."""

        self.puntuacion_total += puntos

        if self.puntuacion_total > self.__record_maximo:
            self.__record_maximo = self.puntuacion_total
            print(f"🏆 {self.nombre} consiguió un nuevo récord: "
                  f"{self.__record_maximo} puntos.")
        else:
            print(f"⭐ {self.nombre} suma {puntos} puntos.")

    def perder_vida(self):
        """El jugador pierde una vida."""

        self.vidas -= 1

        print(f"💔 {self.nombre} perdió una vida.")
        print(f"❤️ Vidas restantes: {self.vidas}")

    def mostrar_resumen(self):
        print("\n========== RESUMEN ==========")
        print(f"Jugador: {self.nombre}")
        print(f"Nivel: {self.nivel_actual}")
        print(f"Vidas: {self.vidas}")
        print(f"Puntos: {self.puntuacion_total}")
        print(f"Récord: {self.__record_maximo}")
        print("=============================")


# ---------------- HERENCIA Y POLIMORFISMO ----------------

class JugadorVIP(Jugador):
    """Jugador especial que recibe más puntos."""

    def __init__(self, nombre, multiplicador_bono=1.5):
        super().__init__(nombre)
        self.multiplicador_bono = multiplicador_bono

        print(f"👑 {self.nombre} es un jugador VIP.")

    # Sobreescritura del método
    def actualizar_puntuacion(self, puntos):
        """Aplica un multiplicador a los puntos."""

        puntos_bonificados = puntos * self.multiplicador_bono

        print(
            f"💎 Bono VIP: {puntos} x "
            f"{self.multiplicador_bono} = "
            f"{puntos_bonificados}"
        )

        # Llama al método de la clase padre
        super().actualizar_puntuacion(puntos_bonificados)


# ---------------- COMPOSICIÓN ----------------

class Partida:
    """Gestiona una partida y contiene un objeto Jugador."""

    def __init__(self, jugador):
        # Composición: Partida tiene un Jugador
        self.jugador = jugador
        self.regalos_obtenidos = []

        print(
            f"\n🎮 INICIO DE PARTIDA para "
            f"{self.jugador.nombre}"
        )

    def completar_mision(self, puntos, mision):
        """El jugador completa una misión."""

        print(f"\n🎒 MISIÓN: {mision}")
        print("✅ ¡Misión completada!")

        self.jugador.actualizar_puntuacion(puntos)

    def profesor_atrapa(self):
        """El profesor atrapa al jugador."""

        print("\n👨‍🏫 ¡EL PROFESOR TE ATRAPÓ!")

        self.jugador.perder_vida()

        if self.jugador.vidas > 0:
            print("🔄 Debes repetir la misión.")
        else:
            print("💀 GAME OVER.")

    def usar_poder(self, poder):
        """Utiliza un poder especial."""

        print(f"\n⚡ PODER ACTIVADO: {poder}")

        if poder == "Super velocidad":
            print("🏃 ¡Escapaste rápidamente del profesor!")
            self.jugador.actualizar_puntuacion(30)

        elif poder == "Libro mágico":
            print("📖 ¡El libro mágico te ayudó!")
            self.jugador.actualizar_puntuacion(40)

        elif poder == "Super inteligencia":
            print("🧠 ¡Resolviste el problema!")
            self.jugador.actualizar_puntuacion(50)

    def subir_nivel_y_recompensar(self):
        """Aumenta el nivel y entrega una recompensa."""

        self.jugador.nivel_actual += 1

        recompensa_puntos = self.jugador.nivel_actual * 50

        recompensa_regalo = (
            f"Medalla del Nivel {self.jugador.nivel_actual}"
        )

        self.jugador.actualizar_puntuacion(
            recompensa_puntos
        )

        self.regalos_obtenidos.append(recompensa_regalo)

        print(
            f"\n🎉 ¡FELICIDADES! "
            f"{self.jugador.nombre} subió al "
            f"NIVEL {self.jugador.nivel_actual}."
        )

        print(
            f"🎁 Recibiste {recompensa_puntos} puntos "
            f"extra."
        )

        print(
            f"🏅 Recompensa: {recompensa_regalo}"
        )

    def pregunta_final(self):
        """Pregunta final del juego."""

        print("\n================================")
        print("🏁 PREGUNTA FINAL")
        print("================================")

        print(
            "¿Qué debes hacer si el profesor "
            "te atrapa?"
        )

        print("1. Repetir la misión")
        print("2. Abandonar el juego")

        respuesta = input("Selecciona una opción: ")

        if respuesta == "1":
            print("\n✅ ¡Respuesta correcta!")
            self.jugador.actualizar_puntuacion(100)

            print("🏆 ¡VICTORIA!")
            print("🎓 Ganaste el Diploma Legendario.")

            self.regalos_obtenidos.append(
                "Diploma Legendario"
            )

        else:
            print("\n❌ Respuesta incorrecta.")
            print("🔄 Debes repetir la misión.")

    def finalizar_partida(self):
        """Muestra el resumen final."""

        print("\n================================")
        print("🏆 RESUMEN DE PARTIDA")
        print("================================")

        self.jugador.mostrar_resumen()

        print(
            f"🎁 Regalos obtenidos: "
            f"{self.regalos_obtenidos}"
        )

        print("================================")


# ============================================================
# EJECUCIÓN DEL JUEGO
# ============================================================

print("==============================================")
print("       🏃 HUYENDO DEL PROFESOR 🏃")
print("==============================================")

nombre = input("Escribe tu nombre: ")

print("\nElige tu personaje:")
print("1. Jugador normal")
print("2. Jugador VIP")

tipo = input("Selecciona una opción: ")


# Creamos el jugador según la elección
if tipo == "2":
    jugador = JugadorVIP(nombre)
else:
    jugador = Jugador(nombre)


# Composición: creamos una partida
partida = Partida(jugador)


# ---------------- NIVEL 1 ----------------

print("\n========== NIVEL 1 ==========")

partida.completar_mision(
    100,
    "Recoger las herramientas"
)


# El jugador usa un poder
partida.usar_poder("Super velocidad")


# ---------------- NIVEL 2 ----------------

print("\n========== NIVEL 2 ==========")

partida.subir_nivel_y_recompensar()

partida.completar_mision(
    150,
    "Encontrar el libro mágico"
)


# ---------------- NIVEL 3 ----------------

print("\n========== NIVEL 3 ==========")

partida.subir_nivel_y_recompensar()

partida.completar_mision(
    200,
    "Completar el examen sorpresa"
)


# ---------------- NIVEL FINAL ----------------

print("\n========== NIVEL FINAL ==========")

partida.subir_nivel_y_recompensar()

partida.pregunta_final()


# ---------------- FINAL ----------------

partida.finalizar_partida()