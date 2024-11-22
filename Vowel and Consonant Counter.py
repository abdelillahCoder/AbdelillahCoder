def count_vowels_and_consonants():
    text = input("Enter a text: ")
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
            
    print(f"The text contains {vowel_count} vowels and {consonant_count} consonants.")

count_vowels_and_consonants()
