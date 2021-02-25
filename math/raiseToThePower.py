# We're going to creating a function to calculate the power of a number, instead of using the pow(x, x) function
# so we can understand a bit more about programming logic

# Defining function and giving its parameters to store the values we give it
def raise_to_power(base_num, pow_num): 
    result = 1   # Here, we're defining a variable to store the result of the calculation that will happen later in the function

    # We are going to use this loop to multiply the base number that we're to define, 
    # an X amount of times (the amount of times of the power value)

    for i in range(pow_num):
        result = result * base_num    # In the variable 'result' we are going to store the finished calculation

    return result   # We return result so we dont get a None value from the function

"You can replace these values and run the program"
print(raise_to_power(6, 4))   # We define the base and power number, first value is going to be the base and
                                # 2nd is the power we're going to elevate it to. it can be an integer and/or float number

# This is the same as writing pow(6, 4), therefore 6 to the power of 4
 

