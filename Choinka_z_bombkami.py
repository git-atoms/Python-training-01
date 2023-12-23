def print_colored_christmas_tree(height):
    # Definicje kolorów
    GREEN = '\033[92m'  # Zielony dla liści choinki
    YELLOW = '\033[93m' # Żółty dla gwiazdek
    RESET = '\033[0m'   # Reset kolorów

    for i in range(height):
        # Tworzenie linii choinki
        line = ' ' * (height - i - 1) + '*' * (2 * i + 1)
        # Zamiana niektórych '*' na gwiazdki (bombki) i dodanie kolorów
        colored_line = ''
        for j in range(len(line)):
            if line[j] == '*':
                if i > 1 and j % 3 == 0:  # Warunek na gwiazdki
                    colored_line += YELLOW + '*' + RESET
                else:
                    colored_line += GREEN + '*' + RESET
            else:
                colored_line += line[j]
        print(colored_line)

    # Pień choinki (pozostaje czarny)
    for i in range(height // 3):
        print(' ' * (height - 2) + '***')

# Użyj tej funkcji, aby wydrukować kolorową choinkę o żądanej wysokości
print_colored_christmas_tree(10)
