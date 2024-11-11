# Homework 03
<hr>

## Задание
1. Загрузить файл длиной не менее 2000 символов.
2. Составить программу, которая считает число уникальных слов в тексте (без критерия схожести)
3. Составить программу, которая считает число гласных и согласных букв.
4. Составить программу, которая считает число предложений, их длину и число (количество) раз использования каждого слова в тексте (с критерием схожести, критерий схожести слов выбрать самостоятельно, например, spacy (en_core_web_sm) или расстояние Левенштейна).
5. Вывести 10 наиболее часто встречаемых слов.
<hr>


## Этапы выполнения работы
Для решения поставленной задачи необходимо реализовать следующие этапы:
- [ ] разработать программный код (здесь и далее - функцию), реализующую считывание данных из заданного файла;
- [ ] разработать функцию, которая осуществляет 'подготовку' текста для последующей работы с отдельными словами (удаление знаков препинания, переносов и др.);
- [ ] разработать функцию, которая преобразует текст (str) в список/множество (list/set) слов (для удобства последующей обработки);
- [ ] разработать функцию, которая подсчитывает число гласных и согласных букв в тексте;
- [ ] разработать функцию, которая подсчитывает число предложений в тексте и их длину;
- [ ] разработать функцию подсчета частоты встречаемости слов в тексте (с учетом критерия схожести). В качестве критерия схожести будем использовать расстояние Левенштейна;
- [ ] разработать функцию, которая возвращает пользователю 10 наиболее часто встречаемых слов в тексте;
- [ ] разработать функцию, связывающую описанные выше функции в единый программный код.
<hr>

## Структура репозитория
Структура проекта `HW_03` имеет следующий вид:
+ в каталоге **`data`** содержатся файлы **`.txt`** с исходным текстом для обработки;
+ в каталоге **`src`** содержатся файлы **`.py`** с исходным кодом:
    * в файле **`settings.py`** собраны импортируемые константы;
    * в файле **`hw_03.py`** находится основной код программы;
    * в файле **`hw_03_spacy.ipynd`** находится код программы, который использует готовую библиотеку `spacy` для решения данной задачи;
+ в файле **`requirements.txt`** содержится список подключаемых библиотек.
<hr>

## Выполнение программы
Для запуска программы необходимо выполнить:
```
python.exe -m pip install -r .\requirements.txt
python.exe .\hw_03.py
```
<hr>

## Описание работы программы
Ниже приведен листинг функции **`main`** файла **`hw_03.py`**.

1. -[x] Считываем данные (текст) из файла:
```
# 1) Считываем данные в файл
f = "../data/test_data_01.txt"
test_data = read_data(f)
print(f"1. Данные файла '{f}' успешно импортированы. Полученный текст:\n")
print(test_data)
```
_В командной строке получим следующее:_
```
1. Данные файла '../data/test_data_01.txt' успешно импортированы. Полученный текст:

International cooperation in the sphere of science and technology.

Belarusian science aims at resourcesaving, energy-efficient technologies, industrial biotechnologies, nanomaterials, environmental protection and information solutions. Different research and development centres contribute to the innovation infrastructure of the Republic of Belarus. The two biggest scientific centres in our country are the National Academy of Sciences of Belarus (NASB) and the High-Tech Park (HTP). Our scientists can be proud of their achievements as they contribute a lot to the development of the world's science.
Belarusian scientists of the National Centre of Particle and Hi-Energy Physics of the Belarusian State University took part in experiments at the Large Hadron Collider in the European Organization for Nuclear Research (CERN) which is located at the France-Switzerland border. Our scientists controlled the operation of the Compact Muon Solenoid (CMS).
Belarusian physicists created the source of terahertz radiation which helps to make different objects visible while they are inside solid or liquid bodies.
Our scientists grew a red emerald for the first time in the world. This kind of emerald is very rare in nature, and the artificial analogue created by Belarusian scientists is 100 times cheaper.
Belarusian scientists also created an electronic system "ForestFire" to determine the level of radioactive contamination after forest fires this innovation helps to model possible situations and to find possible solutions during and after forest fires.
Belarusian agriculturists grew new kinds of potato and wheat!
Our scientists created a brand new-generation laser which can be used in different industries from medicine to the manufacturing sector. This laser is smaller, safer for eyes and more functional than its foreign analogues.
Belarus with its scientific potential is now called the Silicon Valley of Europe. The High-Tech Park of Belarus, one of the leading innovation-based IT clusters in Europe, appeared in 2006. The software produced by the HTP resident companies is in high demand abroad and is used by Coca-Cola, Microsoft, Google, Toyota, MTV, Reuters, Samsung, Mitsubishi, British Telecom and the World Bank. In 2011 six resident companies of the HTP were included in the "WORLD Top-100 Providers of IT Services" list. Our country is also number 1 IT technologies exporter within the CIS.
Belarusian company OAO "Peleng" is one of the leading developers of optical devices and optoelectronic systems for military and dual use. The company produces exclusive space equipment. On July 22, 2012 the Belarusian satellite for the remote sensing of the Earth was launched into outer space. This satellite is a part of a cluster of five satellites by the "Soyuz-FG" booster rocket from the Baikonur space launch site. The Belarusian satellite can relocate in the orbit and take images at the required angle. The satellite is fitted with the equipment produced by OAO "Peleng" and works jointly with the Russian satellite "Canopus-B". Peleng also created a "SKIF-GRID" supercomputer on the basis of 12-core AMD Opteron processor and graphic processing units.
Belarus takes an active part in the International telecommunications, information and banking technologies forum TIBO, Belarus' biggest IT forum and one of the major events in the sphere of telecommunications and software in the Baltic States and the CIS. The participants from Belarus, Russia, Europe, Latin America and Asia present the most interesting media projects and modern mass media technologies. The program of the forum includes master classes of famous media persons and presentations of periodicals, TV channels, radio channels and websites. Belarusian scientists presented a unique innovation at the international forum TIBO-2015. A unique chip can help both experts and ordinary buyers to learn all the product information in a flash. Such electronic passports have already been tested by Belarusian producers and buyers of expensive fur products. In a minute, you can see a full file on the chosen product on the screen of your mobile phone. You can learn the quality and origin of the product, place of production and other information.
Annually about 450 international science and technology projects are implemented in Belarus. Some of these projects have bilateral character. Belarus supports bi-lateral cooperation with Russia, Latvia and Lithuania, Ukraine, Poland, Moldova, Kazakhstan, Serbia, China, India, Venezuela and most of them are hosted by the Scientific and Technological Park "Polytechnic" at Belarusian National Technical University. Belarus-South Korean scientific centre is hosted by the NASB.
Among the two most successful bilateral IT achievements are Viber and World of Tanks (WoT).
Viber is the most recognizable Belarusian brand in the IT sector? Viber is called "a Belarusian miracle". This is an instant messaging and voice over IP application for smartphones. With the help of Viber you can exchange video and audio messages. Viber Media Company was founded by Israeli-Belarusian partners Talmon Marko and Igor Magazinnik. The company is run from Israel but has its development centres in Belarus. The company started in 2010 as a small development firm of 40 people and its founder Sergei Goncharic. Nowadays Viber is the leader of social applications category in the Appstores in 30 countries. Viber has about 280 million global registered users.
Another famous Belarusian IT company is Belarusian-Cypriot company "Wargaming" with its massively multiplayer online game "World of Tanks". The developer of WoT "Game Stream", Minsk Development Centre of Wargaming, is a resident company of the High-Tech Park in Belarus. Game Stream provides IT support in organizing international events. The game was officially announced in 2009 and in August 2010 the Russian version of the game was officially released. The players can choose six primary types of battles and take control of a single armoured vehicle and they can communicate with other players through typing or voice chat. In 2011 the number of WoT users reached 1 million. In January 2011 the world record "The Most Players Online Simultaneously" was officially registered by the Guinness Book of Records (91,311 players). In 2012 the game was improved and new features and vehicles were added. Also in 2012 WoT debuted as an eSports game at the World Cyber Games. In 2013 and 2014 WoT was named the "Online Game of the Year" and got the "Golden Joystick Award". Today the number of WoT fans exceeds more than 100 million.
Belarus also has its own Nobel Prize winner in Science. Zhores Ivanovich Alferov was born on March 15, 1930 in Vitebsk, Belarus to a family of a factory manager. He finished high school in Minsk and in 1947 entered Belarusian Politechnic Academy. In 1952 Alferov graduated from Leningrad Electrotechnical Institute and began to work in the Ioffe Physico-Technical Institute where he got several scientific degrees. In 1987 Zhores Alferov became the Director of the Institute. Alferov invented the heterotransistor which revolutionized the mobile phone and satellite communications. This in turn improved semiconductor design in LEDs and CDs. In 2000 Zhores Alferov received the Nobel Prize in Physics together with Herbert Kroemer and Jack Kilby for their work that laid the foundation for the modern era of information technology. Alferov's invention made it possible to transfer all the information from satellites down to the Earth and have many telephone lines between cities. We use his scientific innovations in our everyday life: in mobile phones, CDs, traffic lights, price tag's decoders and even lasers.
```

