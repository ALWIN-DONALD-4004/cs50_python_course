def main():
    print_square(3)
    print_square_simple(5)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end = "")
        print() #print("\n")
        
def print_square_simple(size):
    for i in range(size):
        print("&" * size)  #strin multipulication
        
main()