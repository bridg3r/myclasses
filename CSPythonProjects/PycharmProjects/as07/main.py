text = open('/Users/bridg3r/PycharmProjects/as07/number_names.txt')
number_words = text.readlines()
number_words2 = {}
for i in number_words:
    j = i.split()
    number_words2[int(j[1])] = j[0]


def verbalize(value, total=()):
    if value == 0 and len(total) == 0:  # start value is 0
        return ['zero']
    if value < 1000:  # base case, 3 digits or less
        total = list(total)
        sub_total = []
        digit100 = 0
        if value > 99:  # getting 3rd digit
            digit100 = value // 100
            sub_total.append(number_words2[digit100] + ' hundred')
            value = value - (digit100 * 100)
        digit10 = 0
        if value > 19:
            digit10 = value // 10
            sub_total.append(number_words2[digit10 * 10])
            value = value - (digit10 * 10)
        if value > 0 and digit10 == 0:  # all values 19 and less
            sub_total.append(number_words2[value])
        if digit10 != 0 and value > 0:  # value should be 1 digit only
            sub_total[-1] += '-' + number_words2[value]
        if value == 0 and digit100 == 0 and digit10 == 0:
            return total
        total.append(' '.join(sub_total))
        return total
    value = str(value)
    digits = len(value)
    if digits % 3 != 0:
        sector = digits % 3
    else:
        sector = 3
    sectors = int(value[0:sector])
    total = list(total) + verbalize(sectors)
    magnitude = 10 ** (((digits - 1) // 3) * 3)
    total[-1] += ' ' + number_words2[magnitude]
    return verbalize(int(value[sector:]), total)

print(verbalize(100000))
print(verbalize(107988703579833055175800411289501875397604312987276878350070958531648521902242132125704161671600119124158008562688196239023266720652904207870776278842149377684812671830287520118503563088348126401895404613782147168913864667405475586160768107742278737237772943516151933069189143154686833472722140751175))