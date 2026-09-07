import sys

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
        return 0
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo {file_path}.")
        return 0

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Uso: python word_counter.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    word_count = count_words(file_path)
    print(f"El archivo contiene {word_count} palabras.")