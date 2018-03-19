def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        all_sum = sum(range(begin_number, end_number + 1, step))
        return all_sum

print sequence_sum(1, 5, 3)
print sequence_sum(16, 15, 3)
print sequence_sum(2, 2, 1)
print sequence_sum(0, 15, 3)