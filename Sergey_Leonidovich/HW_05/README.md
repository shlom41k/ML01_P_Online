# Homework 05
<hr>


## Задание
Основная цель задания - познакомиться с принципами ООП в ***Python***.

Есть `Алфавит`, характеристиками которого являются:
1. _Язык_;
2. _Список букв_.

Для алфавита можно:
* напечатать все буквы алфавита;
* посчитать количество букв.

Также есть `Английский алфавит`, характеристиками которого являются:
1. _Язык;_
2. _Список букв;_
3. _Количество букв._

Для английского алфавита можно:
* посчитать количество букв;
* определить, относится ли буква к английскому алфавиту;
* получить пример текста на английском языке.
<hr>


## Описание этапов разработки программы
* _**Для класса `Alphabet` необходимо:**_
  - Создать класс Alphabet.
  - Создать метод `__init__()`, внутри которого будут определены два динамических свойства:
    + `lang` - язык;
    + `letters` - список букв.
    Начальные значения свойств берутся из входных параметров метода.
  - Создать метод `print()`, который выведет в консоль буквы алфавита. 
  - Создать метод `letters_num()`, который вернет количество букв в алфавите.

+ _**Для класса `EngAlphabet` необходимо:**_
  - Создать класс `EngAlphabet` путем наследования от класса `Alphabet`.
  - Создать метод `__init__()`, внутри которого будет вызываться родительский метод `__init__()`. 
    В качестве параметров ему будут передаваться обозначение языка (например, _'En'_) и строка, 
состоящая из всех букв алфавита (можно воспользоваться свойством `ascii_uppercase` из модуля `string`).
  - Добавить приватное статическое свойство `__letters_num`, которое будет хранить количество букв в алфавите.
  - Создать метод `is_en_letter()`, который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
  - Переопределить метод `letters_num()` - пусть в текущем классе он будет возвращать значение свойства `__letters_num`.
  - Создать статический метод `example()`, который будет возвращать пример текста на английском языке.


## Структура репозитория
Структура проекта `HW_05` имеет следующий вид:
+ в каталоге **`src`** содержатся файлы **`.py`** с исходным кодом:
    * в файле **`hw_05.py`** находится код основной программы;
    * в файле **`hw_05.ipynb`** находится код основной программы для `Jupyter Notebook`.


## Выполнение программы
Для запуска программы необходимо выполнить:
```
python.exe .\hw_05.py
```
<hr>

## Описание работы программы
Ниже приведен листинг скрипта **`hw_05.py`**:

```
import string


class Alphabet:

    # All objects in class
    __alphabets = list()

    def __init__(self, language: str, letters: list):
        """
        Constructor: create object of class Alphabet.
        :param language: language (str);
        :param letters: list of letters for current language (list).
        """
        # Add properties
        self.__language = language
        self.__letters = letters

        # Add item to list of all class objects
        self.__class__.__alphabets.append(self.__language)

    def __del__(self):
        """ Destructor """
        # Remove item from list of all class objects
        self.__class__.__alphabets.remove(self.__language)

    def __str__(self) -> str:
        """ View for object, when use str() method """
        return f"{self.__language}"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def get_all_alphabet(cls) -> list:
        """ Get lisf of all class objects """
        return cls.__alphabets

    @property
    def language(self) -> str:
        return self.__language

    @property
    def letters(self) -> list:
        return self.__letters

    def print_letters(self) -> None:
        """ Display all letters in alphabet """
        print(f"Буквы '{self.__language}' алфавита: {''.join(self.__letters)}.")

    def letters_num(self) -> int:
        """ Get number of letters in alphabet """
        return len(self.__letters)


class EngAlphabet(Alphabet):

    def __init__(self, language: str, letters: str):
        """
        Constructor: create object of class EngAlphabet.
        :param language: language (str);
        :param letters: letters for current language (str).
        """
        # Call parent class __init__() method
        super().__init__(language=language, letters=[letter for letter in letters])
        # Add new property for this class
        self.__letters_num = len(self.letters)

    def __del__(self):
        """ Destructor """
        super().__del__()
        ...

    def is_en_letter(self, letter: str) -> bool:
        """
        Checks whether a character belongs to the given alphabet
        :param letter: character (str);
        :return: True or False (boolean).
        """
        return True if letter.lower() in self.letters else False

    # Override parent method
    def letters_num(self) -> int:
        """ Get number of letters in alphabet """
        return self.__letters_num

    @staticmethod
    def example() -> str:
        """ Return text example """
        return "Example of simple english language text"


if __name__ == "__main__":

    # 1) Создаем объект класса EngAlphabet
    en = EngAlphabet(language="EN", letters=string.ascii_lowercase)
    print(f"Алфавит: '{en}'.")

    # 2) Выведем буквы алфавита
    en.print_letters()

    # 3) Выведем количество букв в алфавите
    print(f"Число букв в '{en.language}' алфавите: {en.letters_num()}.")

    # 4) Проверим, относится ли символ 'F' к английскому алфавиту
    test_letter = "F"
    print("Буква '{0}' {1} к английскому алфавиту.".format(test_letter,
                                                        ("относится" if en.is_en_letter(test_letter) else
                                                         "не относится")))

    # 5) Проверим, относится ли символ 'Щ' к английскому алфавиту
    test_letter = "Щ"
    print("Буква '{0}' {1} к английскому алфавиту.".format(test_letter,
                                                        ("относится" if en.is_en_letter(test_letter) else
                                                         "не относится")))

    # 6) Выведем пример текста на английском языке:
    print(f"Пример текста: '{EngAlphabet.example()}'.")
```
_В результате выполнения данного кода в командной строке получим следующее:_
```
Алфавит: 'EN'.
Буквы 'EN' алфавита: abcdefghijklmnopqrstuvwxyz.
Число букв в 'EN' алфавите: 26.
Буква 'F' относится к английскому алфавиту.
Буква 'Щ' не относится к английскому алфавиту.
Пример текста: 'Example of simple english language text'.
```