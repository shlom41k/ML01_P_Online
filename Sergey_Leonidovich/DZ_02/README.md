## Пример разрешения конфликта разных веток Git
<hr>

Имеется репозиторий с веткой `main`. В ветке `main` находится файл `git_example.txt` со следующим содержанием:

```
String from "main" branch
```

### 1. Создание конфликта

- Создаем ветку `pupa`:
```
$ git checkout -b branch_pupa
```

- Вносим изменения в файл `git_example.txt`. Теперь он выгляди так:
```
String from "main" branch
String from "pupa" branch
```

- Добавляем изменения и делаем коммит:
```
$ git add .
$ git commit -am "Update data"
```

- Возвращаемся в ветку `main`. Файл `git_example.txt` в ней по-прежнему выглядит так: 
```
String from "main" branch
```

- Создаем ветку `lupa`:
```
$ git checkout -b lupa
```

- Вносим изменения в файл `git_example.txt`. Теперь он выгляди так:
```
String from "main" branch
String from "lupa" branch
```

- Добавляем изменения и делаем коммит:
```
$ git add .
$ git commit -am "Update data from LUPA"
```

- Возвращаемся в ветку `main`. Файл `git_example.txt` в ней по-прежнему выглядит так: 
```
String from "main" branch
```
<hr>

### 2. Слияние веток

- Сливаем ветку `pupa` в `main`:
```
$ git merge branch_pupa
```

- Получаем сообщение о том, что изменения из ветки `pupa` подтянулись в ветку `main`:
```
Updating 01b48eb..2c71b4f
Fast-forward
 Sergey_Leonidovich/DZ_02/git/git_example.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```

- Файл `git_example.txt` в ветке `main` теперь выгляди так:
```
String from "main" branch
String from "pupa" branch
```

- Следом сливаем ветку `lupa` в `main`:
```
$ git merge lupa
```

- Получаем сообщение о наличии конфликта:
```
Auto-merging Sergey_Leonidovich/DZ_02/git/git_example.txt
CONFLICT (content): Merge conflict in Sergey_Leonidovich/DZ_02/git/git_example.txt
Automatic merge failed; fix conflicts and then commit the result.
```

### 3. Разрешение конфликта
- При помощи программы [Meld](https://meldmerge.org/) открываем 'проблемный' файл:
<p align="center">
![#](https://github.com/shlom41k/ML01_P_Online/blob/main/Sergey_Leonidovich/DZ_02/git/img/meld_1.PNG)
</p>

- Формируем итоговое содержание файла `git_example.txt`. 
В данном случае мы хотим, чтобы присутствовали данные из обеих веток (`pupa` и `lupa`).
Сохраняем полученный результат.
<p align="center">
![#](https://github.com/shlom41k/ML01_P_Online/blob/main/Sergey_Leonidovich/DZ_02/git/img/meld_2.PNG)
</p>

- Добавляем изменения и делаем коммит:
```
$ git add .
$ git commit -am "Merge PUPA & LUPA branches"
```
<hr>

Конфликт разрешен.

В папке [img](Sergey_Leonidovich/DZ_02/git/img) находятся изображения командной строки `git bash`, где выполнялся данный пример.