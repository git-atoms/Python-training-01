def print_christmas_tree(height):
    for i in range(height):
        # Tworzenie linii choinki
        line = ' ' * (height - i - 1) + '*' * (2 * i + 1)
        # Zamiana niektórych '*' na gwiazdki (bombki)
        if i > 1:
            line = list(line)
            for j in range(1, 2 * i, 2):
                if j % 4 == 0:  # Można zmienić warunek, aby zmienić rozmieszczenie gwiazdek
                    line[j] = '*'
            line = ''.join(line)
        print(line)

    # Pień choinki
    for i in range(height // 3):
        print(' ' * (height - 2) + '***')

# Użyj tej funkcji, aby wydrukować choinkę o żądanej wysokości
print_christmas_tree(10)
