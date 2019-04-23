import collections
import heapq
import operator

"""
1.1 Unpacking a sequence into separate variables
"""

# Unpack n-element sequence into n variables

p = (4, 5)
x, y = p
print(x)
print(y)

data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(price)
print(date)
yr, mo, da = date
print(yr)
print(mo)
print(da)

_, shares, price, _ = data

"""
1.2 Unpacking elements from iterables of arbitrary length
"""

# Unpack n elements from a sequence of unknown length

grades = [60, 42, 85, 85, 100, 100]
first, *middle, last = grades
print("Grades: {}".format(grades))
print("First: {}".format(first))
print("Middle: {}".format(middle))
print("Last: {}".format(last))

# What if there are only two items?
grades = [60, 42]
first, *middle, last = grades
print("Grades: {}".format(grades))
print("First: {}".format(first))
print("Middle: {}".format(middle))
print("Last: {}".format(last))
# Result: Var middle returns []

# What about using the star expression as the last arg?
grades = [60, 42]
first, middle, *last = grades
print("Grades: {}".format(grades))
print("First: {}".format(first))
print("Middle: {}".format(middle))
print("Last: {}".format(last))
# Result: Now it's the var last that returns []
# First: 60
# Middle: 42
# Last: []

# Trick to get trailing figure, e.g., average
# Assume a sequence of 8 quarters of sales figures,
# with the last being the most recent
sales_record = [5400, 6000, 3300, 2000,
                8000, 6500, 3000, 2100]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs)/ len(trailing_qtrs)
print("""
Trailing average: {}
Current quarter: {}""".format(trailing_avg, current_qtr))

# Could be used to get running sum of prior quarters, too

# Can be useful for string processing
line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
print("Original line:\n{}".format(line))
print("Split line:\n{}".format(line.split(":")))

uname, *fields, homedir, sh = line.split(":")
print("Username: {}".format(uname))
print("Fields: {}".format(fields))
print("Home dir: {}".format(homedir))
print("Sh: {}".format(sh))

# Combine * with _ to throw away an indeterminate number of variables
name, *_, (*_, day) = data
print(name)
print(day)

"""
Keeping the last n items
"""

# Keep a limited history of last few items seen during
# iteration or some other kind of processing

# Use a collections.deque

my_deque = collections.deque()
print("Deque: {}".format(my_deque))
test_list = [1, 3, 5, 7, 9]
print("Test list: {}".format(test_list))
my_deque.appendleft([test_list])
print("appendleft: {}".format(my_deque))
my_deque.clear()
print("deque cleared: {}".format(my_deque))
my_deque.extendleft(test_list)
print("extendleft: {}".format(my_deque))
my_deque.extend(test_list)
print("extend: {}".format(my_deque))
my_deque.pop()
print("my_deque.pop(): {}".format(my_deque))
my_deque.popleft()
print("my_deque.popleft(): {}".format(my_deque))
fixed_deque = collections.deque(maxlen=3)
print("new deque of fixed size: {}".format(fixed_deque))
fixed_deque.append(1)
print("fixed-size deque after append: {}".format(fixed_deque))
fixed_deque.append(1)
print("fixed-size deque after append: {}".format(fixed_deque))
fixed_deque.append(1)
print("fixed-size deque after append: {}".format(fixed_deque))
fixed_deque.append(2)
print("fixed-size deque after append: {}".format(fixed_deque))
fixed_deque.appendleft(9)
print("fixed-size deque after append left: {}".format(fixed_deque))

"""
1.4 Finding the largest or smallest n items
"""

# Compare using a heap to sorting a list

test_list = [23, 4, 3, 25, 26, 19, 19, 15]
# Must create list and then heapify it
test_heap = test_list.copy()
heapq.heapify(test_heap)
sorted_test_list = sorted(test_list)
n = 4
heap_smallest_n = heapq.nsmallest(n, test_heap)
list_smallest_n = sorted_test_list[:n]
slice_heap = test_heap[0]
slice_list = sorted_test_list[0]
pop_heap = heapq.heappop(test_heap)
heap_after_pop = test_heap
pop_list = sorted_test_list.pop(0)
list_after_pop = sorted_test_list

"""
1.5 Implementing a priority queue
"""

# Skip

"""
1.6 Mapping keys to multiple values in a dictionary
"""
# Use a container as the value in a dict
# Use default dict to avoid having to initialize an empty dict

d = collections.defaultdict(list)
print("Default dict:")
print(d)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print("Filled dict after appending:")
print(d)

# Could also have used .defaultdict(set) to create empty set
# each time a key is added

"""
1.7 Keeping dictionaries in order
"""

# Skip: Use collections.OrderedDict()

# Implementation Note: Internally maintains a doubly linked
# list that orders the keys according to insertion order.
# Therefore the size of an OrderedDict is > 2 times size
# of a normal dictionary

"""
1.8 Calculating with dictionaries
"""
# Often want to do calculations or other operations on the
# values of a dictionary, but also want to retain info
# about the key

# example of stock prices
prices = {"ACME": 45.23,
"AAPL": 612.78,
"IBM": 205.55,
"HPQ": 37.20}

# Can get list of values with .values(), but then lose
# info about the key

# One workaround is to pass a "key" argument to an operation
min_stock_name = min(prices, key=lambda k: prices[k])
print(min_stock_name)
# Returns "HPQ"
# But now don't have what that price was
# Would have to use that return value to do a lookup, like so:
min_stock_price = prices[min_stock_name]
print(min_stock_price)
# Prints 37.2
# But full form of above operation is: 
#   prices[min(prices, key=lambda k: prices[k])]

