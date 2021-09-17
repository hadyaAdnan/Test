import math


def main():
    data = []
    with open('A2_input.txt', 'r') as file:
        for line in file:
            data.append(line.strip().split('\t'))
        while True:
            answer = int(input('Please choose one of the options:\n'
                               'option 1: See the record of one patient\n'
                               'option 2: see the records of 3 patients\n'
                               'option 3: Exit\n'))

            if answer == 1:
                patientNum = input('Please enter Patient Number from 1 to 5 inclusive : ')
                while int(patientNum) < 0 or int(patientNum) > 5:
                    patientNum = input('ERROR!: Please enter Patient Number from 1 to 5 inclusive : ')
                pNum = int(patientNum)
                countOfRecords = analyzeData(pNum, data)
                average = analyzeData(pNum, data)
                print(str(countOfRecords) + 'records found for patient number ' + str(pNum) + '\n The average half '
                                                                                              'life is ' + str(average))
            if answer == 2:
                patientNum1 = int(input('Please enter Patient Number from 1 to 5 inclusive : '))
                while patientNum1 < 0 or patientNum1 > 5:
                    patientNum1 = int(input('ERROR!: Please enter Patient Number from 1 to 5 inclusive : '))

                patientNum2 = int(input('Please enter Patient Number from 1 to 5 inclusive : '))
                while patientNum2 < 0 or patientNum2 > 5:
                    patientNum2 = int(input('ERROR!: Please enter Patient Number from 1 to 5 inclusive : '))

                patientNum3 = int(input('Please enter Patient Number from 1 to 5 inclusive : '))
                while patientNum3 < 0 or patientNum3 > 5:
                    patientNum3 = int(input('ERROR!: Please enter Patient Number from 1 to 5 inclusive : '))

                averageLife = longest(patientNum1, patientNum2, patientNum3, data)
                longestLife = longest(patientNum1, patientNum2, patientNum3, data)
                print('The average Life of patients ' + str(patientNum1) + ', ' + str(patientNum2), ' and ' + str(patientNum3) + ' is ' + str(averageLife))
                print('The longest Life among patients ' + str(patientNum1) + ', ' + str(patientNum2) + ' and ' + str(patientNum3) + ' is ' + str(longestLife))

            elif answer == 3:
                exit()
            else:
                print('The option you choose is invalid')


def analyzeData(p, data):
    averageLife = 0
    numOfRecords = 0
    for patient in data:
        if p == patient[0]:
            numOfRecords += 1
            averageLife += halfLife(patient[1], patient[2], patient[3])
            averageLife /= numOfRecords
    return averageLife, numOfRecords


def halfLife(c0, ct, t):
    k = 0.95
    t_half = -k * float(t) * (math.log(2) / math.log(int(ct) / int(c0)))
    return t_half


def longest(p1, p2, p3, data):
    avgLife1 = analyzeData(p1, data)

    avgLife2 = analyzeData(p2, data)

    avgLife3 = analyzeData(p3, data)

    averageLives = (avgLife1 + avgLife2 + avgLife3) / 3

    longestLife = max(avgLife1, max(avgLife2, avgLife3))

    return averageLives, longestLife


main()
