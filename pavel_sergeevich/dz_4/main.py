import util

txt_raw = util.load_fl("book.txt")
print("Загрузка книги. Количество символов: " + str(len(txt_raw)))

txt_tk = util.tokenizer(txt_raw)
print("Количество токенов: " + str(len(txt_tk)))
# print(txt_tk)

txt_tk_set = set(txt_tk)
print("Количество уникальных токенов (слов): " + str(len(txt_tk_set)))

word = txt_tk[6858]
v_cnt, c_cnt = util.get_type_of_letter(word)
print("Количество гластных букв в слове \"" + word + "\" " + str(v_cnt) + ", а согласных - " + str(c_cnt))

general_v_cnt = 0
general_c_cnt = 0
for w in txt_tk:
    v_cnt, c_cnt = util.get_type_of_letter(w)
    general_v_cnt += v_cnt
    general_c_cnt += c_cnt
print("Количество гластных букв всех токенов " + str(general_v_cnt) + ", а согласных - " + str(general_c_cnt))

sentence = util.sentence_tokenizer(txt_raw)
print("Количество предложений в тексте " + str(len(sentence)))

sentence_words = []
for sn in sentence:
    words_sn = util.tokenizer(sn)
    sentence_words.append(len(words_sn))

print("Максимальное количество слов в предложени составляет " + str(max(sentence_words)) + ". Предложение ниже:")
print(sentence[sentence_words.index(max(sentence_words))])


"""
Out:
Загрузка книги. Количество символов: 57929
Количество токенов: 8616
Количество уникальных токенов (слов): 3443
Количество гластных букв в слове "туннеля" 3, а согласных - 4
Количество гластных букв всех токенов 18716, а согласных - 26874
Количество предложений в тексте 875
Максимальное количество слов в предложени составляет 54
    старенькое обессиленное уже не в состоянии растопить вечные льды и снега за короткое лето опалить яростным взглядом
    скалы заставить захлебнуться пропасти и расщелины в талой влаге родить в них дикие безумные реки уносящие вдаль обломки
    скал куски льда выворачивающие в своем стремительном беге огромные валуны и швыряющие их в бурлящем потоке словно щепки


"""