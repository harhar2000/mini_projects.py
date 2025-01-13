# Write a function taking a list of words and returning a string listing all words longer than 10 characters
#   which don’t contain a hyphen. If any word is longer than 15 characters, 
#   truncate it to 15 characters and add "..." at the end.

words = [
  'hello',
  'nonbiological',
  'Kay',
  'this-is-a-long-word',
  'antidisestablishmentarianism'
]

output = []

for word in words:
    if len(word) > 10 and "-" not in word:
            if len(word) > 15:
                word = word[:15] + "..."
            output.append(word)

result = f"These words are quite long: {', '.join(output)}"
print(result)