2. -[x] Подготавливаем даные для последующей обработки (работой со словами): удаляем знаки препинания из текста:
```
# 2) Подготавливаем данные: удаляем знаки препинания из текста
test_data_1 = remove_punctuation(test_data)
print(test_data_1)
```
_В командной строке получим следующее:_
```
International cooperation in the sphere of science and technology

Belarusian science aims at resourcesaving energyefficient technologies industrial biotechnologies nanomaterials environmental protection and information solutions Different research and development centres contribute to the innovation infrastructure of the Republic of Belarus The two biggest scientific centres in our country are the National Academy of Sciences of Belarus NASB and the HighTech Park HTP Our scientists can be proud of their achievements as they contribute a lot to the development of the worlds science
Belarusian scientists of the National Centre of Particle and HiEnergy Physics of the Belarusian State University took part in experiments at the Large Hadron Collider in the European Organization for Nuclear Research CERN which is located at the FranceSwitzerland border Our scientists controlled the operation of the Compact Muon Solenoid CMS
Belarusian physicists created the source of terahertz radiation which helps to make different objects visible while they are inside solid or liquid bodies
Our scientists grew a red emerald for the first time in the world This kind of emerald is very rare in nature and the artificial analogue created by Belarusian scientists is 100 times cheaper
Belarusian scientists also created an electronic system ForestFire to determine the level of radioactive contamination after forest fires this innovation helps to model possible situations and to find possible solutions during and after forest fires
Belarusian agriculturists grew new kinds of potato and wheat
Our scientists created a brand newgeneration laser which can be used in different industries from medicine to the manufacturing sector This laser is smaller safer for eyes and more functional than its foreign analogues
Belarus with its scientific potential is now called the Silicon Valley of Europe The HighTech Park of Belarus one of the leading innovationbased IT clusters in Europe appeared in 2006 The software produced by the HTP resident companies is in high demand abroad and is used by CocaCola Microsoft Google Toyota MTV Reuters Samsung Mitsubishi British Telecom and the World Bank In 2011 six resident companies of the HTP were included in the WORLD Top100 Providers of IT Services list Our country is also number 1 IT technologies exporter within the CIS
Belarusian company OAO Peleng is one of the leading developers of optical devices and optoelectronic systems for military and dual use The company produces exclusive space equipment On July 22 2012 the Belarusian satellite for the remote sensing of the Earth was launched into outer space This satellite is a part of a cluster of five satellites by the SoyuzFG booster rocket from the Baikonur space launch site The Belarusian satellite can relocate in the orbit and take images at the required angle The satellite is fitted with the equipment produced by OAO Peleng and works jointly with the Russian satellite CanopusB Peleng also created a SKIFGRID supercomputer on the basis of 12core AMD Opteron processor and graphic processing units
Belarus takes an active part in the International telecommunications information and banking technologies forum TIBO Belarus biggest IT forum and one of the major events in the sphere of telecommunications and software in the Baltic States and the CIS The participants from Belarus Russia Europe Latin America and Asia present the most interesting media projects and modern mass media technologies The program of the forum includes master classes of famous media persons and presentations of periodicals TV channels radio channels and websites Belarusian scientists presented a unique innovation at the international forum TIBO2015 A unique chip can help both experts and ordinary buyers to learn all the product information in a flash Such electronic passports have already been tested by Belarusian producers and buyers of expensive fur products In a minute you can see a full file on the chosen product on the screen of your mobile phone You can learn the quality and origin of the product place of production and other information
Annually about 450 international science and technology projects are implemented in Belarus Some of these projects have bilateral character Belarus supports bilateral cooperation with Russia Latvia and Lithuania Ukraine Poland Moldova Kazakhstan Serbia China India Venezuela and most of them are hosted by the Scientific and Technological Park Polytechnic at Belarusian National Technical University BelarusSouth Korean scientific centre is hosted by the NASB
Among the two most successful bilateral IT achievements are Viber and World of Tanks WoT
Viber is the most recognizable Belarusian brand in the IT sector Viber is called a Belarusian miracle This is an instant messaging and voice over IP application for smartphones With the help of Viber you can exchange video and audio messages Viber Media Company was founded by IsraeliBelarusian partners Talmon Marko and Igor Magazinnik The company is run from Israel but has its development centres in Belarus The company started in 2010 as a small development firm of 40 people and its founder Sergei Goncharic Nowadays Viber is the leader of social applications category in the Appstores in 30 countries Viber has about 280 million global registered users
Another famous Belarusian IT company is BelarusianCypriot company Wargaming with its massively multiplayer online game World of Tanks The developer of WoT Game Stream Minsk Development Centre of Wargaming is a resident company of the HighTech Park in Belarus Game Stream provides IT support in organizing international events The game was officially announced in 2009 and in August 2010 the Russian version of the game was officially released The players can choose six primary types of battles and take control of a single armoured vehicle and they can communicate with other players through typing or voice chat In 2011 the number of WoT users reached 1 million In January 2011 the world record The Most Players Online Simultaneously was officially registered by the Guinness Book of Records 91311 players In 2012 the game was improved and new features and vehicles were added Also in 2012 WoT debuted as an eSports game at the World Cyber Games In 2013 and 2014 WoT was named the Online Game of the Year and got the Golden Joystick Award Today the number of WoT fans exceeds more than 100 million
Belarus also has its own Nobel Prize winner in Science Zhores Ivanovich Alferov was born on March 15 1930 in Vitebsk Belarus to a family of a factory manager He finished high school in Minsk and in 1947 entered Belarusian Politechnic Academy In 1952 Alferov graduated from Leningrad Electrotechnical Institute and began to work in the Ioffe PhysicoTechnical Institute where he got several scientific degrees In 1987 Zhores Alferov became the Director of the Institute Alferov invented the heterotransistor which revolutionized the mobile phone and satellite communications This in turn improved semiconductor design in LEDs and CDs In 2000 Zhores Alferov received the Nobel Prize in Physics together with Herbert Kroemer and Jack Kilby for their work that laid the foundation for the modern era of information technology Alferovs invention made it possible to transfer all the information from satellites down to the Earth and have many telephone lines between cities We use his scientific innovations in our everyday life in mobile phones CDs traffic lights price tags decoders and even lasers
```

3. -[x] Преобразуем текст во множество слов и находим его длину (кол-во 'уникальных' слов):
```
# 3) Преобразуем текст во множество слов и находим его длину (кол-во 'уникальных' слов без учета стоп-слов)
uniq_words = str_2_words(test_data_1, ignore_stopwords=True)
# Выводим количество уникальных слов в тексте
print(f"2. Количество уникальных слов в тексте: {len(uniq_words)}.")
print(uniq_words)
```
_В командной строке получим следующее:_
```
2. Количество уникальных слов в тексте: 462.
{'visible', 'produces', 'brand', 'safer', 'university', 'satellite', 'republic', 'cern', 'reached', 'exclusive', 'equipment', 'family', 'graduated', 'lines', 'number', 'game', 'academy', 'eyes', 'oao', 'park', 'model', 'leds', 'providers', 'laid', 'world', 'organizing', 'leading', 'factory', 'ivanovich', 'located', 'companies', 'different', 'inside', 'vehicle', 'minsk', 'protection', 'politechnic', 'solid', 'belarus', 'goncharic', 'cooperation', 'bilateral', 'environmental', 'cds', 'wheat', 'institute', 'latin', 'july', 'armoured', 'use', 'design', 'emerald', 'centre', 'manufacturing', 'rocket', 'situations', 'unique', 'named', 'tv', 'soyuzfg', 'franceswitzerland', 'turn', 'school', 'founder', 'physicotechnical', 'work', 'ukraine', 'exceeds', 'screen', 'users', 'biotechnologies', 'samsung', 'nasb', 'production', 'developer', 'tested', 'leningrad', 'contamination', 'modern', 'records', 'proud', 'canopusb', 'appeared', 'cms', 'orbit', 'information', 'provides', 'types', 'part', 'tanks', 'among', 'potential', 'book', 'year', 'innovations', 'works', 'added', 'help', 'energyefficient', 'magazinnik', 'announced', 'sphere', 'valley', 'biggest', 'presentations', 'experts', 'grew', 'particle', 'prize', 'global', 'application', 'poland', 'instant', 'foundation', 'worlds', 'persons', 'fans', 'implemented', 'china', 'services', 'belarussouth', 'radiation', 'small', 'joystick', 'artificial', 'military', 'major', 'record', 'control', 'called', 'quality', 'forum', 'venezuela', 'latvia', 'india', 'received', 'august', 'nanomaterials', 'six', 'founded', 'vehicles', 'required', 'earth', 'determine', 'jointly', 'active', 'chosen', 'massively', 'buyers', 'forestfire', 'silicon', 'kazakhstan', 'support', 'million', 'products', 'improved', 'launch', 'functional', 'transfer', 'supercomputer', 'solutions', 'choose', 'lasers', 'developers', 'video', 'physicists', 'list', 'liquid', 'potato', 'igor', 'social', 'demand', 'banking', 'minute', 'winner', 'interesting', 'communications', 'baikonur', 'simultaneously', 'even', 'muon', 'golden', 'alferovs', 'esports', 'got', 'games', 'sergei', 'experiments', 'centres', 'opteron', 'infrastructure', 'nuclear', 'israel', 'battles', 'technological', 'exporter', 'heterotransistor', 'mtv', 'firm', 'cis', 'sensing', 'miracle', 'online', 'newgeneration', 'british', 'make', 'kroemer', 'bodies', 'degrees', 'cluster', 'participants', 'vitebsk', 'jack', 'level', 'organization', 'asia', 'invented', 'analogues', 'hosted', 'angle', 'people', 'invention', 'research', 'talmon', 'chip', 'viber', 'technology', 'scientific', 'kinds', 'national', 'foreign', 'primary', 'border', 'relocate', 'belarusiancypriot', 'red', 'multiplayer', 'category', 'radioactive', 'science', 'character', 'analogue', 'zhores', 'medicine', 'laser', 'officially', 'began', 'hienergy', 'events', 'cocacola', 'time', 'high', 'sciences', 'microsoft', 'audio', 'famous', 'optical', 'systems', 'players', 'htp', 'solenoid', 'released', 'price', 'tags', 'devices', 'director', 'fires', 'registered', 'another', 'telecommunications', 'created', 'supports', 'images', 'hightech', 'international', 'now', 'communicate', 'full', 'innovation', 'objects', 'america', 'revolutionized', 'smaller', 'phones', 'google', 'take', 'entered', 'master', 'site', 'version', 'korean', 'phone', 'typing', 'electronic', 'traffic', 'amd', 'classes', 'chat', 'launched', 'physics', 'new', 'agriculturists', 'development', 'country', 'cheaper', 'russia', 'partners', 'controlled', 'voice', 'manager', 'projects', 'telecom', 'herbert', 'hadron', 'see', 'origin', 'software', 'times', 'includes', 'semiconductor', 'industrial', 'resident', 'kind', 'industries', 'finished', 'features', 'applications', 'dual', 'helps', 'nature', 'together', 'single', 'producers', 'skifgrid', 'lot', 'system', 'fur', 'graphic', 'presented', 'can', 'place', 'successful', 'today', 'technical', 'took', 'baltic', 'reuters', 'states', 'debuted', 'produced', 'russian', 'processing', 'march', 'possible', 'smartphones', 'born', 'ordinary', 'file', 'wargaming', 'january', 'five', 'contribute', 'cities', 'europe', 'learn', 'resourcesaving', 'cyber', 'expensive', 'telephone', 'takes', 'guinness', 'mass', 'websites', 'messaging', 'wot', 'already', 'media', 'life', 'several', 'find', 'leader', 'collider', 'everyday', 'polytechnic', 'innovationbased', 'lights', 'first', 'space', 'compact', 'ioffe', 'recognizable', 'ip', 'award', 'company', 'state', 'large', 'annually', 'clusters', 'lithuania', 'within', 'units', 'achievements', 'israelibelarusian', 'basis', 'satellites', 'radio', 'used', 'included', 'alferov', 'processor', 'started', 'product', 'fitted', 'nobel', 'stream', 'scientists', 'rare', 'flash', 'serbia', 'became', 'source', 'technologies', 'passports', 'moldova', 'appstores', 'aims', 'forest', 'mitsubishi', 'kilby', 'exchange', 'decoders', 'program', 'also', 'channels', 'remote', 'peleng', 'booster', 'european', 'electrotechnical', 'two', 'toyota', 'bank', 'many', 'messages', 'belarusian', 'outer', 'made', 'operation', 'countries', 'nowadays', 'periodicals', 'terahertz', 'marko', 'tibo', 'run', 'sector', 'optoelectronic', 'era', 'mobile', 'one', 'abroad', 'present'}
```

