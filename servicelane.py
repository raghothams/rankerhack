input_line1 = raw_input()
n_and_t = input_line1.split()
del input_line1

N = int(n_and_t[0])
T = int(n_and_t[1])


widths_input = raw_input()

test_cases_input = []
for _ in range(0,T):
    test_cases_input.append(raw_input())

test_cases = []
for x in test_cases_input:
    components = x.split(" ")
    t = {}
    t['i'] = int(components[0])
    t['j'] = int(components[1])
    test_cases.append(t)

del test_cases_input

widths = []
widths_input = widths_input.split()
for x in widths_input:
    widths.append(int(x))
del widths_input

for x in test_cases:
    print min(widths[x['i']:x['j']+1])
