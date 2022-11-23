# find all integer powers of num <= 10000 and the first one that is > 10000
def powers(num, power=0):
    # end case
    if num ** power > 10000:
        print(f"answer {num ** power} > 10000, end case triggered")
        # returns the final answer which will be added to the end of the list
        return str(num ** power)
    else:
        print(f"answer {num ** power} <= 10000, adding to list and calling again")
        # combines the answers together with desired formatting, and calls the function again to find the next power
        return f"{num ** power}, {powers(num, power+1)}"


print(powers(2))
