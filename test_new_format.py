#!/usr/bin/env python3
"""Test the new simple numbered format parser"""

from test_parser import TestParser

# Test the new simple numbered format
test_text = """1 Olma nima?
a meva
b piyoz
c sabzavot

2 Nok nima?
a piyoz
b meva
c sabzavot

3 Qo'ng'ir rang nima?
a rang
b shaxs
c hisob"""

questions, fmt = TestParser.parse(test_text)
print(f'Format: {fmt}')
print(f'Questions found: {len(questions)}')
for i, q in enumerate(questions, 1):
    print(f'\nQ{i}: {q["question"]}')
    for j, opt in enumerate(q['options']):
        marker = ' ✓' if j == q['correct_option_id'] else ''
        print(f'  {chr(97+j)}) {opt}{marker}')
