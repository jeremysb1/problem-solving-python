from __future__ import annotations
from typing import Callable, List, Optional
from random import random
from neuron import Neuron
from util import dot_product

class Layer: 
    def __init__(self, previous_layer: Optional[Layer], num_neurons: int, learning_rate: float, activation_funtion: Callable[[float], float], derivative_activation_function: Callable[[float], float]) -> None:
        self.previous_layer: Optional[Layer] = previous_layer
        self.neurons: List[Neuron] = []
        # the following could all be one large list comprehension
        for i in range(num_neurons):
            if previous_layer is None:
                random_weights: List[float] = []
            else: 
                random_weights = [random() for _ in range(len(previous_layer.neurons))]
            neuron: Neuron = Neuron(random_weights, learning_rate, activation_funtion, derivative_activation_function)
            self.neurons.append(neuron)
        self.output_cache: List[float] = [0.0 for _ in range(num_neurons)]

