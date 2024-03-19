class A:
    
    def __init__(self):
        print("From A Class")
        
class B():
    
    def __init__(self):
        print("From B Class")

    
class C(A, B):
    
    def __init__(self):
        print("From C Class")
        A.__init__(self)
        B.__init__(self)
        
classC = C()
