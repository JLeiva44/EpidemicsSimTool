class Environment:
    '''
    Rule base class to represent dynamics such as disease transmission, recovery, or effects of measures.
    '''
    def __init__(self):
        self.agents = []
    
    def add_agent(self, agent):
        self.agents.append(agent)
    
    def update(self):
        for agent in self.agents:
            agent.update(self)
