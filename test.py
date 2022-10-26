
analog_data = [40, 40, 8, 40, 40]
case = 0

for i in range(len(analog_data) - 1):
    if analog_data[i] < analog_data[i + 1]:
        case = i

if case == 0:
    print("case 0")
elif case == 1:
    print("case 1")
elif case == 2:
    print("case 2")
elif case == 3:
    print("case 3")
elif case == 4:
    print("case 4")
