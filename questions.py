import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario","/* Esto es un comentario */","-- Esto es un comentario","# Esto es un comentario",),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Seleccionar 3 preguntas aleatorias para el juego
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)
# Inicializo la variable de puntaje
user_points = float(0)
# El usuario deberá contestar 3 preguntas
for question, answers_options, correct_answers in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answers_options):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))
        # Se verifica si lo que ingreso el usuario es un entero
        if ( not user_answer.isdigit() ):
            print("Respuesta no valida")
            exit(1)
        # Al ser un entero se le resta 1 para que funcione en el rango de respuestas
        user_answer = int(user_answer) - 1
        # Se verifica que este en el rango de respuestas
        if ( user_answer < 0 ) or ( user_answer > 3 ):
            print("Respuesta no valida")
            exit(1)
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers:
            print("¡Correcto!")
            # Se suma 1 al puntaje
            user_points = user_points + 1
            break
        else:
            # Se resta 0.5 al puntaje
            user_points = user_points - 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers_options[correct_answers])
    # Se imprime un blanco al final de la pregunta
    print()
# Se imprime el puntaje
print("Su puntaje es ",user_points)