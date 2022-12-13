# this is to help Yoonbin Cho to solve her problem

def q_1():
    nest_list = [12, 13, [14, 15], [16, [17, 18, ["weather change!"]], 19, 20], 21, 22]
    word = nest_list[3][1][2][0]

    return word


# print(q_1())
def q_2():
    d = {'key1': [1, 2, 3, {'key1_1': ['Modeling', 'of', 'Estimation', {'key1_2': [1, 2, 3, 'Weather Change!']}]}]}
    # START YOUR CODE HERE
    dic_word = d['key1'][3]['key1_1'][3]['key1_2'][3]

    # LAST LINE
    return dic_word


# print(q_2())
def q_3(email):
    # START YOUR CODE HERE
    print(email)
    ans3 = email.split('@')[0]

    # LAST LINE
    return ans3


# print(q_3("fbdxodla@naver.com"))
def q_4(st):
    # START YOUR CODE HERE
    if st.lower().find('weather') == -1:
        ans4 = False
    else:
        ans4 = True

    # LAST LINE
    return ans4


# print(q_4("The Weather is cold today!"))
def q_5(st):
    # START YOUR CODE HERE
    ans5 = st.count('weather')

    # LAST LINE
    return ans5


# print(q_5('This weather is better than the weather of yesterday!'))
def q_6(st):
    # START YOUR CODE HERE
    ans6 = ''
    for le in range(0, len(st)):
        ans6 += st[len(st)-le-1]

    # LAST LINE
    return ans6


# print(q_6('1234567890abcdefghijk'))
def q_7(num):
    # START YOUR CODE HERE
    if num % 2 == 0:
        ans7 = 'Even'
    else:
        ans7 = 'Odd'

    return ans7


# print(q_7(12))
def q_8(lst):
    for i in range(0, 3):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    ans8 = lst[-3:]
    return ans8


# print(q_8([2,4,12,3,7,1,9]))
def q_9(num):
    while num >= 10:
        num //= 10
    ans9 = num

    return ans9


# print(q_9(785893))
def q_10(lst):
    i = 0
    j = 0
    while i < len(lst)-1:
        while j < len(lst)-i-1:
            if lst[j] < lst[j+1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1
        j = 0

    ans10 = lst
    return ans10


# print(q_10([1,2,3,4,5]))

st = "hello"
print(st)