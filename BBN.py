# Import required packages
import math
from pomegranate import *

# Initially the door selected by the guest is completely random
performance = DiscreteDistribution({'Poor': 1. / 5, 'Moderate': 1. / 5, 'Good': 1. / 5, 'VeryGood': 1. / 5,
                                    'Excellent': 1. / 5})

# The door containing the prize is also a random process
learnerState = ConditionalProbabilityTable(
    [['Poor', 'Novice', 0.50],
     ['Poor', 'Beginner', 0.30],
     ['Poor', 'Intermediate', 0.15],
     ['Poor', 'Expert', 0.05],
     ['Moderate', 'Novice', 0.30],
     ['Moderate', 'Beginner', 0.50],
     ['Moderate', 'Intermediate', 0.15],
     ['Moderate', 'Expert', 0.05],
     ['Good', 'Novice', 0.15],
     ['Good', 'Beginner', 0.25],
     ['Good', 'Intermediate', 0.45],
     ['Good', 'Expert', 0.15],
     ['VeryGood', 'Novice', 0.10],
     ['VeryGood', 'Beginner', 0.15],
     ['VeryGood', 'Intermediate', 0.40],
     ['VeryGood', 'Expert', 0.35],
     ['Excellent', 'Novice', 0.05],
     ['Excellent', 'Beginner', 0.15],
     ['Excellent', 'Intermediate', 0.30],
     ['Excellent', 'Expert', 0.50]], [performance])


# The door Monty picks, depends on the choice of the guest and the prize door
contentComplexity = ConditionalProbabilityTable(
    [['Poor', 'Novice', 'Low', 0.90],
     ['Poor', 'Novice', 'Medium', 0.07],
     ['Poor', 'Novice', 'High', 0.03],
     ['Poor', 'Beginner', 'Low', 0.86],
     ['Poor', 'Beginner', 'Medium', 0.11],
     ['Poor', 'Beginner', 'High', 0.03],
     ['Poor', 'Intermediate', 'Low', 0.82],
     ['Poor', 'Intermediate', 'Medium', 0.14],
     ['Poor', 'Intermediate', 'High', 0.04],
     ['Poor', 'Expert', 'Low', 0.76],
     ['Poor', 'Expert', 'Medium', 0.18],
     ['Poor', 'Expert', 'High', 0.06],
     ['Moderate', 'Novice', 'Low', 0.70],
     ['Moderate', 'Novice', 'Medium', 0.22],
     ['Moderate', 'Novice', 'High', 0.08],
     ['Moderate', 'Beginner', 'Low', 0.61],
     ['Moderate', 'Beginner', 'Medium', 0.29],
     ['Moderate', 'Beginner', 'High', 0.10],
     ['Moderate', 'Intermediate', 'Low', 0.52],
     ['Moderate', 'Intermediate', 'Medium', 0.36],
     ['Moderate', 'Intermediate', 'High', 0.12],
     ['Moderate', 'Expert', 'Low', 0.42],
     ['Moderate', 'Expert', 'Medium', 0.44],
     ['Moderate', 'Expert', 'High', 0.14],
     ['Good', 'Novice', 'Low', 0.32],
     ['Good', 'Novice', 'Medium', 0.52],
     ['Good', 'Novice', 'High', 0.16],
     ['Good', 'Beginner', 'Low', 0.21],
     ['Good', 'Beginner', 'Medium', 0.61],
     ['Good', 'Beginner', 'High', 0.18],
     ['Good', 'Intermediate', 'Low', 0.10],
     ['Good', 'Intermediate', 'Medium', 0.70],
     ['Good', 'Intermediate', 'High', 0.20],
     ['Good', 'Expert', 'Low', 0.10],
     ['Good', 'Expert', 'Medium', 0.65],
     ['Good', 'Expert', 'High', 0.25],
     ['VeryGood', 'Novice', 'Low', 0.09],
     ['VeryGood', 'Novice', 'Medium', 0.61],
     ['VeryGood', 'Novice', 'High', 0.30],
     ['VeryGood', 'Beginner', 'Low', 0.08],
     ['VeryGood', 'Beginner', 'Medium', 0.56],
     ['VeryGood', 'Beginner', 'High', 0.36],
     ['VeryGood', 'Intermediate', 'Low', 0.07],
     ['VeryGood', 'Intermediate', 'Medium', 0.51],
     ['VeryGood', 'Intermediate', 'High', 0.42],
     ['VeryGood', 'Expert', 'Low', 0.06],
     ['VeryGood', 'Expert', 'Medium', 0.44],
     ['VeryGood', 'Expert', 'High', 0.50],
     ['Excellent', 'Novice', 'Low', 0.05],
     ['Excellent', 'Novice', 'Medium', 0.37],
     ['Excellent', 'Novice', 'High', 0.58],
     ['Excellent', 'Beginner', 'Low', 0.04],
     ['Excellent', 'Beginner', 'Medium', 0.28],
     ['Excellent', 'Beginner', 'High', 0.68],
     ['Excellent', 'Intermediate', 'Low', 0.03],
     ['Excellent', 'Intermediate', 'Medium', 0.19],
     ['Excellent', 'Intermediate', 'High', 0.78],
     ['Excellent', 'Expert', 'Low', 0.03],
     ['Excellent', 'Expert', 'Medium', 0.10],
     ['Excellent', 'Expert', 'High', 0.87]], [performance, learnerState])

d1 = State(performance, name="performance")
d2 = State(learnerState, name="learnerState")
d3 = State(contentComplexity, name="contentComplexity")

# Building the Bayesian Network
network = BayesianNetwork("Learner Classifier With Bayesian Networks")
network.add_states(d1, d2, d3)
network.add_edge(d1, d3)
network.add_edge(d1, d2)
network.add_edge(d2, d3)
network.bake()

beliefs = network.predict_proba({'performance' : 'Excellent'})
beliefs = map(str, beliefs)
print("n".join( "{}t{}".format( state.name, str(belief) ) for state, belief in zip( network.states, beliefs )))
