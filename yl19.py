text = input("sisesta text:")
vowels = "aieouüõäöAIEOUÜÕÄÖ"
count = sum(text.count(vowel) for vowel in vowels)
print(count)