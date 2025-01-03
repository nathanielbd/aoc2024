from z3 import *

f = open('input.txt', 'r')
data = [row.strip() for row in f]

i = data.index('')
wires = data[:i]
gates = data[i+1:]
vs = set()
s = Solver()

def register(var):
    exec(f"global {var}; {var} = Bool('{var}')")

for wire in wires:
    w, t = wire.split(": ")
    register(w)
    if int(t):
        s.add(eval(w))
    else:
        s.add(eval(f"Not({w})"))
    vs.add(w)
def constraint_from_gate(gate):
    lhs, w3 = gate.split(' -> ')
    w1, op, w2 = lhs.split(' ')
    if w1 not in vs:
        register(w1)
    if w2 not in vs:
        register(w2)
    if w3 not in vs:
        register(w3)
    match op:
        case 'AND':
            s.add(eval(f"And({w1}, {w2}) == {w3}"))
        case 'OR':
            s.add(eval(f"Or({w1}, {w2}) == {w3}"))
        case 'XOR':
            s.add(eval(f"Xor({w1}, {w2}) == {w3}"))
        case _:
            pass

for gate in gates:
    constraint_from_gate(gate)

for v in vs:
    if v.startswith('z'):
        print(simplify(v))