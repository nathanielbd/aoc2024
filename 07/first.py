f = open('input.txt', 'r')
data = [row.strip() for row in f]
def test_if_true(row: str):
    test = int(row.split(":")[0])
    operands = [int(operand) for operand in row.split(":")[1].strip().split(" ")]
    def helper(test, operands):
        if len(operands) == 0:
            return test == 0
        rem = test % operands[-1]
        if rem == 0:
            if helper(test / operands[-1], operands[:-1]):
                return True
        if test >= operands[-1]:
            return helper(test - operands[-1], operands[:-1])
        return False
    return test if helper(test, operands) else 0
print(sum([test_if_true(row) for row in data]))