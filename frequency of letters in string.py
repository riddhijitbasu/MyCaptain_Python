from collections import Counter
test_str =input("Enter a string: ")
res = Counter(test_str)
print("Count of all characters in", test_str, "is :\n "
      + str(res))