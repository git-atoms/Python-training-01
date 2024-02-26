import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

def generate_word_cloud():
    folder_path = input("Podaj ścieżkę do folderu: ")
    # Znajdowanie pierwszego pliku tekstowego w folderze
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            break
    
    # Wczytanie tekstu z pliku
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()


    # Usunięcie znaków interpunkcyjnych
    text = re.sub(r'[^\w\s]', '', text)

    # Ustawienia chmury słów
    wordcloud = WordCloud(width=1920, height=1080, background_color='white').generate(text)

    # Ustawienia obrazu wyjściowego
    plt.figure(figsize=(16, 9), dpi=300)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Zapis do pliku PNG w podanym folderze
    output_path = os.path.join(folder_path, 'chmura_słów.png')
    plt.savefig(output_path, format='png')
    print(f"Chmura słów została zapisana jako 'chmura_słów.png' w folderze: {folder_path}")


generate_word_cloud()
