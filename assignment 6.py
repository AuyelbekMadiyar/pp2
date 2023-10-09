strings = int(input())
words_bili = set()
words = set()
for _ in range(strings):
    strings = input()
    words = strings.split()
    words_bili.update(words)
print(len(words_bili))
