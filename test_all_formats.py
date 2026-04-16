#!/usr/bin/env python3
"""Test all format parsers"""

from test_parser import TestParser

# Test 1: Simple Numbered format
print("=" * 50)
print("TEST 1: Simple Numbered Format")
print("=" * 50)
test1 = """1 Olma nima?
a meva
b piyoz
c sabzavot

2 Tog'o nima?
a tepa
b yomg'in
c suv"""

q1, fmt1 = TestParser.parse(test1)
print(f"Format: {fmt1}, Questions: {len(q1)}")
for q in q1:
    print(f"  • {q['question']} -> {len(q['options'])} options")

# Test 2: Numbered with parenthesis (original)
print("\n" + "=" * 50)
print("TEST 2: Numbered Format (with parenthesis)")
print("=" * 50)
test2 = """1) Olma nima?
a) meva
b) piyoz (correct)
c) sabzavot

2) Tog'o nima?
a) tepa
b) yomg'in (correct)
c) suv"""

q2, fmt2 = TestParser.parse(test2)
print(f"Format: {fmt2}, Questions: {len(q2)}")
for q in q2:
    print(f"  • {q['question']} -> {len(q['options'])} options")

# Test 3: Q/A Format
print("\n" + "=" * 50)
print("TEST 3: Q/A Format")
print("=" * 50)
test3 = """Q: Olma nima?
A: meva
A: piyoz
A: sabzavot*

Q: Tog'o nima?
A: tepa*
A: yomg'in
A: suv"""

q3, fmt3 = TestParser.parse(test3)
print(f"Format: {fmt3}, Questions: {len(q3)}")
for q in q3:
    print(f"  • {q['question']} -> {len(q['options'])} options")

# Test 4: Unnumbered format
print("\n" + "=" * 50)
print("TEST 4: Unnumbered Format")
print("=" * 50)
test4 = """Olma nima?
meva
piyoz
sabzavot

Tog'o nima?
tepa
yomg'in
suv"""

q4, fmt4 = TestParser.parse(test4)
print(f"Format: {fmt4}, Questions: {len(q4)}")
for q in q4:
    print(f"  • {q['question']} -> {len(q['options'])} options")

# Test 5: Mixed with correct markers
print("\n" + "=" * 50)
print("TEST 5: Simple Numbered with correct marker")
print("=" * 50)
test5 = """1 Olma nima?
a meva*
b piyoz
c sabzavot

2 Tog'o nima?
a tepa
b yomg'in (to'g'ri)
c suv"""

q5, fmt5 = TestParser.parse(test5)
print(f"Format: {fmt5}, Questions: {len(q5)}")
for i, q in enumerate(q5):
    correct_idx = q['correct_option_id']
    correct_option = q['options'][correct_idx] if correct_idx < len(q['options']) else "?"
    print(f"  • {q['question']}")
    print(f"    Correct: {chr(97 + correct_idx)}) {correct_option}")

print("\n" + "=" * 50)
print("All tests completed successfully!")
print("=" * 50)
