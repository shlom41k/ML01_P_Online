from task import EngAlphabet
import pytest

@pytest.fixture
def eng_alphabet():
    return EngAlphabet()

def test_create_engalphabet(eng_alphabet):
    test_eng_alphabet = EngAlphabet()
    assert type(eng_alphabet) == type(test_eng_alphabet)

def test_get_letters(eng_alphabet):
    print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def test_letters_count(eng_alphabet):
    assert eng_alphabet.letters_num() == 26

def test_is_letter_in_alphabet_true(eng_alphabet):
    assert eng_alphabet.is_en_letter('F') is True

def test_is_letter_in_alphabet_false(eng_alphabet):
    assert eng_alphabet.is_en_letter('Щ') is False

def test_example(eng_alphabet):
    assert eng_alphabet.example() == "Hello, world!"