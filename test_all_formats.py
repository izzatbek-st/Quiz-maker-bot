#!/usr/bin/env python3
"""Test all format parsers with poll-style display"""

from test_parser import TestParser

def display_poll(test_num, test_name, questions, format_type):
    """Display quiz in poll interface style"""
    print("\n")
    print("┌" + "─" * 78 + "┐")
    print("│" + f" TEST {test_num}: {test_name}".ljust(78) + "│")
    print("├" + "─" * 78 + "┤")
    
    for q_idx, q in enumerate(questions, 1):
        print("│" + " " * 78 + "│")
        print("│" + f"  📋 Quiz Test #{q_idx}".ljust(78) + "│")
        print("│" + f"  Anonymous Poll".ljust(78) + "│")
        print("│" + " " * 78 + "│")
        print("│" + f"  ❓ {q['question']}".ljust(78) + "│")
        print("│" + " " * 78 + "│")
        
        # Display options with checkboxes
        for opt_idx, option in enumerate(q['options']):
            checkbox = "☑️ " if opt_idx == q.get('correct_option_id', -1) else "☐ "
            option_text = f"{checkbox}{option}"
            print("│" + f"  {option_text}".ljust(78) + "│")
        
        print("│" + " " * 78 + "│")
        print("│" + "  [Vote]".ljust(78) + "│")
        print("│" + " " * 78 + "│")
        print("│" + f"  ❤️  {q_idx}    👁 {len(q['options'])} votes    23:58".ljust(78) + "│")
        print("├" + "─" * 78 + "┤")
    
    print("│" + f" Format: {format_type} | Total Questions: {len(questions)}".ljust(78) + "│")
    print("└" + "─" * 78 + "┘")

# Test 1: Simple Numbered format
test1 = """1 Olma nima?
a meva
b piyoz
c sabzavot

2 Tog'o nima?
a tepa
b yomg'in
c suv"""

q1, fmt1 = TestParser.parse(test1)
display_poll(1, "Simple Numbered Format", q1, fmt1)

# Test 2: Numbered with parenthesis (original)
test2 = """1) Olma nima?
a) meva
b) piyoz (correct)
c) sabzavot

2) Tog'o nima?
a) tepa
b) yomg'in (correct)
c) suv"""

q2, fmt2 = TestParser.parse(test2)
display_poll(2, "Numbered Format (with parenthesis)", q2, fmt2)

# Test 3: Q/A Format
test3 = """Q: Olma nima?
A: meva
A: piyoz
A: sabzavot*

Q: Tog'o nima?
A: tepa*
A: yomg'in
A: suv"""

q3, fmt3 = TestParser.parse(test3)
display_poll(3, "Q/A Format", q3, fmt3)

# Test 4: Unnumbered format
test4 = """Olma nima?
meva
piyoz
sabzavot

Tog'o nima?
tepa
yomg'in
suv"""

q4, fmt4 = TestParser.parse(test4)
display_poll(4, "Unnumbered Format", q4, fmt4)

# Test 5: Mixed with correct markers
test5 = """1 Olma nima?
a meva*
b piyoz
c sabzavot

2 Tog'o nima?
a tepa
b yomg'in (to'g'ri)
c suv"""

q5, fmt5 = TestParser.parse(test5)
display_poll(5, "Simple Numbered with correct marker", q5, fmt5)

print("\n" + "╔" + "═" * 78 + "╗")
print("║" + "✅ All tests completed successfully!".center(78) + "║")
print("╚" + "═" * 78 + "╝")
