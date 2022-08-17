import random

def MarkovChain(states, transitionNames, transitionMatrix, n_iter):
    initRand = random.randint(0,4)
    
    currentState = states[initRand]
    stateList = [currentState]

    initialState = currentState

    i = 0
    prob = 1

    while i != n_iter:
        rand = random.randint(0,4)

        stateIndex = states.index(currentState)
        chance = transitionNames[stateIndex][rand]
        probIndex = transitionNames[stateIndex].index(chance)
        prob *= transitionMatrix[stateIndex][probIndex]
        
        transition = chance.split("-")

        stateList.append(transition[1])
        currentState = transition[1]
        
        i += 1

    return [initialState, stateList, n_iter, prob]

stados = ["1","2","3","4","5"]
transitionNombres = [["1-1","1-2","1-3","1-4","1-5"],["2-1","2-2","2-3","2-4","2-5"],["3-1","3-2","3-3","3-4","3-5"],["4-1","4-2","4-3","4-4","4-5"],["5-1","5-2","5-3","5-4","5-5"]]
transitionMatrices = [[0.2, 0.2, 0.2, 0.2, 0.2],[0.1, 0.3, 0.1, 0.4, 0.1],[0.6, 0.1, 0.1, 0.1, 0.1],[0.3, 0.0, 0.5, 0.1, 0.1],[0.0, 0.0, 0.1, 0.1, 0.8]]

res = MarkovChain(stados, transitionNombres, transitionMatrices, 3)

print("Estado inicial: " + str(res[0]))
print("Estados visitados: " + str(res[1]))
print("Numero de iteraciones: " + str(res[2]))
print("Probabilidad final: " + str(res[3]))
