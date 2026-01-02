
# Problem 4: Reading Files (File I/O)   

# Create a DocumentReader class that:
# 1. Takes a filename in __init__
# 2. Has read() method that reads file
# 3. Returns a Document object with content
# 4. Handles file not found error gracefully
# 5. Returns None if file missing



class Document: 
    def __init__(self, filename, content): 
        self.filename = filename   
        self.content = content    
class DocumentReader:  
    def __init__(self, filename):
        self.filename = filename 
    def read(self):
        try: 
            with open(self.filename, 'r') as file:       
                content = file.read() 
            return Document(self.filename, content)
        except FileNotFoundError: 
            print(f"File {self.filename} not found")
            return None   
        

# Test the code
reader = DocumentReader("test.txt") 
doc = reader.read()  # doc will be a Document object or None

if doc:  # Check if doc is not None
    print(doc.content)  # File contents
    print(doc.filename)  # "test.txt"
else:
    print("Document could not be read (file not found)")







"""

**What You'll Build:**
Read documents from files (like DocumentLoaders do).

**The Challenge:**

```python

# Usage:
reader = DocumentReader("test.txt")
doc = reader.read()
print(doc.content)  # File contents
print(doc.filename)  # "test.txt"

# If file missing:
reader = DocumentReader("missing.txt")
doc = reader.read()
print(doc)  # None (no crash)
```

**Why This Matters:**
- LangChain loaders read files
- You need to handle missing files
- File operations are common in contributions

**Implementation:**

```python
class Document:
    def __init__(self, content, filename):
        self.content = content
        self.filename = filename

class DocumentReader:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        try:
            with open(self.filename, 'r') as f:
                content = f.read()
            return Document(content, self.filename)
        except FileNotFoundError:
            print(f"File {self.filename} not found")
            return None
```

**Difficulty**: ⭐ (Easy)
**Time**: 25 minutes
**Skills**: File I/O, context managers (with), error handling"""























