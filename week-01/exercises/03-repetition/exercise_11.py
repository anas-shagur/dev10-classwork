# DOUBLE IT
phrase = input("Enter a word: ")

# 1. Write a loop that "doubles" each character in a user-entered word.
# You'll need a new string variable to store the result.
# 2. Print the result.

# Examples
# ===============
# "dog" -> "ddoogg"
# "what?" -> "wwhhaatt??"
# "" -> "" (empty string has nothing to double)
# " " -> "  " (but whitespace should be doubled)
# "open & shut" -> "ooppeenn  &&  sshhuutt"
# "Eep" -> "EEeepp"

result = ""

for i in range(len(phrase)):
    result += phrase[i] + phrase[i] 

print(result)