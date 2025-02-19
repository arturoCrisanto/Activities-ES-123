# Prelim: Modify and Calculate from a String

## Objective:

### Create a Python program that:

1. Takes a user-inputted string containing numbers separated by spaces.
2. Uses `.split()` to extract the numbers.
3. Uses `.replace()` to modify a specific digit (e.g., replace all `0` with `5`).
4. Converts the modified numbers back to integers and calculates their sum.

---

## Instructions:

1. Ask the user to enter numbers separated by spaces (e.g., "`120 305 789`").
2. Use `.replace()` to replace all `0s` with `5`.
3. Split the string into a list of numbers using `.split()`.
4. Convert the modified numbers to integers.
5. Calculate and display the sum of the modified numbers.

---

Example Outputs:
Output 1:

```yaml
Enter numbers: 120 305 789
Modified numbers: 125, 355, 789
Sum of modified numbers: 1269
```

Output 2:

```yaml
Enter numbers: 10 200 304
Modified numbers: 15, 255, 354
Sum of modified numbers: 624
```

## Hint

```python
total_sum = sum(modified_numbers_int)

print("Modified numbers:" + modified_numbers)
print("Sum of modified numbers:", total_sum)
```
