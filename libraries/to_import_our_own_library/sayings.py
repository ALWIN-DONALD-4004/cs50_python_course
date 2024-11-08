def main():
    hello("world")
    goodbye("world")
    

def hello(name):
    print(f"hello , {name}")
    
def goodbye(name):
    print(f"goodbye, {name}")
    
# __name__ -call the selected function

if __name__ == "__main__":
 main()