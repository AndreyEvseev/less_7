
def number_syllables(user_str):
    count_syllables = 0
    for elem in user_str:
        if elem in vowels:
            count_syllables += 1
    return count_syllables

def rhythm_analysis(user_str):
    work_list = user_str.split()
    count_syllables = number_syllables(work_list[0])
    for i in range(1, len(work_list)):
        if count_syllables != number_syllables(work_list[i]):
            return res_false
    return res_true


vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
res_true = 'Парам пам-пам'
res_false = 'Пам парам'

poem = input('Введите своё стихотворение. Каждое стихотворение состоит из фраз. '
             'Фразы в стихотворении разделяются пробелом. Слова в фразах разделяются дефисом.\n')
print(rhythm_analysis(poem))


