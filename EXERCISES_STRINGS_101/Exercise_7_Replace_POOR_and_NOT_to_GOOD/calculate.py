def replaceToGOOD(str1):
    str_NOT = "not"
    str_POOR = "poor"

    position_NOT = str1.find(str_NOT)
    position_POOR = str1.find(str_POOR)

    if position_NOT < position_POOR and position_POOR > 0 and position_NOT > 0:
        result_str= str1[:position_NOT] + "good" + str1[position_POOR + 4:]
        return result_str


def replaceToGOOD1(str1):
    str_NOT = "not"
    str_POOR = "poor"

    position_NOT = str1.find(str_NOT)
    position_POOR = str1.find(str_POOR)

    if position_NOT < position_POOR and position_POOR > 0 and position_NOT > 0:
        result_str = str1.replace(str1[position_NOT:position_POOR + 4], "GOOD")
        return result_str


str1 = "the lyrics is not that poor and not bad"

print(replaceToGOOD(str1))
print(replaceToGOOD1(str1))
