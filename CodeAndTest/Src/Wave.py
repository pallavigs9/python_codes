def wave(word):
    simple = ','.join(word).split(',')
    wave_lst = []
    idx = 0

    for i in range(len(simple)):
        simple_copy = simple[:]
        simple_copy[idx] = simple_copy[idx].upper()
        if simple == simple_copy:
            pass
        else:
            wave_lst.append(''.join(map(str, simple_copy)))
        idx = idx + 1
        del simple_copy[:]

    return wave_lst

print wave('two words')


