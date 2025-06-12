"""
    Para practicar dictionary comprehensions.
    -------------------------------------------
    Dado un diccionario con temperaturas en celsius, crea un nuevo diccionario con esas
    temperaturas en farenheit.
"""

temp_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

temp_f = { day: (celsius*9/5)+32 for (day, celsius) in temp_c.items() }

print(temp_f)