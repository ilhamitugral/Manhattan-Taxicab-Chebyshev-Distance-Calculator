import math

variable = [
    [0, 1, 2, 3, 4],
    [1, 0, 1, 2, 3],
    [2, 1, 0, 1, 2],
    [3, 2, 1, 0, 1],
    [4, 3, 2, 1, 0]
]


def calcManhattan(variable):
    print("----- Manhattan Uzaklığı Hesaplaması -----")
    for i in range(len(variable)):
        temp = variable[i]
        for j in range(len(variable[i])):
            print('|{0}-{1}|+|{2}-{3}|+|{4}-{5}|+|{6}-{7}|+|{8}-{9}| = ({10}+{11}+{12}+{13}+{14}) = {15}'.format(
                temp[0], variable[j][0],
                temp[1], variable[j][1],
                temp[2], variable[j][2],
                temp[3], variable[j][3],
                temp[4], variable[j][4],
                abs(temp[0] - variable[j][0]),
                abs(temp[1] - variable[j][1]),
                abs(temp[2] - variable[j][2]),
                abs(temp[3] - variable[j][3]),
                abs(temp[4] - variable[j][4]),
                abs(temp[0] - variable[j][0]) + abs(temp[1] - variable[j][1]) + abs(temp[2] - variable[j][2]) + abs(
                    temp[3] - variable[j][3]) + abs(temp[4] - variable[j][4])))
    print("\n")


def calcOklid(variable):
    print('----- Oklid Uzaklığı Hesaplaması -----')
    for i in range(len(variable)):
        for j in range(len(variable[i])):
            temp = variable[i]

            print('|{0}-{1}|²+|{2}-{3}|²+|{4}-{5}|²+|{6}-{7}|²+|{8}-{9}|²=√({10}+{11}+{12}+{13}+{14}) = √{15}'.format(
                temp[0], variable[j][0],
                temp[1], variable[j][1],
                temp[2], variable[j][2],
                temp[3], variable[j][3],
                temp[4], variable[j][4],
                int(math.sqrt(abs(temp[0] - variable[j][0]) ** 2)),
                int(math.sqrt(abs(temp[1] - variable[j][1]) ** 2)),
                int(math.sqrt(abs(temp[2] - variable[j][2]) ** 2)),
                int(math.sqrt(abs(temp[3] - variable[j][3]) ** 2)),
                int(math.sqrt(abs(temp[4] - variable[j][4]) ** 2)),
                # ----
                abs(temp[0] - variable[j][0]) ** 2 +
                abs(temp[1] - variable[j][1]) ** 2 +
                abs(temp[2] - variable[j][2]) ** 2 +
                abs(temp[3] - variable[j][3]) ** 2 +
                abs(temp[4] - variable[j][4]) ** 2))
    print("\n")


def calcCheby(variable):
    print('----- Chebyshev Uzaklığı Hesaplaması -----')
    for i in range(len(variable)):
        for j in range(len(variable[i])):
            temp = variable[i]
            maxValue = 0

            controlValues = [
                abs(temp[0] - variable[j][0]),
                abs(temp[1] - variable[j][1]),
                abs(temp[2] - variable[j][2]),
                abs(temp[3] - variable[j][3]),
                abs(temp[4] - variable[j][4])
            ]

            textValues = []

            for k in range(len(controlValues)):
                if controlValues[k] >= maxValue:
                    maxValue = controlValues[k]
                    textValues.append('<' + str(controlValues[k]) + '>')
                else:
                    textValues.append(' ' + str(controlValues[k]) + ' ')

            print('|{0}-{1}|,|{2}-{3}|,|{4}-{5}|,|{6}-{7}|,|{8}-{9}| = ({10},{11},{12},{13},{14})'.format(
                temp[0], variable[j][0],
                temp[1], variable[j][1],
                temp[2], variable[j][2],
                temp[3], variable[j][3],
                temp[4], variable[j][4],
                textValues[0],
                textValues[1],
                textValues[2],
                textValues[3],
                textValues[4]))


###########################################

calcManhattan(variable)
calcOklid(variable)
calcCheby(variable)
