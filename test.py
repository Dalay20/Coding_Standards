"""Sistema de gestión de calificaciones de estudiantes."""

class Student:
    """Representa a un estudiante con sus calificaciones, promedio y estado."""

    def __init__(self, student_id: str, name: str):
        """
        Inicializa un registro de estudiante con un ID y nombre.

        Args:
            student_id (str): Identificador único del estudiante.
            name (str): Nombre completo del estudiante.
        """
        if not student_id or not name:
            raise ValueError("El ID y el nombre del estudiante no pueden estar vacíos.")

        self.student_id = student_id
        self.name = name
        self.grades = []
        self.average = 0.0
        self.letter_grade = "N/A"
        self.status = "No calificado"
        self.honor_roll = False

    # ----------------------------------------------------------------------
    # Funcionalidades principales
    # ----------------------------------------------------------------------

    def add_grade(self, grade: float):
        """
        Agrega una calificación válida (0–100) al registro del estudiante.

        Args:
            grade (float): Calificación numérica a agregar.
        """
        if not isinstance(grade, (int, float)):
            print(f"Error: {grade} no es un número válido.")
            return
        if not 0 <= grade <= 100:
            print(f"Error: {grade} está fuera del rango permitido (0–100).")
            return

        self.grades.append(float(grade))
        self.update_status()

    def calc_average(self) -> float:
        """Calcula y devuelve el promedio de calificaciones del estudiante."""
        if not self.grades:
            return 0.0
        self.average = sum(self.grades) / len(self.grades)
        return self.average

    def determine_letter_grade(self) -> str:
        """Determina la calificación en letra (A–F) según el promedio."""
        avg = self.calc_average()
        if avg >= 90:
            self.letter_grade = "A"
        elif avg >= 80:
            self.letter_grade = "B"
        elif avg >= 70:
            self.letter_grade = "C"
        elif avg >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"
        return self.letter_grade

    def update_status(self):
        """Actualiza el estado de aprobación y honor del estudiante."""
        avg = self.calc_average()
        self.determine_letter_grade()
        self.status = "Aprobado" if avg >= 60 else "Reprobado"
        self.honor_roll = avg >= 90

    # ----------------------------------------------------------------------
    # Funcionalidades extendidas
    # ----------------------------------------------------------------------

    def remove_grade_by_index(self, index: int):
        """Elimina una calificación por índice, manejando errores."""
        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(f"Calificación {removed} eliminada en el índice {index}.")
            self.update_status()
        else:
            print(f"Error: índice {index} fuera de rango.")

    def remove_grade_by_value(self, value: float):
        """Elimina una calificación por valor, manejando errores."""
        try:
            self.grades.remove(value)
            print(f"Calificación {value} eliminada.")
            self.update_status()
        except ValueError:
            print(f"Error: la calificación {value} no se encuentra en la lista.")

    def generate_report(self) -> str:
        """Genera un reporte con los datos del estudiante."""
        self.update_status()
        report = (
            f"\nREPORTE DEL ESTUDIANTE\n"
            f"-----------------------------\n"
            f"ID: {self.student_id}\n"
            f"Nombre: {self.name}\n"
            f"Calificaciones: {self.grades}\n"
            f"Número de Calificaciones: {len(self.grades)}\n"
            f"Promedio: {self.average:.2f}\n"
            f"Calificación en Letra: {self.letter_grade}\n"
            f"Estado: {self.status}\n"
            f"Cuadro de Honor: {'Sí' if self.honor_roll else 'No'}\n"
        )
        return report


# ----------------------------------------------------------------------
# Ejemplo de uso
# ----------------------------------------------------------------------

def main():
    """Demostración del sistema."""
    try:
        student_a = Student("S001", "Alice Smith")
    except ValueError as e:
        print(e)
        return

    # Agregar calificaciones
    student_a.add_grade(95)
    student_a.add_grade(88.5)
    student_a.add_grade(76)
    student_a.add_grade(-5)      # inválido
    student_a.add_grade("A+")    # inválido

    # Eliminar calificaciones
    student_a.remove_grade_by_index(2)
    student_a.remove_grade_by_value(50)  # inexistente

    # Generar reporte
    print(student_a.generate_report())


if __name__ == "__main__":
    main()
