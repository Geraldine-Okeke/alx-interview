# Making Changes

## Requirements

### General

- Allowed editors: vi, vim, emacs
- Files interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- Files end with a new line
- The first line of files: #!/usr/bin/python3
- Mandatory README.md at project root
- Code follows PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Change comes from within (mandatory)

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet total
- If total is 0 or less, return 0
- If total cannot be met by any coins, return -1
- `coins` is a list of coin values
- Value of a coin always > 0
- Assume infinite number of each denomination
- Solution runtime will be evaluated

## Examples

```python
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```
