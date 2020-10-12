# program to count vowels count in a sentence

sentence_str = 'HellO, have you tried our tutorial section yet?'
sentence_str = sentence_str.casefold()

a_count = e_count = i_count = o_count = u_count = 0
for c in sentence_str:
    if c == 'a':
        a_count += 1
    elif c == 'e':
        e_count += 1
    elif c == 'i':
        i_count += 1
    elif c == 'o':
        o_count += 1
    elif c == 'u':
        u_count += 1
    else:
        pass

print("a=", a_count, "e=", e_count, "i=", i_count, "o=", o_count, "u=", u_count)
