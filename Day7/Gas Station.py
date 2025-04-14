gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

def can_complete_circuit(gas, cost):
    total_gas = 0
    total_cost = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i + 1
            tank = 0

    return start if total_gas >= total_cost else -1

print(can_complete_circuit(gas, cost))
