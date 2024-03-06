def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dic1={}
    num1_str=str(num1)
    print(num1_str)
    for num in num1_str:
        num_count = num1_str.count(num)
        dic1[num]= num_count
    
    dic2={}
    num2_str=str(num2)
    for num in num2_str:
        num_count = num2_str.count(num)
        dic2[num]= num_count
    
    if dic1 == dic2:
        return True
    else:
        return False

