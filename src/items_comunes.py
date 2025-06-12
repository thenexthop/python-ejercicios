"""
    Para practicar list comprehensions y lectura de archivos de texto.
    ------------------------------------------------------------------
    Compara el contenido de dos archivos y crea una lista con los numeros enteros que
    se encuentren en ambos archivos.
"""
lineas_file1 = []
lineas_file2 = []
with open("file1.txt", "r") as file1:
    lineas_file1 = [int(line.rstrip()) for line in file1]
    print(lineas_file1)
    
with open("file2.txt", "r") as file2:
    lineas_file2 = [int(line.rstrip()) for line in file2]
    print(lineas_file2)

lista_comunes = [x for x in lineas_file1 if x in lineas_file2]
print("Números comunes:", lista_comunes)
