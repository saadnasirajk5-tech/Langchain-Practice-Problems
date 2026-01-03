

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
class AIMessage(Message):
    def __init__(self, content: str):
        """Initializing AIMessage with 'ai' role"""
        super().__init__(content)
        self.role = "ai" 
class SystemMessage(Message):
    def __init__(self, content: str):
        super().__init__(content)
        self.role = "system" 

        
# Usage Example 
if __name__ == "__main__":
    # Creating messages
    human_msg = HumanMessage("Hello") 
    ai_msg = AIMessage("Hi there") 
    system_msg = SystemMessage("You are helpful")     
    



print("Human Message:")
print(f"  Role: {human_msg.role}")  # "human"
print(f"  Content: {human_msg.content}")  # "Hello"
print(f"  Dictionary: {human_msg.to_dict()}")  # {"content": "Hello", "role": "human"}
print()
    

print("AI Message:")
print(f"  Role: {ai_msg.role}")  # "ai"
print(f"  Dictionary: {ai_msg.to_dict()}")  # {"content": "Hi there", "role": "ai"}
print()

print("System Message:")
print(f"  Role: {system_msg.role}")  # "system"
print(f"  Dictionary: {system_msg.to_dict()}") 


















