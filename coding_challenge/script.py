def find_all_occurrences(text_to_search, subtext):
    """
    Finds all occurrences of a subtext within a text regardless of its case.
    Assuming the permission of using len() and direct string indexing [].

    Args:
        text_to_search (str): The main text to search within.
        subtext (str): The subtext to search for.

    Returns:
        str: A comma-separated string of starting positions (1-indexed) of matches,
             or an empty string if no matches are found.
    """
    matches = []
    
    lower_text = text_to_search.lower()
    lower_subtext = subtext.lower()

    len_text = len(lower_text)
    len_subtext = len(lower_subtext)

    if len_subtext == 0:
        return ""

    for outer_loop_index in range(len_text-len_subtext+1):
        is_match = True

        for inner_loop_index in range(len_subtext):
            if lower_text[outer_loop_index+inner_loop_index] != lower_subtext[inner_loop_index]:
                is_match = False
                break

        if is_match:
            matches.append(str(outer_loop_index+1))
    
    return ", ".join(matches)


# --- Sample Acceptance Criteria ---
test_cases = [
    {
        "textToSearch": "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!",
        "subtext": "Peter",
        "expected": "1, 20, 75"
    },
    {
        "textToSearch": "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!",
        "subtext": "peter",
        "expected": "1, 20, 75"
    },
    {
        "textToSearch": "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!",
        "subtext": "pick",
        "expected": "30, 58"
    },
    {
        "textToSearch": "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!",
        "subtext": "pi",
        "expected": "30, 37, 43, 51, 58"
    },
    {
        "textToSearch": "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!",
        "subtext": "z",
        "expected": ""
    },
    {
        "textToSearch": "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!",
        "subtext": "Peterz",
        "expected": ""
    }
]

print("--- Running Tests ---")
for i, test_case in enumerate(test_cases):
    text = test_case["textToSearch"]
    sub = test_case["subtext"]
    expected = test_case["expected"]
    
    result = find_all_occurrences(text, sub)
    
    print(f"\nTest Case {i+1}:")
    print(f"Text: '{text}'")
    print(f"Subtext: '{sub}'")
    print(f"Expected: '{expected}'")
    print(f"Result:   '{result}'")
    
    if result == expected:
        print("Status: PASSED")
    else:
        print("Status: FAILED")

print("\n--- Tests Complete ---")