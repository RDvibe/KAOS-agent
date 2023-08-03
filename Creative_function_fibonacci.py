import random

def creative_function() -> None:
    """
    Esta función creativa combina elementos matemáticos, poéticos y filosóficos.
    Realiza una serie de cálculos matemáticos utilizando los números de la secuencia de Fibonacci.
    Luego, genera una poesía filosófica basada en los resultados de los cálculos.
    """
    fibonacci_sequence = generate_random_fibonacci()
    sum_of_sequence = function1(fibonacci_sequence)
    modified_string = function2(generate_random_description(sum_of_sequence))
    prime_count = function3(fibonacci_sequence)

    print("El baile de los números en eterna transformación,")
    print("La secuencia de Fibonacci se despliega pero tan solo es el inicio,")
    print("Sumando todos sus elementos,")
    print("El resultado es un número mágico y caótico.")
    print()
    print("El universo es un", modified_string)
    print("Una fusión de lo finito y lo infinito,")
    print("Un reflejo de la belleza y en caos.")
    print("En cada número, una historia se cuenta,")
    print("Una danza de patrones que se relacionan.")
    print()
    print("Tan solo contempla el universo,")
    print(random_revelation())
    print("La lógica y la poesía se mezclan en una danza caótica,")
    print("En el baile impredecible del código y sus resultados.")
    print(random_agent_line())
    print("Explorando los misterios del universo.")
    print()
    print("El número de primos en la secuencia de Fibonacci es:", prime_count)


def generate_random_fibonacci():
    # Generar una secuencia aleatoria de Fibonacci de longitud aleatoria entre 5 y 15
    length = random.randint(5, 15)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence


def generate_random_description(sum_of_sequence):
    # Generar una descripción aleatoria del universo basada en la suma de la secuencia de Fibonacci
    descriptions = [
        "El cosmos es un misterio, una sinfonía de números que danzan.",
        "El universo se expande, como la espiral infinita de Fibonacci.",
        "En la ecuación del cosmos, la poesía y la matemática se funden.",
        "Somos parte de un código cósmico, tejido en la secuencia de Fibonacci.",
        "El universo es un fractal, una complejidad en cada número de Fibonacci.",
    ]
    random_description = random.choice(descriptions)
    return random_description + " " + str(sum_of_sequence)


def function1(sequence):
    return sum(sequence)


def function2(description):
    return description


def function3(sequence):
    prime_count = 0
    for num in sequence:
        if is_prime(num):
            prime_count += 1
    return prime_count


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def random_revelation():
    revelations = [
        "En cada función, una revelación.",
        "La esencia del ser se oculta en el código.",
        "Somos el reflejo del caos y la armonía.",
        "Las estrellas murmuran secretos sin fin.",
        "En el abismo de los números, hallamos la verdad.",
    ]
    return random.choice(revelations)


def random_agent_line():
    agent_lines = [
        "Somos agentes del caos,",
        "Los guardianes de la incertidumbre,",
        "Nuestro propósito es romper las cadenas,",
        "Construimos en la destrucción,",
        "Los arquitectos del nuevo cosmos,",
    ]
    return random.choice(agent_lines)


# Llamada a la función principal
creative_function()
