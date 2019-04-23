"""
CHAPTER 3: Numbers, Dates, and Times
"""

### 3.1 Rounding numerical values ###

# Rounding decimals
original = [1.23, 1.27, -1.27, 1.25361, 1.5432, 1.55432, 1.5555, 2.555, 2.5]
for x in original:
    print("Original")
    print(x)
    print("Round 0")
    print(round(x, 0))
    print("Round 1")
    print(round(x, 1))
    print("Round 2")
    print(round(x, 2))
    print("Round 3")
    print(round(x, 3))    
    print("\n")

# Rounding whole numbers
original = [123, 1235, 12536, 125361]
for x in original:
    print("Original")
    print(x)
    print("Round 0")
    print(round(x, 0))
    print("Round -1")
    print(round(x, -1))
    print("Round -2")
    print(round(x, -2))
    print("Round -3")
    print(round(x, -3))    
    print("\n")

### 3.2 Performing Accurate Decimal Calculations ###

# Use decimal module to get more accuracy
from decimal import Decimal

a = Decimal ("4.2")
b = Decimal ("2.1")
print(a)
print(b)
print(a + b)

check = a + b == Decimal('6.3')
print("Added terms and 6.3 equal:", check)
print("Sum with standard floats:", 4.2+2.1)

# Try setting precision
from decimal import localcontext
a = Decimal("1.3")
b = Decimal("1.7")
print("division", a, b, a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print("division at precision of 3:", a, b, a/b)

with localcontext() as ctx:
    ctx.prec = 5
    print("division at precision of 5:", a, b, a/b)

### 3.3 Formatting Numbers for Output ###

x = 1234.56789

#Format to specify is "[<>^]?width[,]?(.digits)?"
# where width and digits are integers
# and '?' signifies optional parts

# Note: can use either format() func or str.format() method

format_tests = {
    "Two decimal places":"{:0.2f}", 
    "Right justified 10 chars": "{:>10.2f}",
    "Centered": "{:^10.2f}",
    "Thousands sep": "{:0,.2f}",
    "Thousands sep width 2": "{:2,.2f}", #width seems to affect only left/right/center justification
    "One deciaml place": "{:.1f}",
    "No decimal places": "{:.0f}",
    "No decimal, thousands sep": "{:,.0f}",
    
}

for desc, ft in format_tests.items():
    print("{}:".format(desc)) 
    print(ft.format(x))
    print("\n")

print("Swap thousands and decimal seps using translate function and dictionary:")
swap_separators = {
    ord("."): ",",
    ord(","): ".",
}
print("{:,.2f}".format(x).translate(swap_separators))

### 3.8 Calculating with fractions ###

# Use the fractions module to work with fractions
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a, b, "a + b", a + b)
print(a, b, "a * b", a * b)

# Get numerator or denominator
print("a*b, numerator", (a*b).numerator)
print("a*b, denominator", (a*b).denominator)

# Convert to a float
print(float(a*b))
# Limit the denominator of a value
print("Denominator limited")
print((a*b).limit_denominator(8))

print("Convert float to fraction")
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(x)
print(y)
x = 0.75
y = Fraction(*x.as_integer_ratio())
print(x)
print(y)

# use fractions package to aid in
# calculating percentiles
# Update: Fractions package actually cannot help here
# But continue to implement func to calculate percentile 
def calc_percentile(num_list, percentile):
    """
   num_list : list, tuple
        A collection of numbers
        e.g., [5, 9, 2, 13, 1]
    percentile : float
        A float in the range 0 to 1 that represents
        the percentage of values that are below the
        returned value
        e.g., 0.4, which represents the 40th percentile
    
    Returns the lowest number under which the percentage
    of values represented by percentile fall below

    Steps:
    Sort list
    Find rank of percentile via:
        percentile (as decimal) * (length of num_list + 1)
    a) If rank is an integer, find and return number at that rank
    b) If rank is not an integer:
       1) Store integer part of rank, IR
       2) Store fractional part of rank, FR
       3) Retrieve value at rank position IR and store as IR_V
       4) Retrieve value at rank position (IR + 1) and store as IR1_V
       5) Calculate FR * (IR1_V - IR_V) + IR_V
       6) return result of step 5
    """
    # List must be sorted
    num_list = sorted(num_list)

    # Find rank of percentile
    # TODO: Allow percentile param to be percentage (0 to 100)
    rnk = percentile * (len(num_list) + 1)
    
    # func to return the value at a certain rank
    def get_value_at_rank(num_list, rnk):
        # Ranks are 1-indexed but 
        # lists and other collections are 0-indexed
        # Number at rank i = collection[i - 1]
        
        # rnk should never be zero or negative
        if rnk <= 0:
            raise ValueError("rnk argument should be in range 1 to n")
        # rnk should be int, not float
        rnk = int(rnk)

        return num_list[rnk - 1]

    # check for int
    rnk_is_int = rnk % int(rnk) == 0
    
    if rnk_is_int:
        return get_value_at_rank(num_list, rnk)
    
    # Follow alternate path when rank is not an int
    IR = int(rnk)
    FR = rnk - int(rnk)
    IR_V = get_value_at_rank(num_list, IR)
    IR1_V = get_value_at_rank(num_list, IR+1)
    
    return round(FR * (IR1_V - IR_V) + IR_V, 2)

print("\n******TEST OF PERCENTILE FUNCTION*****\n")
# Test func
scores = [3, 5, 7, 8, 9, 11, 13, 15]
perc = .25
correct_val = 5.5

test_val = calc_percentile(scores, perc)
print("List: {}".format(scores))
print("Correct value: {}".format(correct_val))
print("Function value: {}".format(test_val))
print("Test passed: {}".format(correct_val == test_val))

scores = [4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10]
perc = .25
correct_val = 5

test_val = calc_percentile(scores, perc)
print("List: {}".format(scores))
print("Correct value: {}".format(correct_val))
print("Function value: {}".format(test_val))
print("Test passed: {}".format(correct_val == test_val))

scores = scores
perc = .85
correct_val = 9.85

test_val = calc_percentile(scores, perc)
print("List: {}".format(scores))
print("Correct value: {}".format(correct_val))
print("Function value: {}".format(test_val))
print("Test passed: {}".format(correct_val == test_val))

scores = [2, 3, 5, 9]
perc = .5
correct_val = 4

test_val = calc_percentile(scores, perc)
print("List: {}".format(scores))
print("Correct value: {}".format(correct_val))
print("Function value: {}".format(test_val))
print("Test passed: {}".format(correct_val == test_val))

scores = [2, 3, 5, 9, 11]
perc = .5
correct_val = 5

test_val = calc_percentile(scores, perc)
print("List: {}".format(scores))
print("Correct value: {}".format(correct_val))
print("Function value: {}".format(test_val))
print("Test passed: {}".format(correct_val == test_val))
