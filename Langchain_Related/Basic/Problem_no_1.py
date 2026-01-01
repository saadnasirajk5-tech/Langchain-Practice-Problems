
"""   
Problem 1: Message Class (Data Structures)
What You'll Build:
A class that stores messages (like LangChain does internally).

The Challenge:
""" 
# Create a Message class that:
# 1. Takes content and role in __init__
# 2. Has a method to_dict() that returns a dictionary
# 3. Has a method __str__() that prints nicely

class Message: 
    def __init__(self,content,role):
        self.content = content   
        self.role = role     
    def to_dict(self):
        pass 
    def __str__(self):
        pass


"""   

# Usage example:
msg = Message(content="Hello", role="user")
print(msg)  # Should print: "User: Hello"
print(msg.to_dict())  # Should print: {"content": "Hello", "role": "user"}

# Bonus: Add a method to_json() that returns JSON string
Why This Matters:

LangChain has Message classes (BaseMessage, HumanMessage, etc.)
You need to understand class structure
__str__() and __dict__() are CRITICAL for debugging
Hints:

import json

class Message:
    def __init__(self, content, role):
        self.content = content
        self.role = role
    
    def __str__(self):
        # Return formatted string
        pass
    
    def to_dict(self):
        # Return dictionary
        pass
    
    def to_json(self):
        # Return JSON string
        pass
Test it:

msg = Message("Hello world", "user")
assert str(msg) == "User: Hello world"
assert msg.to_dict() == {"content": "Hello world", "role": "user"}
assert json.loads(msg.to_json())["content"] == "Hello world"
Difficulty: ⭐ (Easy)
Time: 30 minutes
Skills: Classes, __init__, methods, __str__(), dictionaries
"""






















