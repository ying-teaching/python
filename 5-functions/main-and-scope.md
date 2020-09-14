# `main` and Variable Scope

This section introduces the `main` function and varaible scopes.

## 1 `main` Function

There is a convention in Python coding: you want to use the `main` function name as the entry point of a program. A non-trivial program has many functions, however, there must be a function working as the entry point of the program. It is common to use `main` as the name of the start-up function. The `main` contains the mainline logic of a programthat call other functions to perform top level tasks. Each top level task may call other functions to perform subtasks. Following is an example of function organization.

![structure](images/structure.png)

You should use `main` as the entry of your program as the following:

```python
def main():
    number = 42
    print_triple(number)

def print_triple(number):
    triple = number * 3
    print(f'Triple of {number} is {triple}.')

main()
```

As shown above, you can use a funtion and define it later.

## 2 Variable Scope

Every Python varaible has a scope -- it is only visible in the region it is defined.

### 2.1 Local Variable

A variable defined inside a function can be used in the function after it is defined. This is called a `local variable`. The function is the scope of the local variable. Outside the function, it is invisible and cannot be used.

```python
def main():
    number = 42    # a local variable
    print(number)  # use the local variable

main()
```

The function parameters are local variables. You can use them inside the function as a locally defined variables. Assigning a parameter to another value doesn't affect the corresponding argument.

```python
def main():
    number = 42
    print_triple(number)
    print(f'The number in main is {number}')

def print_triple(number):
    number *=3
    print(f'Tripled number is {number}')

main()
```

In the above code, the `number` in `main` is a local number and is passed to `print_triple` function. Inside the `print_triple` function, the `number` is a local variable -- a totally different one from the `number` in `main`. The program assigns it to a different value of `126`. In the `main` function, it still has a value of `42`.

### 2.3 Global Variable

A variable defined in the main body of a file, i.e, not defined in a function, is called a `global variable`. It is visible and accessible to all statements inside or outside the functtions.

Because a global variable is shared by all functions, you should not define and use global variables in your program because it is hard to tell where it is changed. The only resonable situation for global variable is to define constant values that is shared by all function. For example, define the math constant `PI` as the following.

```python
PI = 3.1416

def main():
    radius = 42
    print_area(radius)

def print_area(radius):
    area = radius * radius * PI
    print(f'The area is {area: .2f}')

main()
```

## 2.4 Control Statements

The scope for variables defined in control statements `if`, `for` and `while` is its enclosing function. If they are not defined in a function (very rare), they are in the global scope. Below is an example:

```python
def main():
    for number in range(3):
        print(number)

    print(number)

main()
```

The `number` is created in the `for` loop but its scope is the `main` function. Therefore it can be used by the `print(number)` statement in the `main` function.
