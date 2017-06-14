def celsius_farenheit(temp_str,temp_num):
    
    if temp_str.lower()=="c":
        temp_num= (9*temp_num/5)+32
        print(temp_num)
    elif temp_str.lower()=="f":
        temp_num=(temp_num- 32)*5/9
        print(temp_num)
    else:
        print("error :" +temp_str)

    return
    
    
