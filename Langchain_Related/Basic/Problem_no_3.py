import logging 
import json 


"""Problem 3: Error Handling (Try/Except)
What You'll Build:
Handle errors gracefully (like when JSON parsing fails).

The Challenge:
"""
# Create a JSONParser class that:
# 1. Takes a string in parse() method
# 2. Tries to parse it as JSON
# 3. Returns parsed dict if successful
# 4. Returns None if it fails (but doesn't crash)
# 5. Logs what went wrong


#  Setup Logging (This tells Python HOW to log)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
        
class JSONParser: 
    def parse(self,json_string):
        try: 
            data = json.loads(json_string) 
            logging.info("JSON parsed successfully") 
            return data 
            
        except json.JSONDecodeError as e: 
            logging.error(f"Failed to parse json. Error:{e}") 
        except TypeError as e:  
            logging.error(f"Input must be a string{e}")  
        
parser = JSONParser()


print("Test 1 Result:", parser.parse('{"name": "Gemini", "role": "AI"}'))
print("Test 2 Result:", parser.parse('{"name": "Gemini", "role": AI"}'))
print("Test 3 Result:", parser.parse(12345))

















"""
# Usage:
parser = JSONParser()
result = parser.parse('{"name": "John"}')  # Works
print(result)  # {"name": "John"}

result = parser.parse("invalid json")  # Doesn't crash
print(result)  # None (and log message printed)
Why This Matters:

Ollama parsing problem involves JSON failure handling
Real production code NEVER crashes on bad input
You need try/except everywhere
Implementation:

import json

class JSONParser:
    def __init__(self):
        self.errors = []
    
    def parse(self, text):
        try:
            return json.loads(text)
        except json.JSONDecodeError as e:
            self.errors.append(str(e))
            print(f"Parse failed: {e}")
            return None
Difficulty: ⭐ (Easy)
Time: 20 minutes
Skills: Try/except, error handling, logging"""