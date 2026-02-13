import pytest
import json
import random

from build_sentences import (
    get_seven_letter_word,
    parse_json_from_file,
    choose_sentence_structure,
    get_pronoun,
    get_article,
    get_word,
    fix_agreement,
    build_sentence,
    structures
)

# ----------------------------
# get_seven_letter_word
# ----------------------------

def test_get_seven_letter_word_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "testinggg")
    word = get_seven_letter_word()
    assert word == "TESTINGGG"


def test_get_seven_letter_word_invalid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "short")
    with pytest.raises(ValueError):
        get_seven_letter_word()


# ----------------------------
# parse_json_from_file
# ----------------------------

def test_parse_json_from_file(tmp_path):
    data = {"nouns": ["dog"], "verbs": ["run"]}
    file = tmp_path / "test.json"
    file.write_text(json.dumps(data))

    result = parse_json_from_file(file)
    assert result == data


# ----------------------------
# choose_sentence_structure
# ----------------------------

def test_choose_sentence_structure():
    structure = choose_sentence_structure()
    assert structure in structures


# ----------------------------
# get_pronoun
# ----------------------------

def test_get_pronoun():
    pronoun = get_pronoun()
    assert pronoun in ["he", "she", "they", "I", "we"]


# ----------------------------
# get_article
# ----------------------------

def test_get_article():
    article = get_article()
    assert article in ["a", "the"]


# ----------------------------
# get_word
# ----------------------------

def test_get_word():
    words = ["apple", "banana", "cherry"]
    result = get_word("A", words)
    assert result == "apple"


# ----------------------------
# fix_agreement
# ----------------------------

def test_fix_agreement_he():
    sentence = ["he", "quickly", "run"]
    fix_agreement(sentence)
    assert sentence == ["he", "quickly", "runs"]


def test_fix_agreement_a_to_an():
    sentence = ["a", "big", "apple"]
    fix_agreement(sentence)
    assert sentence == ["an", "big", "apple"]


def test_fix_agreement_the_at_start():
    sentence = ["the", "big", "dog", "quickly", "run"]
    fix_agreement(sentence)
    assert sentence == ["the", "big", "dog", "quickly", "runs"]


# ----------------------------
# build_sentence
# ----------------------------

def test_build_sentence_with_prep():
    seed_word = "ABCDEFGH"

    structure = ["PRO", "ADV", "VERB", "PREP", "ART", "ADJ", "NOUN"]

    data = {
        "adjectives": ["big","small","red","blue","fast","slow","old","new"],
        "nouns": ["dog","cat","car","tree","house","man","woman","child"],
        "verbs": ["run","eat","drive","see","jump","talk","play","watch"],
        "adverbs": ["quickly","slowly","well","badly","loudly","silently","today","now"],
        "prepositions": ["to","from","with","without","under","over","before","after"]
    }

    sentence = build_sentence(seed_word, structure, data)

    assert isinstance(sentence, str)
    assert len(sentence.split()) == len(structure)


