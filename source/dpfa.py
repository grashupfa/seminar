class DPFA:
    
    def __init__(self, finite_set_of_states, state_labels, alphabets, initial_state, final_state_probability, probability_transition_matrix):
        self.finite_set_of_states = finite_set_of_states
        self.state_labels = state_labels
        self.alphabets = alphabets
        self.initial_state = initial_state
        self.final_state_probability = final_state_probability
        self.probability_transition_matrix = probability_transition_matrix