import sys
#  data is - +91-9850-kitcat
fancy_number = sys.argv[1]

s_2_n = {}
s_2_n['A'] = s_2_n['B'] = s_2_n['C'] = 2
s_2_n['D'] = s_2_n['E'] = s_2_n['F'] = 3 
s_2_n['G'] = s_2_n['H'] = s_2_n['I'] = 4 
s_2_n['J'] = s_2_n['K'] = s_2_n['L'] = 5
s_2_n['M'] = s_2_n['N'] = s_2_n['O'] = 6 
s_2_n['P'] = s_2_n['Q'] = s_2_n['R'] = s_2_n['S'] = 7
s_2_n['T'] = s_2_n['U'] = s_2_n['V'] = 8
s_2_n['W'] = s_2_n['X'] = s_2_n['Y'] = s_2_n['Z'] = 9



non_fancy = ''
for f in fancy_number:
    f = f.upper()
    if f in s_2_n:
       non_fancy = non_fancy + str(s_2_n[f])
    else:
       non_fancy = non_fancy + f


print ("The number is: {}".format(non_fancy))



