
print("")
deleteValue = {"FORTY": 40, "FIFTY": 50}

print("Set A =", deleteValue)

numValues = {'TEN': 10,
              'TWENTY': 20,
              'THIRTY': 30,
             'FORTY': 40,
             'FIFTY': 50}
print("Set B =", numValues)
print("")

for key, value in dict(numValues).items():
    if value == 50:
        del numValues['FIFTY']
    if value == 40:
        del numValues['FORTY']

numValues = dict(reversed(numValues.items()))
print("Sort (descending) and remove items = ", numValues)
print("A is a subset of B: ", deleteValue.items() <= numValues.items())