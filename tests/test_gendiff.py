#!/usr/bin/env python3

from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.gendiff import formatter
from gendiff import loader


def test_generate_diff_json():
    file1, file2 = loader.load_file('before_flat.json', 'after_flat.json')
    val = formatter(generate_diff(file1, file2))
    g = open("tests/fixtures/test_flat.txt", "r")
    contentsg = g.read()
    assert val == contentsg
    file1, file2 = loader.load_file('before.json', 'after.json')
    val = formatter(generate_diff(file1, file2))
    g = open("tests/fixtures/test_tree.txt", "r")
    contentsg = g.read()


def test_generate_diff_yml():
    file1, file2 = loader.load_file('before_flat.yml', 'after_flat.yml')
    val = formatter(generate_diff(file1, file2))
    g = open("tests/fixtures/test_flat.txt", "r")
    contentsg = g.read()
    assert val == contentsg
    file1, file2 = loader.load_file('before.yml', 'after.yml')
    val = formatter(generate_diff(file1, file2))
    g = open("tests/fixtures/test_tree.txt", "r")
    contentsg = g.read()
