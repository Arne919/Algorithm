'''
00000000000000000000110001011110101101110010011011110100100110011001001001100000
'''
M = 70
code = '0000011101101100010111011011000101100010001101001001101110110000000000'
for j in range(M-1, -1, -1):
    if code[j] == '1':
        k = j
        break

real_code = []
for l in range(k-55,k+1,7):
    real_code.append([code[l:l+7]])
print(real_code)