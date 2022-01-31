import shlex
import subprocess
import sys

from loadtxt.loadtxt import loadtxt



def test_main():
    expected = 'Some PS1 - Note that None as a type hint is a special case and is replaced.'.strip()
    _path = '/Users/smikhail/Public/libs/loadtxt/loadtxt'
    _str = 'Some PS1 - Note that None as a type hint is a special case and is replaced.'
    actual = subprocess.Popen(shlex.split('python loadtxt '+_str)).returncode
    assert actual == expected

def test_loadtxt():
    expected = 'Note that None as a type hint is a special case and is replaced.'.strip()
    actual = loadtxt('Note that None as a type hint is a special case and is replaced.').strip()
    assert actual == expected


def test_loadtxt_file():
    expected = 'Insanity is doing the same thing over and over and expecting different results.'.strip()
    actual = loadtxt('/Users/smikhail/Public/libs/loadtxt/loadtxt/tests/text.txt').strip()
    assert actual == expected

