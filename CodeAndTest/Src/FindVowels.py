'''find index of the vowels in a given word
IP super OP 2,4'''

def vowel_indices(word):
    vowel = "aeiouyAEIOUY"
    vowel_idx = []
    for idx, letter in enumerate(word, 1):
        if letter in vowel:
            vowel_idx.append(idx)
    return vowel_idx

print vowel_indices('super')
print vowel_indices('aeiouy')