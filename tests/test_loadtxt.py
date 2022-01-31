from loadtxt.loadtxt.loadtxt import new


def test_new():
    expected = 'Note that None as a type hint is a special case and is replaced.'.strip()
    actual = new('Note that None as a type hint is a special case and is replaced.').strip()
    assert actual == expected


def test_new_file():
    expected = 'Insanity is doing the same thing over and over and expecting different results.'.strip()
    actual = new('/Users/smikhail/Public/libs/loadtxt/loadtxt/tests/text.txt').strip()
    assert actual == expected

