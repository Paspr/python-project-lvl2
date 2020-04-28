#!/usr/bin/env python3

import pytest
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
  val = generate_diff('before.json', 'after.json')
  g = open("tests/fixtures/test.txt", "r")
  contentsg = g.read()
  assert val == contentsg
  