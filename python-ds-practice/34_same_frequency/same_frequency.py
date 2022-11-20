def same_frequency(num1, num2):
    nm1 = str(num1)
    nm2 = str(num2)
    num1_dict = {}
    num2_dict = {}
    for x in range(len(nm1)-1):
        num1_dict[nm1[x]] = 0
    for x in range(len(nm2)-1):
        num2_dict[nm2[x]] = 0
    for num in nm2:
        if num in num1_dict:
            num1_dict[num] +=1
    for num in nm2:
        if num in num2_dict:
            num2_dict[num] +=1
    return num2_dict == num1_dict
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """