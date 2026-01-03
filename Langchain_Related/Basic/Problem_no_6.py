

# Goal is to build multiple message types with shared behavior (like LangChain's HumanMessage, AIMessage).


class Message:
    def __init__(self, content:str):
        """Initialize with content"""
        self.content = content  
        self.role = None # It will be set by sub classes
        def to_dict(self):
            """Converting message to dictionary format"""
            return {
                "content": self.content, 
                "role": self.role   
            }
class HumanMessage(Message):
    def __init__(self, content: str):
        """ Initializing HumanMessage with 'human' role"""
        super().__init__(content)     
        self.role = "human" 
class AI(Message):
    def __init__(self, content: str):
        """Initializing AIMessage with 'ai' role"""
        super().__init__(content)
        self.role = "ai" 
class SystemMessage(Message):
    def __init__(self, content: str):
        super().__init__(content)
        self.role = "system" 

        























