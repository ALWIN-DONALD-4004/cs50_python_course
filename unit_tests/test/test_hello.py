from hello import hello



def test_str():
   assert hello("alwin") == "hello, alwin"
   
def test_wrong():
   assert hello("donald") == "hello, donald"
   

def test_default():
   assert hello() == "hello, world"
   
def test_argument():
    for name in ["fred","ari","chan"]:
        assert hello(name) == f"hello, {name}"
   
    
    
