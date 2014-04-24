def calc_pieces(cuts):
    x1 = cuts/2
    x2 = cuts-x1
    return x1* x2

no_tests = int(raw_input())
tests = []
for i in xrange(0,no_tests):
    tests.append(int(raw_input()))

for test in tests:
    print calc_pieces(test)
