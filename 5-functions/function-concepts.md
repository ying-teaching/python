# Function Concepts

## What and Why

A function is a group of statements that performs a specific task. Though there is no limit in the number of statements that you can write inside a function, tt is important that a function consists of a group of closely related statemetns to serve a single purpose. It will make your code easy to read and maintain.

Why you need functions? A simple anwser is divide and conquer. Programmers use functions to organize and reuse code. Instead of writing a long list of statements of a complex application, you can divide the application into a set of subtasks such that each task is relatively easy to be solved.

![subtask](images/subtask.png)

In the above diagram, instead of a long list of statements on the left, you can organize statements into a set of functions that each function perform a single subtask. It helps you to design the program because at one moment you only need to solve a relatively simpler subtask.

For example, following is a list of operations that a robot performs:

1. unplug from charger
2. walk to the house door
3. open the door
4. walk out the door
5. close the door
6. walk to the car
7. open the car door
8. sit in the car
9. close the car door
10. drive the car to Beach Dr

If you use two functions, the code will be

1. leave house (this function has the statements 1 to 5)
2. drive to shcool (this function has the statements 6 to 10)

The functional version is easy to write and easy to understand. Another huge benefit is that a function name summarizes the task. From the

If a subtask is too complex, you can divided it into a set of subtasks agian.
