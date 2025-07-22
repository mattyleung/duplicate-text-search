from script import find_all_occurrences

def run_tests():
    """
    Runs a series of predefined test cases for the find_all_occurrences function.
    """
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
        },
        {
            "textToSearch": "aaaaa",
            "subtext": "aa",
            "expected": "1, 2, 3, 4"
        },
        {
            "textToSearch": "Banana",
            "subtext": "an",
            "expected": "2, 4"
        },
        {
            "textToSearch": "TEST TEST TEST",
            "subtext": "test",
            "expected": "1, 6, 11"
        },

        # Overlapping matches (like 'aa' in 'aaaaa')
        {
            "textToSearch": "aaaaa",
            "subtext": "aa",
            "expected": "1, 2, 3, 4"
        },
        {
            "textToSearch": "ababab",
            "subtext": "aba",
            "expected": "1, 3"
        },
        {
            "textToSearch": "aaaa",
            "subtext": "aaa",
            "expected": "1, 2"
        },

        # Matches at boundaries
        {
            "textToSearch": "Hello World",
            "subtext": "hello",
            "expected": "1"
        },
        {
            "textToSearch": "Hello World",
            "subtext": "world",
            "expected": "7"
        },
        {
            "textToSearch": "Test",
            "subtext": "test",
            "expected": "1"
        },

        # Subtext is longer than text (should return no output)
        {
            "textToSearch": "short",
            "subtext": "longertext",
            "expected": ""
        },
        {
            "textToSearch": "a",
            "subtext": "aa",
            "expected": ""
        },

        # Subtext is the entire text
        {
            "textToSearch": "Exact Match",
            "subtext": "exact match",
            "expected": "1"
        },

        # Single character subtext
        {
            "textToSearch": "Mississippi",
            "subtext": "i",
            "expected": "2, 5, 8, 11"
        },
        {
            "textToSearch": "zzzz",
            "subtext": "z",
            "expected": "1, 2, 3, 4"
        },
        {
            "textToSearch": "AbC",
            "subtext": "b",
            "expected": "2"
        },

        # Empty textToSearch
        {
            "textToSearch": "",
            "subtext": "test",
            "expected": ""
        },
        {
            "textToSearch": "",
            "subtext": "",
            "expected": ""
        },

        # No match found (more scenarios)
        {
            "textToSearch": "apple",
            "subtext": "banana",
            "expected": ""
        },
        {
            "textToSearch": "test",
            "subtext": "tst",
            "expected": ""
        },
        {
            "textToSearch": "This is a Test",
            "subtext": "test_word",
            "expected": ""
        },

        # Text with spaces and punctuation
        {
            "textToSearch": "Hello, world! Hello, python.",
            "subtext": "hello",
            "expected": "1, 15"
        },
        {
            "textToSearch": "Hello, world! Hello, python.",
            "subtext": "world!",
            "expected": "8"
        },
    ]

    print("--- Running Tests for find_all_occurrences ---")
    all_passed = True
    for i, test_case in enumerate(test_cases):
        text = test_case["textToSearch"]
        sub = test_case["subtext"]
        expected = test_case["expected"]
        
        result = find_all_occurrences(text, sub)
        
        print(f"\nTest Case {i+1}:")
        print(f"Text: '{text}'")
        print(f"Subtext: '{sub}'")
        print(f"Expected: '{expected}'")
        print(f"Result: '{result}'")
        
        if result == expected:
            print("Status: PASSED")
        else:
            print("Status: FAILED")
            all_passed = False

    print("\n--- Tests Complete ---")
    if all_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests FAILED.")

if __name__ == "__main__":
    run_tests()