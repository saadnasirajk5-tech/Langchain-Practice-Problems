"""  Problem 2: List of Messages (Collections)
What You'll Build:
Store multiple messages and filter them.

The Challenge: """

# Create a MessageHistory class that:
# 1. Stores a list of Message objects
# 2. Has add_message(msg) method
# 3. Has get_last_n(n) method - returns last N messages
# 4. Has get_by_role(role) method - returns all messages from a role
# 5. Has __len__() - return count of messages

class Message:
    def __init__(self, content, role):
        self.content = content
        self.role = role
    def __repr__(self):
        return f"Message(content={self.content!r}, role={self.role!r})"
class MessageHistory: 
    def __init__(self):
        self.messages = []
    def add_message(self, msg):
        self.messages.append(msg)    
    def get_last_n(self, n):
        return self.messages[-n:] 
    def get_by_role(self, role): 
        return [msg for msg in self.messages if msg.role == role] 
    def __len__(self):
        return len(self.messages)
history = MessageHistory()
history.add_message(Message("Hello", "user"))
history.add_message(Message("Hi there", "assistant"))  # Fixed: use Message not msg
history.add_message(Message("How are you?", "user"))
print(len(history))  # 3
print(history.get_last_n(2))  # Last 2 messages
print(history.get_by_role("user"))  # All user messages

"""
# Usage:
history = MessageHistory()
history.add_message(Message("Hello", "user"))
history.add_message(Message("Hi there", "assistant"))
history.add_message(Message("How are you?", "user"))

print(len(history))  # 3
print(history.get_last_n(2))  # Last 2 messages
print(history.get_by_role("user"))  # All user messages
Why This Matters:

LangChain's ConversationBufferMemory works like this
You need to manage collections
List operations (append, slicing, filtering)
Hints:

class MessageHistory:
    def __init__(self):
        self.messages = []
    
    def add_message(self, msg):
        self.messages.append(msg)
    
    def get_last_n(self, n):
        return self.messages[-n:]  # Last n elements
    
    def get_by_role(self, role):
        return [msg for msg in self.messages if msg.role == role]
    
    def __len__(self):
        return len(self.messages)
Difficulty: ⭐ (Easy)
Time: 30 minutes
Skills: List operations, list comprehension, __len__(), slicing"""