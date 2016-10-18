import numpy

class DFFA:
    
    RED = numpy.empty(0, dtype=int)
    BLUE = numpy.empty(0, dtype=int)
    
    def __init__(self, finite_set_of_states, state_labels, alphabets, initial_state, initial_state_frequency, final_state_frequency, frequency_transition_matrix):
        self.finite_set_of_states = finite_set_of_states
        self.state_labels = state_labels
        self.alphabets = alphabets
        self.initial_state = initial_state
        self.initial_state_frequency = initial_state_frequency
        self.final_state_frequency = final_state_frequency
        self.frequency_transition_matrix = frequency_transition_matrix