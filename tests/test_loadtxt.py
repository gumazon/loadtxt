import shlex
import subprocess

from loadtxt.loadtxt import loadtxt


def test_main_txt():
    expected = 'Same thing over and over and expecting different results.'
    cmd = 'python /Users/smikhail/Public/libs/loadtxt/loadtxt/loadtxt "Same thing over and over and expecting different results."'
    actual = subprocess.run(shlex.split(cmd), check=True, stdout=subprocess.PIPE).stdout.decode().strip()
    assert actual == expected


def test_main_file():
    expected = 'Insanity is doing the same thing over and over and expecting different results.'
    cmd = 'python /Users/smikhail/Public/libs/loadtxt/loadtxt/loadtxt "/Users/smikhail/Public/libs/loadtxt/loadtxt/tests/text.txt"'
    actual = subprocess.run(shlex.split(cmd), check=True, stdout=subprocess.PIPE).stdout.decode().strip()
    assert actual == expected


def test_loadtxt():
    expected = 'Note that None as a type hint is a special case and is replaced.'.strip()
    actual = loadtxt.loadtxt('Note that None as a type hint is a special case and is replaced.').strip()
    assert actual == expected


def test_loadtxt_file():
    expected = 'Insanity is doing the same thing over and over and expecting different results.'.strip()
    actual = loadtxt.loadtxt('/Users/smikhail/Public/libs/loadtxt/loadtxt/tests/text.txt').strip()
    assert actual == expected

