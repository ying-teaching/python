# Module

This section introduce the module concept, including its definition, why and how you use it.

## 1 Module: What and Why

A `module` is a Pyhon code file. Or you can say a Python file is a module. A module usually consists of a set of closely-related functions.

Python uses three constructs to organize an application:

- a funtion to group statements
- a module/file to group functions
- a pacakge/libarary to group files

The reason is rather simple, putting all functions into a single file is not appropirate for big programs. Putting functions into diffrent files are easy to read/write and easy to collaborate. Packages are used to organize a large functional area. For example, all math functions or network requests.

## 2 Use Modules

To make it simple, we put all modules in the same folder. In real applications, you may want to use foders to organize files into packages. For beginners, a fold with multiple Python scripts files/modules should be enough to write a non-trivial program.

To use a module, you use `import module_name` to import a module. The module name is the Python script file name with the `.py` postfix. Then you can use `module_name.function_name` to call a function defined in the module.

For demo purpose, the following simple example uses several files to calculate an area of a circle.

```python
# constants.py
PI = 3.1416

# you can define many constants
```

```python
# circle.py
import constants

def area(radius):
    return radius * radius * constants.PI

def diameter(radius):
    return radius * 2

def circumference(radius):
    return diameter(radius) * constants.PI

# you can define many circle functions here
```

```python
# main.py
import circle

def main():
    radius1 = 3
    area1 = circle.area(radius1)
    print(f'area is: {area1: .2f}')

main()
```

## 3 `from` and `import`

There is another way to import one or more specific functions using the `from moduel_name import function1, function2` statement.

For example, the `main.py` file can be written as the following:

```python
from circle import area, diameter

def main():
    radius1 = 3
    area1 = area(radius1)
    print(f'area is: {area1: .2f}')

    print(diameter(radius1))

main()
```

Python allows you to rename a function using the `as` keyword in importing. For example: `from circle import area as calcuate_area`. Then you can use the renamed function name.

```python
# main.py
from circle import area as calcuate_area

def main():
    radius1 = 3
    area1 = calcuate_area(radius1)
    print(f'area is: {area1: .2f}')

main()
```

The feature is useful when there is a name conflict among different modules.

## 4 Import and Execution

When a module is imported, Python executes the statements in the module. For example, if you change the `constants.py` to the following:

```python
# constants.py
PI = 3.1416

print('PI is define')
```

Then the `import constants` will execute the two statemens: define a variable and print a message.

However, if you import a file multiple times, Python only executes it once.

## 5 Conditionally Execute `main`

In Python, it is common to define a `main` function in a module that is used to run testing code.

You want to run the `main` function in the command line but don't want to run the test code when a module is imported into another file.
