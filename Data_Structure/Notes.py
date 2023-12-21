"""
Declare a list

When building the string, add the characters to the list. This is
O(1) per operation. Across n operations, it will cost
O(n) in tota

Once finished, convert the list to a string using "".join(list). This is  O(n).
In total, it cost us => O(n+n)=O(2n)=O(n)

"""
# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4504/

##  String concatenation in python.
# Add all the elements in the list
# Use join function to concatenate the list
# "".join(['d', 'i', 'n']

"""
1: As a reminder, a subarray or substring is a contiguous section of an array or string.

2: A subsequence is a set of elements of an array/string that keeps the same relative order but doesn't 
need to be contiguous.
For example, subsequences of [1, 2, 3, 4] include: [1, 3], [4], [], [2, 3], but not [3, 2], [5], [4, 1].

3: In Subsequance order matter. Order need to be maintained

4: Difference between subset and subsequence.

5: HashMap Iteration :-
a) Iterate Keys

# Get keys: use .keys(). You can iterate over this using a for loop.
keys = hash_map.keys()
for key in keys:
    print(key)
    
b) 
# Get values: use .values(). You can iterate over this using a for loop.
values = hash_map.values()
for val in values:
    print(val)
    
c)

for key, val in my_hash_map.items():
    print(f"{key}: {val}")

6: Find if there is a substring in the given string
Python String find() method returns the lowest index or first occurrence of the substring if it is found in a given string. If it is not found, then it returns -1.

Syntax: str_obj.find(sub, start, end)

Parameters: 

sub: Substring that needs to be searched in the given string. 
start (optional): Starting position where the substring needs to be checked within the string. 
end (optional): End position is the index of the last value for the specified range. It is excluded while checking. 
Return:  Returns the lowest index of the substring if it is found in a given string. If it’s not found then it returns -1.


## Dictionay

In Python, defaultdict is a class provided by the collections module. It's a variation of the built-in dict (dictionary) data type, but with one key difference: it allows you to specify a default value for any new keys that are accessed but not yet present in the dictionary.

When you create a defaultdict with a default value type (e.g., int, list, str, etc.), it ensures that you won't encounter a KeyError when trying to access a non-existent key. Instead, it automatically creates that key with the specified default value type. For defaultdict(int), the default value is 0.

Here's an example of how to use defaultdict(int):

Example: 

from collections import defaultdict

# Create a defaultdict with int as the default value type
my_dict = defaultdict(int)

# Access a key that doesn't exist
my_dict['a'] += 1

# No KeyError is raised, and the key is created with a default value of 0
print(my_dict['a'])  # Output: 1


from collections import defaultdict

# Create a defaultdict with str as the default value type
my_dict = defaultdict(str)

# Different keys of dictionary
my_dict = {
    'name': 'John',
    42: 'answer',
    (1, 2): 'tuple_key'
}


# Access a key that doesn't exist
my_dict['name'] += "John"

# No KeyError is raised, and the key is created with a default value of an empty string
print(my_dict['name'])  # Output: "John"

# Access another key that doesn't exist
my_dict['address'] += "123 Main Street"

# Again, no KeyError is raised, and the key is created with a default value of an empty string
print(my_dict['address'])  # Output: "123 Main Street"

In this example, we use defaultdict(str) to specify that the default value for any non-existent key is an empty string. 
When we access keys like 'name' and 'address' for the first time, the defaultdict creates them with empty string values. 
This is helpful when you want to concatenate or manipulate strings associated with 
dictionary keys without needing to handle key existence manually.


Permuation and COmbination
https://www.britannica.com/science/permutation


24 HRs challenge
https://www.youtube.com/watch?v=a3Aep-SygUA

## Kashish Channel
https://www.youtube.com/@KashishMehndiratta
"""
def build_string(s):
    arr = []
    for c in s:
        arr.append(c)

    return "".join(arr)

if __name__ =="__main__":
    s = "dinesh"
    result = build_string(s)
    print(result)
