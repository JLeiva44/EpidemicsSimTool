class Simulator:
    '''
    Simulator class that coordinates everything: initializes agents and environment, and executes simulation steps.
    '''
    def __init__(self, environment, rules):
        self.environment = environment
        self.rules = rules
    
    def run(self, steps):
        for _ in range(steps):
            self.environment.update()
            for rule in self.rules:
                for agent in self.environment.agents:
                    rule.apply(agent, self.environment)
