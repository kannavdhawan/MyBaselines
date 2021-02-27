def split_char(str):
    # char_split = []
    # char_split[:0] = str
    # char_split = str.split('')
    char_split = []
    for i in str:
        char_split.append(i)
    return char_split

print(split_char('abcd'))


