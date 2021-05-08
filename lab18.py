words = ["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]
full_string = "".join(words)
rates_global = {}

for c in full_string:
    if c not in rates_global.keys():
        rates_global[c] = full_string.count(c) / len(full_string)

print("Введите слово")
word = input()
chance = 1
for c in word:
    chance *= rates_global[c]

print(chance)


