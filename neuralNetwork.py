import random
import math

class NeuralNetwork:
    def __init__(self,architecture):
        self.Network = []
        for i in range(1,len(architecture)): # layers
            self.Network.append([])
            for j in range(architecture[i]):    # neurons
                self.Network[i-1].append([])
                for k in range(architecture[i-1]+1): # weights
                    self.Network[i-1][j].append(random.uniform(-0.5,0.5))

    def getNetwork(self):
        return self.Network

    def sigmoidLogistic(self,x):
        return 1/(1 + math.e**(-x))
    
    def activateNeuron(self,weights,inputs):
        signal = weights[0]*(-1)
        for i in range(1,len(weights)):
            signal += weights[i]*inputs[i-1]
        return self.sigmoidLogistic(signal)

    def feedForward(self,inputs):
        for layer in self.Network:
            inputs_aux = []
            for neuron in layer:
                inputs_aux.append(self.activateNeuron(neuron,inputs))
            inputs = inputs_aux
        return inputs