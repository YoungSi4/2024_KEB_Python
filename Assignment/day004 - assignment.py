# Day4 Assignment
# 책 예제 205p 8.1 ~ 8.10

# # 8.1
# # 영어 - 프랑스어 사전을 만들어보자
# e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
# print(e2f)

# # 8.2
# # e2f 딕셔너리에서 영어 walrus를 프랑스어로 출력해보자
# print(e2f['walrus'])

# # 8.3
# # e2f 딕셔너리에서 f2e 딕셔너리라는 프랑스어-영어 사전을 만들어보자
# # (item 메서드 사용) / 리버스가 없나
# f2e = {}
# for eng, fre in list(e2f.items()):
#     f2e[fre] = eng
# print(f2e)

# # 8.4 e2f 딕셔너리를 사용해서 프랑스어 chien을 출력해보자
# print(f2e["chien"])

# 8.5 e2f의 영어 단어 키들을 출력해보자
# print(e2f.keys())

# -----------------------------------------------------------------------------

# # 8.6 이차원 딕셔너리 life를 만들어보자. 최상위 키는 'animals', 'plant', 'others'
# # 그리고 'animals'는 각각 'cat', 'octopi', 'emus'를 키로 하고
# # 'Henri', 'Grumpy', 'Lucy'를 값으로 하는 또 다른 딕셔너리를 참조하고 있다.
# # 나머지 요소는 빈 딕셔너리를 참조한다
#
# Life = {'animals' : {'cat':'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, 'plants' : {}, 'others' :{}}
#
# # 8.7 Life 딕셔너리의 최상위 키를 출력해보자
# print(Life.keys())
#
# # 8.8 Life['animals'] 의 모든 키를 출력해보자
# print(Life['animals'].keys())
#
# # 8.9 Life['animals']['cat']의 모든 값을 출력해보자
# print(Life['animals']['cat'])

# -----------------------------------------------------------------------------

# # 8.10 딕셔너리 컴프리헨션으로 squares 딕셔너리를 생성한다 range(10)를 키로 하고, 각 키의 제곱을 값으로 한다.
#
# squares = { keys : keys*keys for keys in range(10)}
# print(squares)