4. -[x] Подсчитываем число гласных и согласных букв в тексте:
```
# 4) Подсчитываем число гласных и согласных букв
gl, sogl = get_vow_cons(test_data_1, alph="EN")
print(f"3. Количество гласных букв: {gl}; согласных букв: {sogl}.")
```
_В командной строке получим следующее:_
```
3. Количество гласных букв: 2457; согласных букв: 3789.
```

5. -[x] Разбиваем текст из фала на предложения, считаем их колиество и выводим статистику по каждому из них:
```
# 5) Разбиваем текст из фала на предложения и выводим статистику по каждому из них
sentences = get_sent(test_data)
print(f"4. Общее число предложений в тексте: {len(sentences)}.")
print(f"\tНиже приводится информация о длине каждого предложения:")
for ind, sent in enumerate(sentences):
	print(f"\tSentence #{ind+1}: length: {sentences.get(sent)}; data: {sent}.")
```
_В командной строке получим следующее:_
```
4. Общее число предложений в тексте: 69.
	Ниже приводится информация о длине каждого предложения:
	Sentence #1: length: 65; data: International cooperation in the sphere of science and technology.
	Sentence #2: length: 167; data: Belarusian science aims at resourcesaving, energy-efficient technologies, industrial biotechnologies, nanomaterials, environmental protection and information solutions.
	Sentence #3: length: 113; data: Different research and development centres contribute to the innovation infrastructure of the Republic of Belarus.
	Sentence #4: length: 133; data: The two biggest scientific centres in our country are the National Academy of Sciences of Belarus (NASB) and the High-Tech Park (HTP).
	Sentence #5: length: 116; data: Our scientists can be proud of their achievements as they contribute a lot to the development of the world's science.
	Sentence #6: length: 274; data: Belarusian scientists of the National Centre of Particle and Hi-Energy Physics of the Belarusian State University took part in experiments at the Large Hadron Collider in the European Organization for Nuclear Research (CERN) which is located at the France-Switzerland border.
	Sentence #7: length: 74; data: Our scientists controlled the operation of the Compact Muon Solenoid (CMS).
	Sentence #8: length: 154; data: Belarusian physicists created the source of terahertz radiation which helps to make different objects visible while they are inside solid or liquid bodies.
	Sentence #9: length: 65; data: Our scientists grew a red emerald for the first time in the world.
	Sentence #10: length: 126; data: This kind of emerald is very rare in nature, and the artificial analogue created by Belarusian scientists is 100 times cheaper.
	Sentence #11: length: 251; data: Belarusian scientists also created an electronic system "ForestFire" to determine the level of radioactive contamination after forest fires this innovation helps to model possible situations and to find possible solutions during and after forest fires.
	Sentence #12: length: 60; data: Belarusian agriculturists grew new kinds of potato and wheat.
	Sentence #13: length: 135; data: Our scientists created a brand new-generation laser which can be used in different industries from medicine to the manufacturing sector.
	Sentence #14: length: 84; data: This laser is smaller, safer for eyes and more functional than its foreign analogues.
	Sentence #15: length: 80; data: Belarus with its scientific potential is now called the Silicon Valley of Europe.
	Sentence #16: length: 106; data: The High-Tech Park of Belarus, one of the leading innovation-based IT clusters in Europe, appeared in 2006.
	Sentence #17: length: 199; data: The software produced by the HTP resident companies is in high demand abroad and is used by Coca-Cola, Microsoft, Google, Toyota, MTV, Reuters, Samsung, Mitsubishi, British Telecom and the World Bank.
	Sentence #18: length: 108; data: In 2011 six resident companies of the HTP were included in the "WORLD Top-100 Providers of IT Services" list.
	Sentence #19: length: 68; data: Our country is also number 1 IT technologies exporter within the CIS.
	Sentence #20: length: 136; data: Belarusian company OAO "Peleng" is one of the leading developers of optical devices and optoelectronic systems for military and dual use.
	Sentence #21: length: 46; data: The company produces exclusive space equipment.
	Sentence #22: length: 107; data: On July 22, 2012 the Belarusian satellite for the remote sensing of the Earth was launched into outer space.
	Sentence #23: length: 125; data: This satellite is a part of a cluster of five satellites by the "Soyuz-FG" booster rocket from the Baikonur space launch site.
	Sentence #24: length: 88; data: The Belarusian satellite can relocate in the orbit and take images at the required angle.
	Sentence #25: length: 124; data: The satellite is fitted with the equipment produced by OAO "Peleng" and works jointly with the Russian satellite "Canopus-B".
	Sentence #26: length: 122; data: Peleng also created a "SKIF-GRID" supercomputer on the basis of 12-core AMD Opteron processor and graphic processing units.
	Sentence #27: length: 254; data: Belarus takes an active part in the International telecommunications, information and banking technologies forum TIBO, Belarus' biggest IT forum and one of the major events in the sphere of telecommunications and software in the Baltic States and the CIS.
	Sentence #28: length: 148; data: The participants from Belarus, Russia, Europe, Latin America and Asia present the most interesting media projects and modern mass media technologies.
	Sentence #29: length: 147; data: The program of the forum includes master classes of famous media persons and presentations of periodicals, TV channels, radio channels and websites.
	Sentence #30: length: 88; data: Belarusian scientists presented a unique innovation at the international forum TIBO-2015.
	Sentence #31: length: 103; data: A unique chip can help both experts and ordinary buyers to learn all the product information in a flash.
	Sentence #32: length: 111; data: Such electronic passports have already been tested by Belarusian producers and buyers of expensive fur products.
	Sentence #33: length: 93; data: In a minute, you can see a full file on the chosen product on the screen of your mobile phone.
	Sentence #34: length: 94; data: You can learn the quality and origin of the product, place of production and other information.
	Sentence #35: length: 91; data: Annually about 450 international science and technology projects are implemented in Belarus.
	Sentence #36: length: 47; data: Some of these projects have bilateral character.
	Sentence #37: length: 271; data: Belarus supports bi-lateral cooperation with Russia, Latvia and Lithuania, Ukraine, Poland, Moldova, Kazakhstan, Serbia, China, India, Venezuela and most of them are hosted by the Scientific and Technological Park "Polytechnic" at Belarusian National Technical University.
	Sentence #38: length: 60; data: Belarus-South Korean scientific centre is hosted by the NASB.
	Sentence #39: length: 90; data: Among the two most successful bilateral IT achievements are Viber and World of Tanks (WoT).
	Sentence #40: length: 64; data: Viber is the most recognizable Belarusian brand in the IT sector.
	Sentence #41: length: 38; data: Viber is called "a Belarusian miracle".
	Sentence #42: length: 74; data: This is an instant messaging and voice over IP application for smartphones.
	Sentence #43: length: 64; data: With the help of Viber you can exchange video and audio messages.
	Sentence #44: length: 95; data: Viber Media Company was founded by Israeli-Belarusian partners Talmon Marko and Igor Magazinnik.
	Sentence #45: length: 73; data: The company is run from Israel but has its development centres in Belarus.
	Sentence #46: length: 101; data: The company started in 2010 as a small development firm of 40 people and its founder Sergei Goncharic.
	Sentence #47: length: 93; data: Nowadays Viber is the leader of social applications category in the Appstores in 30 countries.
	Sentence #48: length: 51; data: Viber has about 280 million global registered users.
	Sentence #49: length: 138; data: Another famous Belarusian IT company is Belarusian-Cypriot company "Wargaming" with its massively multiplayer online game "World of Tanks".
	Sentence #50: length: 129; data: The developer of WoT "Game Stream", Minsk Development Centre of Wargaming, is a resident company of the High-Tech Park in Belarus.
	Sentence #51: length: 66; data: Game Stream provides IT support in organizing international events.
	Sentence #52: length: 116; data: The game was officially announced in 2009 and in August 2010 the Russian version of the game was officially released.
	Sentence #53: length: 170; data: The players can choose six primary types of battles and take control of a single armoured vehicle and they can communicate with other players through typing or voice chat.
	Sentence #54: length: 49; data: In 2011 the number of WoT users reached 1 million.
	Sentence #55: length: 148; data: In January 2011 the world record "The Most Players Online Simultaneously" was officially registered by the Guinness Book of Records (91,311 players).
	Sentence #56: length: 70; data: In 2012 the game was improved and new features and vehicles were added.
	Sentence #57: length: 68; data: Also in 2012 WoT debuted as an eSports game at the World Cyber Games.
	Sentence #58: length: 96; data: In 2013 and 2014 WoT was named the "Online Game of the Year" and got the "Golden Joystick Award".
	Sentence #59: length: 58; data: Today the number of WoT fans exceeds more than 100 million.
	Sentence #60: length: 54; data: Belarus also has its own Nobel Prize winner in Science.
	Sentence #61: length: 104; data: Zhores Ivanovich Alferov was born on March 15, 1930 in Vitebsk, Belarus to a family of a factory manager.
	Sentence #62: length: 83; data: He finished high school in Minsk and in 1947 entered Belarusian Politechnic Academy.
	Sentence #63: length: 166; data: In 1952 Alferov graduated from Leningrad Electrotechnical Institute and began to work in the Ioffe Physico-Technical Institute where he got several scientific degrees.
	Sentence #64: length: 59; data: In 1987 Zhores Alferov became the Director of the Institute.
	Sentence #65: length: 104; data: Alferov invented the heterotransistor which revolutionized the mobile phone and satellite communications.
	Sentence #66: length: 58; data: This in turn improved semiconductor design in LEDs and CDs.
	Sentence #67: length: 188; data: In 2000 Zhores Alferov received the Nobel Prize in Physics together with Herbert Kroemer and Jack Kilby for their work that laid the foundation for the modern era of information technology.
	Sentence #68: length: 147; data: Alferov's invention made it possible to transfer all the information from satellites down to the Earth and have many telephone lines between cities.
	Sentence #69: length: 131; data: We use his scientific innovations in our everyday life: in mobile phones, CDs, traffic lights, price tag's decoders and even lasers.
```

