# this is to help Yoonbin Cho to solve her problem

def q_1():
    nest_list = [12, 13, [14, 15], [16, [17, 18, ["weather change!"]], 19, 20], 21, 22]
    word = nest_list[3][1][2][0]

    return word


print(q_1())
