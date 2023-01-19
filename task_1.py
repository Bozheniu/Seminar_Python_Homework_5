"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""

text = 'Где-то лето с ночи до рассвета, а может быть и нет, вот так'
print(f'Исходный текст:\n {text}')

def delete_words(my_text):
    my_text = list(filter(lambda x: 'а' not in x, my_text.split()))
    my_text = list(filter(lambda x: 'б' not in x, my_text))
    my_text = list(filter(lambda x: 'в' not in x, my_text))
    return " ".join(my_text)

print(f'Текст без слов с "абв":\n {delete_words(text)}')
