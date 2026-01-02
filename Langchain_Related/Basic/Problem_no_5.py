


# To filter and transform data(Like vector store retrieval)

class DataFilter: 
    def __init__(self, data):
        self.data = data   
        self.validate_data()
    def validate_data(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list") 
    # def filter_by_key(data, key, value):  
    #     filtered_results = [] 
    #     for item in data:
    #         if key in item and item[key] == value: 
    #             filtered_results.append(item)     
    #     return filtered_results    
    def filter_by_key(self, key, value):  
        return [item for item in self.data if key in item and item[key] == value]
    def filter_by_range(self, key, min_val, max_val):
        results = [] 
        for item in self.data: 
            if key in item: 
                if min_val <= item[key] <= max_val:
                    results.append(item) 
        return results 
    def transform(self ,data, key, func):
        for item in data: 
            if key in item: 
                old_val = item[key] 
                new_val = func(old_val)     
                item[key] = new_val    
        return data           
    def limit(self, n):
        return data[:n]

data = [{"name": "Alice", "score": 85}]
filter = DataFilter(data)

result = filter.filter_by_range("score", 80, 90)
print(result)


 








