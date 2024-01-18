# # 딕셔너리 컴프리헨션
# univ = 'inha university'
# count_alphabet = {letter : univ.count(letter) for letter in univ}
# print(count_alphabet)
#
# # 컴프리헨션 아닌 형태로
# univ = 'inha university'
# count_alphabet = dict()
# for letter in univ:
#     count_alphabet[letter] = univ.count(letter)
# print (count_alphabet)

# 과제 8.10
squares = {n : pow(n, 2) for n in range(10) } # n**2나 n*n으로 해도 된다.
print(squares)