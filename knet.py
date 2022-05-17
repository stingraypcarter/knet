import random
import math
import matplotlib.pyplot as plt
import sys

relations = ['AND','OR','XOR','NAND','NOR','XNOR']

class Gene:
    def __init__(self, id, gene_count):
        ids = list(range(gene_count))
        ids.remove(id)
        self.a = random.choice(ids)
        ids.remove(self.a)
        self.b = random.choice(ids)
        self.relation = random.choice(relations)

    def get_state(self,cur_states):
        state_a = cur_states[self.a]
        state_b = cur_states[self.b]
        if(self.relation == 'AND'):
            return (state_a and state_b)
        elif(self.relation == 'OR'):
            return (state_a or state_b)
        elif(self.relation == 'XOR'):
            return (state_a != state_b)
        elif(self.relation == 'NAND'):
            return (not (state_a and state_b))
        elif(self.relation == 'NOR'):
            return ((not state_a) and (not state_b))
        elif(self.relation == 'XNOR'):
            return (state_a == state_b)

def get_next_states(states):
    new_states = list()
    for i in range(gene_count):
        new_val = genes[i].get_state(states)
        new_states.append(new_val)
    return new_states

def bools_to_int(bool_list):
    vals = list(map(int, bool_list))
    decimal = sum([int(b*math.pow(2,i)) for i, b in enumerate(vals)])
    return decimal

if __name__ == "__main__":
    gene_count = int(sys.argv[1])
    run_times = int(sys.argv[2])

    genes = [Gene(i,gene_count) for i in range(gene_count)]
    states = [bool(random.getrandbits(1)) for i in range(gene_count)]

    time = range(run_times)
    data = list()

    repeats_at = list()
    repeat_time = int()
    repeated = [False,False]

    for t in time:
        val = bools_to_int(states)
        seen = val in data
        if seen and repeated[0] and not repeated[1]:
            if not val == repeats_at[0]:
                repeats_at.append(val)
            else:
                repeated[1] = True
        elif seen and not repeated[0]:
            repeated[0] = True
            repeat_time = t
            repeats_at.append(val)

        data.append(val)
        states = get_next_states(states)

    print(repeats_at)
    print(repeat_time)
    print(f'repeat starts at {repeat_time} with cycle of length {len(repeats_at)} with cycle {repeats_at}')

    plt.plot(time, data)
    plt.show()
