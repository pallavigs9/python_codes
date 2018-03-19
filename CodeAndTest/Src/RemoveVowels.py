def vowel_removal(string):
    vowel = "aeiouAEIOU"
    new_str = ''

    for i in string:
        if i not in vowel:
            new_str = new_str + i
    return new_str

print vowel_removal("This website is for losers LOL!")

