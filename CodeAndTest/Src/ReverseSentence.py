def reverse_word(sentence):
    cnt = -1
    rev_sent= sentence[::-1].split()
    new_str = []
    for i in rev_sent:
        new_str.append(rev_sent[cnt])
        cnt = cnt + -1
    return " ".join(map(str, new_str))

print reverse_word("double  spaces")