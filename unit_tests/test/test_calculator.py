from calculator import square


# def main():
#     test_square()
    
'''
def test_square():
    
    if square(2) != 4:
        print("square of 2 is 4")
    elif square(3) != 9:
        print("square of 2 is 4")
        
    # instred of these long code we cna use assert
    
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
   
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square is not 9")
    
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not 4")
        
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square is not 9")
        
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square is not 0")
          
'''
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    

def test_zero():
    assert square(0) == 0

# if __name__ == "__main__":
#     main()
    
    
    