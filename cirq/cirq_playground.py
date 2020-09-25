import cirq
import numpy as np
from cirq import Simulator
from cirq.circuits import InsertStrategy
from cirq.ops import CZ, H

print(cirq.google.Foxtail)
length = 3
qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
print(qubits)

# define a circuit
circuit = cirq.Circuit()
circuit.append(cirq.H(q) for q in qubits if (q.row + q.col) % 2 == 0)
print(circuit)

circuit.append(cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1)
print(circuit)

# redefing the circuit with an InsertStrategy
circuit = cirq.Circuit()
circuit.append(
    [cirq.H(q) for q in qubits if (q.row + q.col) % 2 == 0],
    strategy=cirq.InsertStrategy.EARLIEST,
)
circuit.append(
    [cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1],
    strategy=cirq.InsertStrategy.EARLIEST,
)
print(circuit)


# look at the circuit moments
for i, m in enumerate(circuit):
    print("Moment {}: {}".format(i, m))


# creating a grid of qubits
qubits = [cirq.GridQubit(x, y) for x in range(3) for y in range(3)]
print(qubits)

# applying a gate at Qubit location (0,0)
x_gate = cirq.X

# turn in into an operation
x_op = x_gate(qubits[0])
print(x_op)

# define a Moment
cz = cirq.CZ(qubits[0], qubits[1])
x = cirq.X(qubits[2])
moment = cirq.Moment([x, cz])
print(moment)

# define a Circuit by combining Moments togeteher
cz01 = cirq.CZ(qubits[0], qubits[1])
x2 = cirq.X(qubits[2])
cz12 = cirq.CZ(qubits[1], qubits[2])
moment0 = cirq.Moment([cz01, x2])
moment1 = cirq.Moment([cz12])
circuit = cirq.Circuit((moment0, moment1))
print(circuit)

q0, q1, q2 = [cirq.GridQubit(i, 0) for i in range(3)]

circuit = cirq.Circuit()
circuit.append([CZ(q0, q1)])
circuit.append([H(q0), H(q2)], strategy=InsertStrategy.EARLIEST)
print(circuit)

circuit = cirq.Circuit()
circuit.append([H(q0), H(q1), H(q2)], strategy=InsertStrategy.NEW)
print(circuit)
circuit = cirq.Circuit()
circuit.append([CZ(q1, q2)])
circuit.append([CZ(q1, q2)])
circuit.append([H(q0), H(q1), H(q2)], strategy=InsertStrategy.INLINE)
print(circuit)

circuit = cirq.Circuit()
circuit.append([H(q0)])
circuit.append([CZ(q1, q2), H(q0)], strategy=InsertStrategy.NEW_THEN_INLINE)
print(circuit)

q0 = cirq.GridQubit(0, 0)
q1 = cirq.GridQubit(0, 1)


# create a basic circuit constructor
def basic_circuit(meas=True):
    sqrt_x = cirq.X ** (0.5)
    yield sqrt_x(q0), sqrt_x(q1)
    yield cirq.CZ(q0, q1)
    yield sqrt_x(q0), sqrt_x(q1)
    if meas:
        yield cirq.measure(q0, key="alpha"), cirq.measure(q1, key="beta")


circuit = cirq.Circuit()
circuit.append(basic_circuit())
print(circuit)


simulator = Simulator()
result = simulator.run(circuit)
print(result)


def generate_2x2_grid():
    a, b, c, d = [
        cirq.GridQubit(0, 0),
        cirq.GridQubit(0, 1),
        cirq.GridQubit(1, 1),
        cirq.GridQubit(1, 0),
    ]
    circuit = cirq.Circuit.from_ops(
        cirq.H(a),
        cz_swap(a, b, 0.5),
        cz_swap(b, c, 0.25),
        cz_swap(c, d, 0.125),
        cirq.H(a),
        cz_swap(a, b, 0.5),
        cz_swap(b, c, 0.25),
        cirq.H(a),
        cz_swap(a, b, 0.5),
        cirq.H(a),
        strategy=cirq.InsertStrategy.EARLIEST,
    )
    return circuit


def main():
    qft_circuit = generate_2x2_grid()
    print("Circuit:")
    print(qft_circuit)

    # creating a simulator
    simulator = cirq.Simulator()

    # pass in the circuit and print the result
    result = simulator.simulate(qft_circuit)
    print()
    print("Final State:")
    print(np.around(result.final_state, 3))


def cz_swap(q0, q1, rot):
    yield cirq.CZ(q0, q1) ** rot
    yield cirq.SWAP(q0, q1)

