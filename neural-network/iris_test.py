import csv
from typing import List
from util import normalize_by_feature_scaling
from network import Network
from random import shuffle

if __name__ == "__main__":
    iris_parameters: List[List[float]] = []
    iris_classifications: List[List[float]] = []
    iris_species: List[str] = []
    with open('iris.csv', mode='r') as iris_file:
        irises: List = list(csv.reader(iris_file))
        shuffle(irises)
        for iris in irises:
            parameters: List[float] = [float(n) for n in iris[0:4]]
            iris_parameters.append(parameters)
            species: str = iris[4]
            if species == "Iris-setosa":
                iris_classifications.append([1.0, 0.0, 0.0])
            elif species == "Iris-versicolor":
                iris_classifications.append([0.0, 1.0, 0.0])
            else:
                iris_classifications.append([0.0, 0.0, 1.0])
    normalize_by_feature_scaling(iris_parameters)

    iris_network: Network = Network([4, 6, 3], 0.3)

    def iris_interpret_output(output: List[float]) -> str:
        if max(output) == output[0]:
            return "Iris-setosa"
        elif max(output) == output[1]:
            return "Iris-versicolor"
        else: 
            return "Iris-verginica"
    
    iris_trainers: List[List[float]] = iris_parameters[0:140]
    iris_trainers_corrects: List[List[float]] = iris_classifications[0:140]
    for _ in range(50):
        iris_network.train(iris_trainers, iris_trainers_corrects)

    