#!/usr/bin/env python3

import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff import loader


def test_generate_diff_json():
    file1, file2 = loader.load_file('before.json', 'after.json')
    val = generate_diff(file1, file2)
    g = open("tests/fixtures/test.txt", "r")
    contentsg = g.read()
    assert val == contentsg


def test_generate_diff_yml():
    file1, file2 = loader.load_file('before.yml', 'after.yml')
    val = generate_diff(file1, file2)
    g = open("tests/fixtures/test.txt", "r")
    contentsg = g.read()
    assert val == contentsg
