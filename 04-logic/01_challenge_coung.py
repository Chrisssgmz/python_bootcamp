text = "rrjjrjrrjjrj"

def check_is_balanced(text: str) -> bool:
    text = text.upper()
    
    count_r: int = text.count("R")
    count_j: int = text.count("J")
    
    print(f"Count of 'R': {count_r}")
    print(f"Count of 'J': {count_j}")
        
    return count_r == count_j

print(check_is_balanced("rrjjrjrrjjrj"))
print(check_is_balanced("rrjjrjr"))