# Solution: Use zip to get tuples of the values and keys
price_collection = zip(prices.values(), prices.keys())
print(price_collection)
# <zip object at 0x102c562c8>

# Can then feed zip object to an iterative operation:
print("Contents of price_collection:")
for x in price_collection:
    print(x[0], x[1])
# But note that zip object can only be consumed one:
print("Contents of price_collection:")
for x in price_collection:
    print(x[0], x[1])
# Contents of price_collection:
# Jasons-MacBook-Pro:python_cookbook jasondixon$
# i.e., returns nothing

# Note in book, but could convert to a list to make
# an object that can be used more than once
price_collection_list = list(zip(prices.values(), prices.keys()))
print("Contents of price_collection:")
for x in price_collection_list:
    print(x[0], x[1])
print("Contents of price_collection:")
for x in price_collection_list:
    print(x[0], x[1])

"""
1.9 Finding commonalities in two dictionaries
"""
# Can perform common set operations using keys() or items()
a = {
    "x": 1,
    "y": 2,
    "z": 3}

b = {
    "w": 10,
    "x": 11,
    "y": 2
}
# Find keys in common
a_b_common = a.keys() & b.keys()
print("Keys shared between dicts a and b:")
print(a_b_common)
# Find keys in a that are not in b
a_not_in_b = a.keys() - b.keys()
print("Keys in a but not in b:")
print(a_not_in_b)
# Find (key, value) pairs in common
k_v_pairs_common = a.items() & b.items()
print("Key value pairs in both a and b:")
print(k_v_pairs_common)

# Note that set operations work because
# dictionary keys are guaranteed to be
# unique and by extension so are (key, value) pairs
# However, per the documentation for the dict class,
# set-like behavior of (key, value) pairs only holds
# under a condition:
#       If all values are hashable, 
#       so that (key, value) pairs are unique and hashable, 
#       then the items view is also set-like.

# Set operations are not possible on values because
# they are not guaranteed to be unique, so they
# can't be treated as sets (unless one were to convert
# .values() to a set in an extra step)

"""
1.10 Removing duplicates from a sequence while maintaining order
"""

# Recipes use set, which I thought would result in unordered
# collection

# Explore: 
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
a_deduped = list(dedupe(a))
print("Original list: {}".format(a))
print("Deduped: {}".format(a_deduped))

# Does this work for negative ints too?
b = [1, 5, -2, 1, 5, -9, 10]
b_deduped = list(dedupe(b))
print("Original list: {}".format(b))
print("Deduped: {}".format(b_deduped))

# Does this work for strings?
c = ["blue", "red", "purple", "cyan", "red", "maroon"]
c_deduped = list(dedupe(c))
print("Original list: {}".format(c))
print("Deduped: {}".format(c_deduped))

# What is the dedupe() func actually returning? 
# There's no return statement

print(dedupe(a))
# <generator object dedupe at 0x107ec0048>

print(list(dedupe(a)))

"""
1.11 Naming a slice
"""
# Use slice() func to name a slice
# instead of having a bunch of hardcoded slice indices
# Note the use of a comma instead of a colon to separate the
# start and stop values

record = "..........100..........513.25.........."
SHARES = slice(10, 13)
PRICE = slice(23, 29)

print("Share Count: {}".format(record[SHARES]))
print("Price: {}".format(record[PRICE]))

# Note that slices have .start, .stop, and .step attributes
print("Start/Stop/Step:")
print(SHARES.start, SHARES.stop, SHARES.step)

# Step value can be used as expected
record_separated = "1.4.5"
LOCATION = slice(0,5,2)
print("Record: {}".format(record_separated))
print("Result of slice: {}".format(
    record_separated[LOCATION]))
print("Start/Stop/Step:")
print(LOCATION.start, LOCATION.stop, LOCATION.step)

record_list = [1, 2, 3, 4, 5, 6, 7, 8]
LIST_LOC = slice(0, 10, 2)
print("Record: {}".format(record_list))
print("Result of slice: {}".format(
    record_list[LIST_LOC]))
print("Start/Stop/Step:")
print(LIST_LOC.start, LIST_LOC.stop, LIST_LOC.step)

"""
1.12 Determining the most frequently occuring items in a sequence
"""
# Use collections.Counter
# In addition to providing a count, it also has a 
# most_common() method

words = ["when", "in", "the", "course", "of", "human", "events",
"when", "the", "over", "the", "land", "of", "the", "free"]

word_counts = collections.Counter(words)
print(word_counts)
print("Most common 3:")
top_three = word_counts.most_common(3)
print(top_three)

"""
1.13 Sorting a list of dictionaries by a common key
"""
# The sorted() function accepts a key argument to specify
# what to sort by
# The itemgetter() function in the operator module
# is a useful key to pass to output rows in a list of 
# dictionaries by any of th fields common to all 
# of the dictionaries

rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleese", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004},
]
print("\n")
print("Sorted by uid:")
rows_by_uid = sorted(rows, key=operator.itemgetter("uid"))
for row in rows_by_uid:
    print(row)
print("\n")
print("Sorted by lname:")
rows_by_lname = sorted(rows, key=operator.itemgetter("lname"))
for row in rows_by_lname:
    print(row)

# Try with lambda
rows_by_lname_lambda = sorted(rows, key=lambda d: d["lname"])
print("\n")
print("Sorted by lname using lambda func:")
for row in rows_by_lname:
    print(row)

# .itemgetter() method can accept more than one field,
# .e.g, to sort by both first and last name 
print("\n")
print("Sorted by lname, fname:")
rows_by_full_name = sorted(rows, 
    key=operator.itemgetter("lname", "fname"))
for row in rows_by_full_name:
    print(row)

