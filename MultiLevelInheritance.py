class A:
    
    def __init__(self):
        print("From A Class")
        
class B(A):
    
    def __init__(self):
        print("From B Class")
        super().__init__()
        
class C(B):
    
    def __init__(self):
        print("From C Class")
        super().__init__()
        
classC = C()
