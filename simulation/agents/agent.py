class Agent:
    def __init__(self, id, state):
        self.id = id
        self.state = state  # Ej. susceptible, infectado, recuperado
    
    def update(self, environment):
        pass  # Reglas específicas se definen en subclases
