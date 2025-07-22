# Contact Center Coding Challenge

This repository contains a Python solution to the Contact Center Coding Challenge, which involves finding all occurrences of a given subtext within a larger text, with restricting the usage of some built in method for string mainpulation.

## Problem Statement

We need a way of finding all the occurrences of a particular set of characters in a string. It should:
* Accept two strings as input: `textToSearch` and `subtext`.
* The solution should match the `subtext` against the `textToSearch`, outputting the positions of the beginning of each match for the `subtext` within the `textToSearch`.
* Multiple matches are possible.
* Matching is case-insensitive.
* If no matches have been found, no output is generated.

**Constraints:**
* Do not use any extended functionality of the framework to solve this problem (e.g., `IndexOf`, `substring`, regular expression classes, LINQ, etc.).
* For Python, this means avoiding built-in string methods that perform complex searching or slicing.
* **Permitted:** `len()` for string length and direct indexing `string[index]` for character access are allowed. `.lower()` for case conversion is also used as a fundamental operation.


## Solution Overview

The `find_all_occurrences` function implements a manual string search algorithm. It iterates through the `textToSearch` using an outer loop (`outer_loop_index`) to define potential starting points for a match. For each potential starting point, an inner loop (`inner_loop_index`) performs a character-by-character comparison of the `subtext` against the corresponding segment of the `textToSearch`.

Key aspects of the solution:
* **Case-Insensitivity:** Both `textToSearch` and `subtext` are converted to lowercase at the beginning to simplify comparisons.
* **Manual Comparison:** Direct character access (`string[index]`) is used within the inner loop to compare characters.
* **Early Termination:** When the first character of `outer_loop_index` and `inner_loop_index` are not matched, we terminate the inner loop to go for the next character.
* **Plus-One-Indexed Positions:** Match positions are converted to indexed plus one before being stored, as question asked for the index of the character.
* **Multiple Matches:** The outer loop continues searching after finding a match, incrementing `inner_loop_index` with the for loop to find all possible (including potentially overlapping) occurrences.


### Running the Main Script (Optional)

You can run `script.py` directly to see some hardcoded examples:

```bash
python script.py
```

### Running the Tests

```bash
python test_script.py
```