import random

class VaccinationRule(Rule):
    def __init__(self, rate):
        self.rate = rate
   
    def apply(self, agent, environment):
        if agent.state == "susceptible":
            # Probabilidad de vacunación
            if random.random() < self.rate:
                agent.state = "vaccinated"
