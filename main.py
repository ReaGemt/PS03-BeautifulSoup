import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаем объект Translator
translator = Translator()


# Создаем функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаем объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и его определение на русский
        translated_word = translator.translate(english_words, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        # Чтобы программа возвращала словарь
        return {
            "english_words": translated_word,
            "word_definition": translated_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Создаем функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаем функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user.lower() == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаем возможность закончить игру
        play_again = input("Хотите сыграть еще раз? да/нет")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break


word_game()
