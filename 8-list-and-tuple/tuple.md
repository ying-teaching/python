# Tuples

A `tuple` is an immutable sequence. It is similar to a list because both have a sequence of elements, however a tuple is immutable: once created, you can only read it but cannot change it. It is helpfule to represent a small set of immucate data such as result data of a function call.

To create a tuple, just put the elements in a pair of parenthese: `a_tuple = (2, 3, 4, 5)`. If there is only one element (rarely used), put a comma after the element: `single = (2, )`. You can also use `tuple` function to create a tuple from a list or a range. For example: `a = tuple(range(5))` or `b = tuple([2, 3, 4])`.

A tuple support the same set operations of a list, except those change the contents of a list. The common operations are:

- indexing: `a_tuple[1]`
- slicing: `a_tuple[1:]`
- `in`, `+` and `*` operators
- built-in functions: `len`, `min`, `max`