6. -[x] Считаем число повторений каждого слова в тексте (с учетом критерием схожести - расстояния Левенштейна).
Параметр `crit_lev_val` зададим равным 100 (т.е. полное совпадение). 
При этом стоп-слова не учитываются (параметр `ignore_stopwords=True`):
```
# 6) Считаем число повторений каждого слова в тексте (с учетом критерием схожести)
words_stat = words_cnt(str_2_words(test_data_1, unique=False, ignore_stopwords=True), crit_lev_val=80)
print(f"5. Ниже приводится информация о частоте использования каждого слова в тексте:")
for word, cnt in words_stat.items():
    print(f"\tWord: '{word}': number of entries: {cnt}.")
```
_В командной строке получим следующее:_
```
5. Ниже приводится информация о частоте использования каждого слова в тексте:
	Word: 'international': number of entries: 5.
	Word: 'cooperation': number of entries: 2.
	Word: 'sphere': number of entries: 2.
	Word: 'science': number of entries: 5.
	Word: 'technology': number of entries: 3.
	Word: 'belarusian': number of entries: 17.
	Word: 'aims': number of entries: 1.
	Word: 'resourcesaving': number of entries: 1.
	Word: 'energyefficient': number of entries: 1.
	Word: 'technologies': number of entries: 4.
	Word: 'industrial': number of entries: 1.
	Word: 'biotechnologies': number of entries: 1.
	Word: 'nanomaterials': number of entries: 1.
	Word: 'environmental': number of entries: 1.
	Word: 'protection': number of entries: 1.
	Word: 'information': number of entries: 6.
	Word: 'solutions': number of entries: 2.
	Word: 'different': number of entries: 3.
	Word: 'research': number of entries: 2.
	Word: 'development': number of entries: 5.
	Word: 'centres': number of entries: 3.
	Word: 'contribute': number of entries: 2.
	Word: 'innovation': number of entries: 3.
	Word: 'infrastructure': number of entries: 1.
	Word: 'republic': number of entries: 1.
	Word: 'belarus': number of entries: 13.
	Word: 'two': number of entries: 2.
	Word: 'biggest': number of entries: 2.
	Word: 'scientific': number of entries: 6.
	Word: 'country': number of entries: 2.
	Word: 'national': number of entries: 3.
	Word: 'academy': number of entries: 2.
	Word: 'sciences': number of entries: 1.
	Word: 'nasb': number of entries: 2.
	Word: 'hightech': number of entries: 3.
	Word: 'park': number of entries: 4.
	Word: 'htp': number of entries: 3.
	Word: 'scientists': number of entries: 8.
	Word: 'can': number of entries: 9.
	Word: 'proud': number of entries: 1.
	Word: 'achievements': number of entries: 2.
	Word: 'lot': number of entries: 1.
	Word: 'worlds': number of entries: 1.
	Word: 'centre': number of entries: 3.
	Word: 'particle': number of entries: 1.
	Word: 'hienergy': number of entries: 1.
	Word: 'physics': number of entries: 2.
	Word: 'state': number of entries: 1.
	Word: 'university': number of entries: 2.
	Word: 'took': number of entries: 1.
	Word: 'part': number of entries: 3.
	Word: 'experiments': number of entries: 1.
	Word: 'large': number of entries: 1.
	Word: 'hadron': number of entries: 1.
	Word: 'collider': number of entries: 1.
	Word: 'european': number of entries: 1.
	Word: 'organization': number of entries: 1.
	Word: 'nuclear': number of entries: 1.
	Word: 'cern': number of entries: 1.
	Word: 'located': number of entries: 1.
	Word: 'franceswitzerland': number of entries: 1.
	Word: 'border': number of entries: 1.
	Word: 'controlled': number of entries: 1.
	Word: 'operation': number of entries: 1.
	Word: 'compact': number of entries: 1.
	Word: 'muon': number of entries: 1.
	Word: 'solenoid': number of entries: 1.
	Word: 'cms': number of entries: 1.
	Word: 'physicists': number of entries: 1.
	Word: 'created': number of entries: 5.
	Word: 'source': number of entries: 1.
	Word: 'terahertz': number of entries: 1.
	Word: 'radiation': number of entries: 1.
	Word: 'helps': number of entries: 2.
	Word: 'make': number of entries: 1.
	Word: 'objects': number of entries: 1.
	Word: 'visible': number of entries: 1.
	Word: 'inside': number of entries: 1.
	Word: 'solid': number of entries: 1.
	Word: 'liquid': number of entries: 1.
	Word: 'bodies': number of entries: 1.
	Word: 'grew': number of entries: 2.
	Word: 'red': number of entries: 1.
	Word: 'emerald': number of entries: 2.
	Word: 'first': number of entries: 1.
	Word: 'time': number of entries: 1.
	Word: 'world': number of entries: 7.
	Word: 'kind': number of entries: 1.
	Word: 'rare': number of entries: 1.
	Word: 'nature': number of entries: 1.
	Word: 'artificial': number of entries: 1.
	Word: 'analogue': number of entries: 1.
	Word: 'times': number of entries: 1.
	Word: 'cheaper': number of entries: 1.
	Word: 'also': number of entries: 5.
	Word: 'electronic': number of entries: 2.
	Word: 'system': number of entries: 1.
	Word: 'forestfire': number of entries: 1.
	Word: 'determine': number of entries: 1.
	Word: 'level': number of entries: 1.
	Word: 'radioactive': number of entries: 1.
	Word: 'contamination': number of entries: 1.
	Word: 'forest': number of entries: 2.
	Word: 'fires': number of entries: 2.
	Word: 'model': number of entries: 1.
	Word: 'possible': number of entries: 3.
	Word: 'situations': number of entries: 1.
	Word: 'find': number of entries: 1.
	Word: 'agriculturists': number of entries: 1.
	Word: 'new': number of entries: 2.
	Word: 'kinds': number of entries: 1.
	Word: 'potato': number of entries: 1.
	Word: 'wheat': number of entries: 1.
	Word: 'brand': number of entries: 2.
	Word: 'newgeneration': number of entries: 1.
	Word: 'laser': number of entries: 2.
	Word: 'used': number of entries: 2.
	Word: 'industries': number of entries: 1.
	Word: 'medicine': number of entries: 1.
	Word: 'manufacturing': number of entries: 1.
	Word: 'sector': number of entries: 2.
	Word: 'smaller': number of entries: 1.
	Word: 'safer': number of entries: 1.
	Word: 'eyes': number of entries: 1.
	Word: 'functional': number of entries: 1.
	Word: 'foreign': number of entries: 1.
	Word: 'analogues': number of entries: 1.
	Word: 'potential': number of entries: 1.
	Word: 'now': number of entries: 1.
	Word: 'called': number of entries: 2.
	Word: 'silicon': number of entries: 1.
	Word: 'valley': number of entries: 1.
	Word: 'europe': number of entries: 3.
	Word: 'one': number of entries: 3.
	Word: 'leading': number of entries: 2.
	Word: 'innovationbased': number of entries: 1.
	Word: 'clusters': number of entries: 1.
	Word: 'appeared': number of entries: 1.
	Word: 'software': number of entries: 2.
	Word: 'produced': number of entries: 2.
	Word: 'resident': number of entries: 3.
	Word: 'companies': number of entries: 2.
	Word: 'high': number of entries: 2.
	Word: 'demand': number of entries: 1.
	Word: 'abroad': number of entries: 1.
	Word: 'cocacola': number of entries: 1.
	Word: 'microsoft': number of entries: 1.
	Word: 'google': number of entries: 1.
	Word: 'toyota': number of entries: 1.
	Word: 'mtv': number of entries: 1.
	Word: 'reuters': number of entries: 1.
	Word: 'samsung': number of entries: 1.
	Word: 'mitsubishi': number of entries: 1.
	Word: 'british': number of entries: 1.
	Word: 'telecom': number of entries: 1.
	Word: 'bank': number of entries: 1.
	Word: 'six': number of entries: 2.
	Word: 'included': number of entries: 1.
	Word: 'providers': number of entries: 1.
	Word: 'services': number of entries: 1.
	Word: 'list': number of entries: 1.
	Word: 'number': number of entries: 3.
	Word: 'exporter': number of entries: 1.
	Word: 'within': number of entries: 1.
	Word: 'cis': number of entries: 2.
	Word: 'company': number of entries: 8.
	Word: 'oao': number of entries: 2.
	Word: 'peleng': number of entries: 3.
	Word: 'developers': number of entries: 1.
	Word: 'optical': number of entries: 1.
	Word: 'devices': number of entries: 1.
	Word: 'optoelectronic': number of entries: 1.
	Word: 'systems': number of entries: 1.
	Word: 'military': number of entries: 1.
	Word: 'dual': number of entries: 1.
	Word: 'use': number of entries: 2.
	Word: 'produces': number of entries: 1.
	Word: 'exclusive': number of entries: 1.
	Word: 'space': number of entries: 3.
	Word: 'equipment': number of entries: 2.
	Word: 'july': number of entries: 1.
	Word: 'satellite': number of entries: 6.
	Word: 'remote': number of entries: 1.
	Word: 'sensing': number of entries: 1.
	Word: 'earth': number of entries: 2.
	Word: 'launched': number of entries: 1.
	Word: 'outer': number of entries: 1.
	Word: 'cluster': number of entries: 1.
	Word: 'five': number of entries: 1.
	Word: 'satellites': number of entries: 2.
	Word: 'soyuzfg': number of entries: 1.
	Word: 'booster': number of entries: 1.
	Word: 'rocket': number of entries: 1.
	Word: 'baikonur': number of entries: 1.
	Word: 'launch': number of entries: 1.
	Word: 'site': number of entries: 1.
	Word: 'relocate': number of entries: 1.
	Word: 'orbit': number of entries: 1.
	Word: 'take': number of entries: 2.
	Word: 'images': number of entries: 1.
	Word: 'required': number of entries: 1.
	Word: 'angle': number of entries: 1.
	Word: 'fitted': number of entries: 1.
	Word: 'works': number of entries: 1.
	Word: 'jointly': number of entries: 1.
	Word: 'russian': number of entries: 2.
	Word: 'canopusb': number of entries: 1.
	Word: 'skifgrid': number of entries: 1.
	Word: 'supercomputer': number of entries: 1.
	Word: 'basis': number of entries: 1.
	Word: 'amd': number of entries: 1.
	Word: 'opteron': number of entries: 1.
	Word: 'processor': number of entries: 1.
	Word: 'graphic': number of entries: 1.
	Word: 'processing': number of entries: 1.
	Word: 'units': number of entries: 1.
	Word: 'takes': number of entries: 1.
	Word: 'active': number of entries: 1.
	Word: 'telecommunications': number of entries: 2.
	Word: 'banking': number of entries: 1.
	Word: 'forum': number of entries: 4.
	Word: 'tibo': number of entries: 1.
	Word: 'major': number of entries: 1.
	Word: 'events': number of entries: 2.
	Word: 'baltic': number of entries: 1.
	Word: 'states': number of entries: 1.
	Word: 'participants': number of entries: 1.
	Word: 'russia': number of entries: 2.
	Word: 'latin': number of entries: 1.
	Word: 'america': number of entries: 1.
	Word: 'asia': number of entries: 1.
	Word: 'present': number of entries: 1.
	Word: 'interesting': number of entries: 1.
	Word: 'media': number of entries: 4.
	Word: 'projects': number of entries: 3.
	Word: 'modern': number of entries: 2.
	Word: 'mass': number of entries: 1.
	Word: 'program': number of entries: 1.
	Word: 'includes': number of entries: 1.
	Word: 'master': number of entries: 1.
	Word: 'classes': number of entries: 1.
	Word: 'famous': number of entries: 2.
	Word: 'persons': number of entries: 1.
	Word: 'presentations': number of entries: 1.
	Word: 'periodicals': number of entries: 1.
	Word: 'tv': number of entries: 1.
	Word: 'channels': number of entries: 2.
	Word: 'radio': number of entries: 1.
	Word: 'websites': number of entries: 1.
	Word: 'presented': number of entries: 1.
	Word: 'unique': number of entries: 2.
	Word: 'chip': number of entries: 1.
	Word: 'help': number of entries: 2.
	Word: 'experts': number of entries: 1.
	Word: 'ordinary': number of entries: 1.
	Word: 'buyers': number of entries: 2.
	Word: 'learn': number of entries: 2.
	Word: 'product': number of entries: 3.
	Word: 'flash': number of entries: 1.
	Word: 'passports': number of entries: 1.
	Word: 'already': number of entries: 1.
	Word: 'tested': number of entries: 1.
	Word: 'producers': number of entries: 1.
	Word: 'expensive': number of entries: 1.
	Word: 'fur': number of entries: 1.
	Word: 'products': number of entries: 1.
	Word: 'minute': number of entries: 1.
	Word: 'see': number of entries: 1.
	Word: 'full': number of entries: 1.
	Word: 'file': number of entries: 1.
	Word: 'chosen': number of entries: 1.
	Word: 'screen': number of entries: 1.
	Word: 'mobile': number of entries: 3.
	Word: 'phone': number of entries: 2.
	Word: 'quality': number of entries: 1.
	Word: 'origin': number of entries: 1.
	Word: 'place': number of entries: 1.
	Word: 'production': number of entries: 1.
	Word: 'annually': number of entries: 1.
	Word: 'implemented': number of entries: 1.
	Word: 'bilateral': number of entries: 3.
	Word: 'character': number of entries: 1.
	Word: 'supports': number of entries: 1.
	Word: 'latvia': number of entries: 1.
	Word: 'lithuania': number of entries: 1.
	Word: 'ukraine': number of entries: 1.
	Word: 'poland': number of entries: 1.
	Word: 'moldova': number of entries: 1.
	Word: 'kazakhstan': number of entries: 1.
	Word: 'serbia': number of entries: 1.
	Word: 'china': number of entries: 1.
	Word: 'india': number of entries: 1.
	Word: 'venezuela': number of entries: 1.
	Word: 'hosted': number of entries: 2.
	Word: 'technological': number of entries: 1.
	Word: 'polytechnic': number of entries: 1.
	Word: 'technical': number of entries: 1.
	Word: 'belarussouth': number of entries: 1.
	Word: 'korean': number of entries: 1.
	Word: 'among': number of entries: 1.
	Word: 'successful': number of entries: 1.
	Word: 'viber': number of entries: 7.
	Word: 'tanks': number of entries: 2.
	Word: 'wot': number of entries: 6.
	Word: 'recognizable': number of entries: 1.
	Word: 'miracle': number of entries: 1.
	Word: 'instant': number of entries: 1.
	Word: 'messaging': number of entries: 1.
	Word: 'voice': number of entries: 2.
	Word: 'ip': number of entries: 1.
	Word: 'application': number of entries: 1.
	Word: 'smartphones': number of entries: 1.
	Word: 'exchange': number of entries: 1.
	Word: 'video': number of entries: 1.
	Word: 'audio': number of entries: 1.
	Word: 'messages': number of entries: 1.
	Word: 'founded': number of entries: 1.
	Word: 'israelibelarusian': number of entries: 1.
	Word: 'partners': number of entries: 1.
	Word: 'talmon': number of entries: 1.
	Word: 'marko': number of entries: 1.
	Word: 'igor': number of entries: 1.
	Word: 'magazinnik': number of entries: 1.
	Word: 'run': number of entries: 1.
	Word: 'israel': number of entries: 1.
	Word: 'started': number of entries: 1.
	Word: 'small': number of entries: 1.
	Word: 'firm': number of entries: 1.
	Word: 'people': number of entries: 1.
	Word: 'founder': number of entries: 1.
	Word: 'sergei': number of entries: 1.
	Word: 'goncharic': number of entries: 1.
	Word: 'nowadays': number of entries: 1.
	Word: 'leader': number of entries: 1.
	Word: 'social': number of entries: 1.
	Word: 'applications': number of entries: 1.
	Word: 'category': number of entries: 1.
	Word: 'appstores': number of entries: 1.
	Word: 'countries': number of entries: 1.
	Word: 'million': number of entries: 3.
	Word: 'global': number of entries: 1.
	Word: 'registered': number of entries: 2.
	Word: 'users': number of entries: 2.
	Word: 'another': number of entries: 1.
	Word: 'belarusiancypriot': number of entries: 1.
	Word: 'wargaming': number of entries: 2.
	Word: 'massively': number of entries: 1.
	Word: 'multiplayer': number of entries: 1.
	Word: 'online': number of entries: 3.
	Word: 'game': number of entries: 8.
	Word: 'developer': number of entries: 1.
	Word: 'stream': number of entries: 2.
	Word: 'minsk': number of entries: 2.
	Word: 'provides': number of entries: 1.
	Word: 'support': number of entries: 1.
	Word: 'organizing': number of entries: 1.
	Word: 'officially': number of entries: 3.
	Word: 'announced': number of entries: 1.
	Word: 'august': number of entries: 1.
	Word: 'version': number of entries: 1.
	Word: 'released': number of entries: 1.
	Word: 'players': number of entries: 4.
	Word: 'choose': number of entries: 1.
	Word: 'primary': number of entries: 1.
	Word: 'types': number of entries: 1.
	Word: 'battles': number of entries: 1.
	Word: 'control': number of entries: 1.
	Word: 'single': number of entries: 1.
	Word: 'armoured': number of entries: 1.
	Word: 'vehicle': number of entries: 1.
	Word: 'communicate': number of entries: 1.
	Word: 'typing': number of entries: 1.
	Word: 'chat': number of entries: 1.
	Word: 'reached': number of entries: 1.
	Word: 'january': number of entries: 1.
	Word: 'record': number of entries: 1.
	Word: 'simultaneously': number of entries: 1.
	Word: 'guinness': number of entries: 1.
	Word: 'book': number of entries: 1.
	Word: 'records': number of entries: 1.
	Word: 'improved': number of entries: 2.
	Word: 'features': number of entries: 1.
	Word: 'vehicles': number of entries: 1.
	Word: 'added': number of entries: 1.
	Word: 'debuted': number of entries: 1.
	Word: 'esports': number of entries: 1.
	Word: 'cyber': number of entries: 1.
	Word: 'games': number of entries: 1.
	Word: 'named': number of entries: 1.
	Word: 'year': number of entries: 1.
	Word: 'got': number of entries: 2.
	Word: 'golden': number of entries: 1.
	Word: 'joystick': number of entries: 1.
	Word: 'award': number of entries: 1.
	Word: 'today': number of entries: 1.
	Word: 'fans': number of entries: 1.
	Word: 'exceeds': number of entries: 1.
	Word: 'nobel': number of entries: 2.
	Word: 'prize': number of entries: 2.
	Word: 'winner': number of entries: 1.
	Word: 'zhores': number of entries: 3.
	Word: 'ivanovich': number of entries: 1.
	Word: 'alferov': number of entries: 5.
	Word: 'born': number of entries: 1.
	Word: 'march': number of entries: 1.
	Word: 'vitebsk': number of entries: 1.
	Word: 'family': number of entries: 1.
	Word: 'factory': number of entries: 1.
	Word: 'manager': number of entries: 1.
	Word: 'finished': number of entries: 1.
	Word: 'school': number of entries: 1.
	Word: 'entered': number of entries: 1.
	Word: 'politechnic': number of entries: 1.
	Word: 'graduated': number of entries: 1.
	Word: 'leningrad': number of entries: 1.
	Word: 'electrotechnical': number of entries: 1.
	Word: 'institute': number of entries: 3.
	Word: 'began': number of entries: 1.
	Word: 'work': number of entries: 2.
	Word: 'ioffe': number of entries: 1.
	Word: 'physicotechnical': number of entries: 1.
	Word: 'several': number of entries: 1.
	Word: 'degrees': number of entries: 1.
	Word: 'became': number of entries: 1.
	Word: 'director': number of entries: 1.
	Word: 'invented': number of entries: 1.
	Word: 'heterotransistor': number of entries: 1.
	Word: 'revolutionized': number of entries: 1.
	Word: 'communications': number of entries: 1.
	Word: 'turn': number of entries: 1.
	Word: 'semiconductor': number of entries: 1.
	Word: 'design': number of entries: 1.
	Word: 'leds': number of entries: 1.
	Word: 'cds': number of entries: 2.
	Word: 'received': number of entries: 1.
	Word: 'together': number of entries: 1.
	Word: 'herbert': number of entries: 1.
	Word: 'kroemer': number of entries: 1.
	Word: 'jack': number of entries: 1.
	Word: 'kilby': number of entries: 1.
	Word: 'laid': number of entries: 1.
	Word: 'foundation': number of entries: 1.
	Word: 'era': number of entries: 1.
	Word: 'alferovs': number of entries: 1.
	Word: 'invention': number of entries: 1.
	Word: 'made': number of entries: 1.
	Word: 'transfer': number of entries: 1.
	Word: 'many': number of entries: 1.
	Word: 'telephone': number of entries: 1.
	Word: 'lines': number of entries: 1.
	Word: 'cities': number of entries: 1.
	Word: 'innovations': number of entries: 1.
	Word: 'everyday': number of entries: 1.
	Word: 'life': number of entries: 1.
	Word: 'phones': number of entries: 1.
	Word: 'traffic': number of entries: 1.
	Word: 'lights': number of entries: 1.
	Word: 'price': number of entries: 1.
	Word: 'tags': number of entries: 1.
	Word: 'decoders': number of entries: 1.
	Word: 'even': number of entries: 1.
	Word: 'lasers': number of entries: 1.
```
Если параметр `crit_lev_val` зададим равным 80, то получим следующий результат:
```
5. Ниже приводится информация о частоте использования каждого слова в тексте:
	Word: 'international': number of entries: 5.
	Word: 'cooperation': number of entries: 3.
	Word: 'sphere': number of entries: 2.
	Word: 'science': number of entries: 6.
	Word: 'technology': number of entries: 7.
	Word: 'belarusian': number of entries: 30.
	Word: 'aims': number of entries: 1.
	Word: 'resourcesaving': number of entries: 1.
	Word: 'energyefficient': number of entries: 1.
	Word: 'technologies': number of entries: 9.
	Word: 'industrial': number of entries: 2.
	Word: 'biotechnologies': number of entries: 5.
	Word: 'nanomaterials': number of entries: 1.
	Word: 'environmental': number of entries: 1.
	Word: 'protection': number of entries: 2.
	Word: 'information': number of entries: 6.
	Word: 'solutions': number of entries: 2.
	Word: 'different': number of entries: 3.
	Word: 'research': number of entries: 2.
	Word: 'development': number of entries: 6.
	Word: 'centres': number of entries: 6.
	Word: 'contribute': number of entries: 2.
	Word: 'innovation': number of entries: 5.
	Word: 'infrastructure': number of entries: 1.
	Word: 'republic': number of entries: 1.
	Word: 'belarus': number of entries: 30.
	Word: 'two': number of entries: 2.
	Word: 'biggest': number of entries: 2.
	Word: 'scientific': number of entries: 6.
	Word: 'country': number of entries: 2.
	Word: 'national': number of entries: 3.
	Word: 'academy': number of entries: 2.
	Word: 'sciences': number of entries: 6.
	Word: 'nasb': number of entries: 2.
	Word: 'hightech': number of entries: 3.
	Word: 'park': number of entries: 4.
	Word: 'htp': number of entries: 3.
	Word: 'scientists': number of entries: 8.
	Word: 'can': number of entries: 9.
	Word: 'proud': number of entries: 1.
	Word: 'achievements': number of entries: 2.
	Word: 'lot': number of entries: 1.
	Word: 'worlds': number of entries: 8.
	Word: 'centre': number of entries: 6.
	Word: 'particle': number of entries: 1.
	Word: 'hienergy': number of entries: 1.
	Word: 'physics': number of entries: 3.
	Word: 'state': number of entries: 3.
	Word: 'university': number of entries: 2.
	Word: 'took': number of entries: 1.
	Word: 'part': number of entries: 3.
	Word: 'experiments': number of entries: 1.
	Word: 'large': number of entries: 1.
	Word: 'hadron': number of entries: 1.
	Word: 'collider': number of entries: 1.
	Word: 'european': number of entries: 4.
	Word: 'organization': number of entries: 2.
	Word: 'nuclear': number of entries: 1.
	Word: 'cern': number of entries: 1.
	Word: 'located': number of entries: 2.
	Word: 'franceswitzerland': number of entries: 1.
	Word: 'border': number of entries: 1.
	Word: 'controlled': number of entries: 2.
	Word: 'operation': number of entries: 3.
	Word: 'compact': number of entries: 1.
	Word: 'muon': number of entries: 1.
	Word: 'solenoid': number of entries: 1.
	Word: 'cms': number of entries: 1.
	Word: 'physicists': number of entries: 3.
	Word: 'created': number of entries: 5.
	Word: 'source': number of entries: 1.
	Word: 'terahertz': number of entries: 1.
	Word: 'radiation': number of entries: 1.
	Word: 'helps': number of entries: 4.
	Word: 'make': number of entries: 1.
	Word: 'objects': number of entries: 4.
	Word: 'visible': number of entries: 1.
	Word: 'inside': number of entries: 1.
	Word: 'solid': number of entries: 1.
	Word: 'liquid': number of entries: 1.
	Word: 'bodies': number of entries: 1.
	Word: 'grew': number of entries: 2.
	Word: 'red': number of entries: 1.
	Word: 'emerald': number of entries: 2.
	Word: 'first': number of entries: 3.
	Word: 'time': number of entries: 2.
	Word: 'world': number of entries: 8.
	Word: 'kind': number of entries: 2.
	Word: 'rare': number of entries: 1.
	Word: 'nature': number of entries: 1.
	Word: 'artificial': number of entries: 1.
	Word: 'analogue': number of entries: 2.
	Word: 'times': number of entries: 2.
	Word: 'cheaper': number of entries: 1.
	Word: 'also': number of entries: 5.
	Word: 'electronic': number of entries: 3.
	Word: 'system': number of entries: 2.
	Word: 'forestfire': number of entries: 1.
	Word: 'determine': number of entries: 1.
	Word: 'level': number of entries: 1.
	Word: 'radioactive': number of entries: 1.
	Word: 'contamination': number of entries: 1.
	Word: 'forest': number of entries: 2.
	Word: 'fires': number of entries: 3.
	Word: 'model': number of entries: 1.
	Word: 'possible': number of entries: 3.
	Word: 'situations': number of entries: 1.
	Word: 'find': number of entries: 1.
	Word: 'agriculturists': number of entries: 1.
	Word: 'new': number of entries: 2.
	Word: 'kinds': number of entries: 2.
	Word: 'potato': number of entries: 1.
	Word: 'wheat': number of entries: 1.
	Word: 'brand': number of entries: 2.
	Word: 'newgeneration': number of entries: 1.
	Word: 'laser': number of entries: 3.
	Word: 'used': number of entries: 4.
	Word: 'industries': number of entries: 2.
	Word: 'medicine': number of entries: 1.
	Word: 'manufacturing': number of entries: 1.
	Word: 'sector': number of entries: 2.
	Word: 'smaller': number of entries: 2.
	Word: 'safer': number of entries: 1.
	Word: 'eyes': number of entries: 1.
	Word: 'functional': number of entries: 1.
	Word: 'foreign': number of entries: 1.
	Word: 'analogues': number of entries: 2.
	Word: 'potential': number of entries: 1.
	Word: 'now': number of entries: 1.
	Word: 'called': number of entries: 2.
	Word: 'silicon': number of entries: 1.
	Word: 'valley': number of entries: 1.
	Word: 'europe': number of entries: 4.
	Word: 'one': number of entries: 3.
	Word: 'leading': number of entries: 2.
	Word: 'innovationbased': number of entries: 5.
	Word: 'clusters': number of entries: 2.
	Word: 'appeared': number of entries: 1.
	Word: 'software': number of entries: 2.
	Word: 'produced': number of entries: 7.
	Word: 'resident': number of entries: 4.
	Word: 'companies': number of entries: 2.
	Word: 'high': number of entries: 2.
	Word: 'demand': number of entries: 1.
	Word: 'abroad': number of entries: 1.
	Word: 'cocacola': number of entries: 1.
	Word: 'microsoft': number of entries: 1.
	Word: 'google': number of entries: 1.
	Word: 'toyota': number of entries: 1.
	Word: 'mtv': number of entries: 2.
	Word: 'reuters': number of entries: 1.
	Word: 'samsung': number of entries: 1.
	Word: 'mitsubishi': number of entries: 1.
	Word: 'british': number of entries: 1.
	Word: 'telecom': number of entries: 1.
	Word: 'bank': number of entries: 1.
	Word: 'six': number of entries: 2.
	Word: 'included': number of entries: 2.
	Word: 'providers': number of entries: 2.
	Word: 'services': number of entries: 2.
	Word: 'list': number of entries: 1.
	Word: 'number': number of entries: 3.
	Word: 'exporter': number of entries: 1.
	Word: 'within': number of entries: 1.
	Word: 'cis': number of entries: 2.
	Word: 'company': number of entries: 8.
	Word: 'oao': number of entries: 2.
	Word: 'peleng': number of entries: 3.
	Word: 'developers': number of entries: 2.
	Word: 'optical': number of entries: 1.
	Word: 'devices': number of entries: 2.
	Word: 'optoelectronic': number of entries: 3.
	Word: 'systems': number of entries: 2.
	Word: 'military': number of entries: 1.
	Word: 'dual': number of entries: 1.
	Word: 'use': number of entries: 4.
	Word: 'produces': number of entries: 8.
	Word: 'exclusive': number of entries: 1.
	Word: 'space': number of entries: 4.
	Word: 'equipment': number of entries: 2.
	Word: 'july': number of entries: 1.
	Word: 'satellite': number of entries: 8.
	Word: 'remote': number of entries: 1.
	Word: 'sensing': number of entries: 1.
	Word: 'earth': number of entries: 2.
	Word: 'launched': number of entries: 2.
	Word: 'outer': number of entries: 1.
	Word: 'cluster': number of entries: 2.
	Word: 'five': number of entries: 1.
	Word: 'satellites': number of entries: 8.
	Word: 'soyuzfg': number of entries: 1.
	Word: 'booster': number of entries: 1.
	Word: 'rocket': number of entries: 1.
	Word: 'baikonur': number of entries: 1.
	Word: 'launch': number of entries: 2.
	Word: 'site': number of entries: 1.
	Word: 'relocate': number of entries: 2.
	Word: 'orbit': number of entries: 1.
	Word: 'take': number of entries: 3.
	Word: 'images': number of entries: 1.
	Word: 'required': number of entries: 1.
	Word: 'angle': number of entries: 1.
	Word: 'fitted': number of entries: 1.
	Word: 'works': number of entries: 3.
	Word: 'jointly': number of entries: 1.
	Word: 'russian': number of entries: 4.
	Word: 'canopusb': number of entries: 1.
	Word: 'skifgrid': number of entries: 1.
	Word: 'supercomputer': number of entries: 1.
	Word: 'basis': number of entries: 1.
	Word: 'amd': number of entries: 1.
	Word: 'opteron': number of entries: 1.
	Word: 'processor': number of entries: 1.
	Word: 'graphic': number of entries: 1.
	Word: 'processing': number of entries: 1.
	Word: 'units': number of entries: 1.
	Word: 'takes': number of entries: 5.
	Word: 'active': number of entries: 1.
	Word: 'telecommunications': number of entries: 3.
	Word: 'banking': number of entries: 1.
	Word: 'forum': number of entries: 4.
	Word: 'tibo': number of entries: 1.
	Word: 'major': number of entries: 1.
	Word: 'events': number of entries: 3.
	Word: 'baltic': number of entries: 1.
	Word: 'states': number of entries: 2.
	Word: 'participants': number of entries: 1.
	Word: 'russia': number of entries: 4.
	Word: 'latin': number of entries: 1.
	Word: 'america': number of entries: 1.
	Word: 'asia': number of entries: 1.
	Word: 'present': number of entries: 5.
	Word: 'interesting': number of entries: 1.
	Word: 'media': number of entries: 4.
	Word: 'projects': number of entries: 4.
	Word: 'modern': number of entries: 2.
	Word: 'mass': number of entries: 1.
	Word: 'program': number of entries: 1.
	Word: 'includes': number of entries: 2.
	Word: 'master': number of entries: 1.
	Word: 'classes': number of entries: 1.
	Word: 'famous': number of entries: 2.
	Word: 'persons': number of entries: 1.
	Word: 'presentations': number of entries: 1.
	Word: 'periodicals': number of entries: 1.
	Word: 'tv': number of entries: 2.
	Word: 'channels': number of entries: 2.
	Word: 'radio': number of entries: 2.
	Word: 'websites': number of entries: 1.
	Word: 'presented': number of entries: 2.
	Word: 'unique': number of entries: 2.
	Word: 'chip': number of entries: 1.
	Word: 'help': number of entries: 4.
	Word: 'experts': number of entries: 1.
	Word: 'ordinary': number of entries: 1.
	Word: 'buyers': number of entries: 2.
	Word: 'learn': number of entries: 2.
	Word: 'product': number of entries: 8.
	Word: 'flash': number of entries: 1.
	Word: 'passports': number of entries: 1.
	Word: 'already': number of entries: 1.
	Word: 'tested': number of entries: 1.
	Word: 'producers': number of entries: 5.
	Word: 'expensive': number of entries: 1.
	Word: 'fur': number of entries: 1.
	Word: 'products': number of entries: 6.
	Word: 'minute': number of entries: 1.
	Word: 'see': number of entries: 1.
	Word: 'full': number of entries: 1.
	Word: 'file': number of entries: 1.
	Word: 'chosen': number of entries: 2.
	Word: 'screen': number of entries: 1.
	Word: 'mobile': number of entries: 3.
	Word: 'phone': number of entries: 3.
	Word: 'quality': number of entries: 1.
	Word: 'origin': number of entries: 1.
	Word: 'place': number of entries: 4.
	Word: 'production': number of entries: 5.
	Word: 'annually': number of entries: 1.
	Word: 'implemented': number of entries: 1.
	Word: 'bilateral': number of entries: 3.
	Word: 'character': number of entries: 1.
	Word: 'supports': number of entries: 3.
	Word: 'latvia': number of entries: 1.
	Word: 'lithuania': number of entries: 1.
	Word: 'ukraine': number of entries: 1.
	Word: 'poland': number of entries: 1.
	Word: 'moldova': number of entries: 1.
	Word: 'kazakhstan': number of entries: 1.
	Word: 'serbia': number of entries: 1.
	Word: 'china': number of entries: 1.
	Word: 'india': number of entries: 1.
	Word: 'venezuela': number of entries: 1.
	Word: 'hosted': number of entries: 2.
	Word: 'technological': number of entries: 6.
	Word: 'polytechnic': number of entries: 2.
	Word: 'technical': number of entries: 2.
	Word: 'belarussouth': number of entries: 1.
	Word: 'korean': number of entries: 1.
	Word: 'among': number of entries: 1.
	Word: 'successful': number of entries: 1.
	Word: 'viber': number of entries: 7.
	Word: 'tanks': number of entries: 3.
	Word: 'wot': number of entries: 6.
	Word: 'recognizable': number of entries: 1.
	Word: 'miracle': number of entries: 1.
	Word: 'instant': number of entries: 1.
	Word: 'messaging': number of entries: 1.
	Word: 'voice': number of entries: 2.
	Word: 'ip': number of entries: 1.
	Word: 'application': number of entries: 2.
	Word: 'smartphones': number of entries: 1.
	Word: 'exchange': number of entries: 1.
	Word: 'video': number of entries: 1.
	Word: 'audio': number of entries: 2.
	Word: 'messages': number of entries: 1.
	Word: 'founded': number of entries: 2.
	Word: 'israelibelarusian': number of entries: 1.
	Word: 'partners': number of entries: 1.
	Word: 'talmon': number of entries: 1.
	Word: 'marko': number of entries: 1.
	Word: 'igor': number of entries: 1.
	Word: 'magazinnik': number of entries: 1.
	Word: 'run': number of entries: 1.
	Word: 'israel': number of entries: 1.
	Word: 'started': number of entries: 2.
	Word: 'small': number of entries: 2.
	Word: 'firm': number of entries: 1.
	Word: 'people': number of entries: 1.
	Word: 'founder': number of entries: 2.
	Word: 'sergei': number of entries: 1.
	Word: 'goncharic': number of entries: 1.
	Word: 'nowadays': number of entries: 1.
	Word: 'leader': number of entries: 1.
	Word: 'social': number of entries: 1.
	Word: 'applications': number of entries: 2.
	Word: 'category': number of entries: 1.
	Word: 'appstores': number of entries: 1.
	Word: 'countries': number of entries: 1.
	Word: 'million': number of entries: 3.
	Word: 'global': number of entries: 1.
	Word: 'registered': number of entries: 2.
	Word: 'users': number of entries: 2.
	Word: 'another': number of entries: 1.
	Word: 'belarusiancypriot': number of entries: 1.
	Word: 'wargaming': number of entries: 2.
	Word: 'massively': number of entries: 1.
	Word: 'multiplayer': number of entries: 1.
	Word: 'online': number of entries: 3.
	Word: 'game': number of entries: 9.
	Word: 'developer': number of entries: 7.
	Word: 'stream': number of entries: 2.
	Word: 'minsk': number of entries: 2.
	Word: 'provides': number of entries: 2.
	Word: 'support': number of entries: 2.
	Word: 'organizing': number of entries: 2.
	Word: 'officially': number of entries: 3.
	Word: 'announced': number of entries: 1.
	Word: 'august': number of entries: 1.
	Word: 'version': number of entries: 1.
	Word: 'released': number of entries: 1.
	Word: 'players': number of entries: 4.
	Word: 'choose': number of entries: 2.
	Word: 'primary': number of entries: 1.
	Word: 'types': number of entries: 1.
	Word: 'battles': number of entries: 1.
	Word: 'control': number of entries: 2.
	Word: 'single': number of entries: 1.
	Word: 'armoured': number of entries: 1.
	Word: 'vehicle': number of entries: 2.
	Word: 'communicate': number of entries: 2.
	Word: 'typing': number of entries: 1.
	Word: 'chat': number of entries: 1.
	Word: 'reached': number of entries: 1.
	Word: 'january': number of entries: 1.
	Word: 'record': number of entries: 2.
	Word: 'simultaneously': number of entries: 1.
	Word: 'guinness': number of entries: 1.
	Word: 'book': number of entries: 1.
	Word: 'records': number of entries: 2.
	Word: 'improved': number of entries: 2.
	Word: 'features': number of entries: 1.
	Word: 'vehicles': number of entries: 2.
	Word: 'added': number of entries: 1.
	Word: 'debuted': number of entries: 1.
	Word: 'esports': number of entries: 2.
	Word: 'cyber': number of entries: 1.
	Word: 'games': number of entries: 9.
	Word: 'named': number of entries: 1.
	Word: 'year': number of entries: 1.
	Word: 'got': number of entries: 2.
	Word: 'golden': number of entries: 1.
	Word: 'joystick': number of entries: 1.
	Word: 'award': number of entries: 1.
	Word: 'today': number of entries: 1.
	Word: 'fans': number of entries: 1.
	Word: 'exceeds': number of entries: 1.
	Word: 'nobel': number of entries: 2.
	Word: 'prize': number of entries: 3.
	Word: 'winner': number of entries: 1.
	Word: 'zhores': number of entries: 3.
	Word: 'ivanovich': number of entries: 1.
	Word: 'alferov': number of entries: 6.
	Word: 'born': number of entries: 1.
	Word: 'march': number of entries: 1.
	Word: 'vitebsk': number of entries: 1.
	Word: 'family': number of entries: 1.
	Word: 'factory': number of entries: 1.
	Word: 'manager': number of entries: 1.
	Word: 'finished': number of entries: 1.
	Word: 'school': number of entries: 1.
	Word: 'entered': number of entries: 1.
	Word: 'politechnic': number of entries: 2.
	Word: 'graduated': number of entries: 1.
	Word: 'leningrad': number of entries: 1.
	Word: 'electrotechnical': number of entries: 1.
	Word: 'institute': number of entries: 3.
	Word: 'began': number of entries: 1.
	Word: 'work': number of entries: 3.
	Word: 'ioffe': number of entries: 1.
	Word: 'physicotechnical': number of entries: 1.
	Word: 'several': number of entries: 1.
	Word: 'degrees': number of entries: 1.
	Word: 'became': number of entries: 1.
	Word: 'director': number of entries: 1.
	Word: 'invented': number of entries: 1.
	Word: 'heterotransistor': number of entries: 1.
	Word: 'revolutionized': number of entries: 1.
	Word: 'communications': number of entries: 4.
	Word: 'turn': number of entries: 1.
	Word: 'semiconductor': number of entries: 1.
	Word: 'design': number of entries: 1.
	Word: 'leds': number of entries: 1.
	Word: 'cds': number of entries: 2.
	Word: 'received': number of entries: 1.
	Word: 'together': number of entries: 1.
	Word: 'herbert': number of entries: 1.
	Word: 'kroemer': number of entries: 1.
	Word: 'jack': number of entries: 1.
	Word: 'kilby': number of entries: 1.
	Word: 'laid': number of entries: 1.
	Word: 'foundation': number of entries: 1.
	Word: 'era': number of entries: 1.
	Word: 'alferovs': number of entries: 6.
	Word: 'invention': number of entries: 1.
	Word: 'made': number of entries: 1.
	Word: 'transfer': number of entries: 1.
	Word: 'many': number of entries: 1.
	Word: 'telephone': number of entries: 1.
	Word: 'lines': number of entries: 1.
	Word: 'cities': number of entries: 1.
	Word: 'innovations': number of entries: 5.
	Word: 'everyday': number of entries: 1.
	Word: 'life': number of entries: 1.
	Word: 'phones': number of entries: 3.
	Word: 'traffic': number of entries: 1.
	Word: 'lights': number of entries: 1.
	Word: 'price': number of entries: 3.
	Word: 'tags': number of entries: 1.
	Word: 'decoders': number of entries: 1.
	Word: 'even': number of entries: 3.
	Word: 'lasers': number of entries: 3.
```
В данном случае число вхождений некоторых слов увеличилось. 
Например, слова ***`belarus`*** и ***`belarusian`*** считаются теперь ***'похожими'***.

7. -[x] Выводим N наиболее часто встречаемых слов в тексте (при `crit_lev_val = 80`):
```
N = 10
sorted_words = most_rep_words(words_stat, num=N)
print(f"6. {N} наиболее часто встречаемых слов в тексте:")
for word, cnt in sorted_words:
	print(f"\tWord: '{word}': number of entries: {cnt}.")
```
_В командной строке получим следующее:_
```
6. 10 наиболее часто встречаемых слов в тексте:
	Word: 'belarusian': number of entries: 17.
	Word: 'belarus': number of entries: 13.
	Word: 'can': number of entries: 9.
	Word: 'scientists': number of entries: 8.
	Word: 'company': number of entries: 8.
	Word: 'game': number of entries: 8.
	Word: 'world': number of entries: 7.
	Word: 'viber': number of entries: 7.
	Word: 'information': number of entries: 6.
	Word: 'scientific': number of entries: 6.
```
<hr>

***В файле **`hw_03_spacy.ipynd`** находится код программы, который использует готовую библиотеку `spacy` для решения данной задачи.
Готовый мощный функционал библиотеки позволяет значительно сократить и упростить программный код.***
