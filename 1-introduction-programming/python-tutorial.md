# Python Tutorial

This tutorial is based on the [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial). It is revised to fit beginners.

## Hello World

It is a tradition from C programming language to say "Hello World" as the first program in learning a new programming langauge. Below is a comparison of the first program in different langauges.

![hello-world](./images/hello-world.png)

In Python, it is a single line: `print('Hello World!')`.

- `print` is a built-in function that displays (prints) things to a console. A function, as defined in math, takes an input and generates an output. The input is the value passed into the function to generate an output. An input consists of one or multiple values. Those input values are called arguments. A console is your terminal (Mac OS or Linux) or commmand line (Windows) screen.
- `()` is a pair of parentheses that separates a function from its inputs. The input of the function is put inside a pair of parenthese.
- `'Hello World!'` is the input. It is the only argument here. It is a string that has a sequence of characters quoted in a single quote. Actually you can use double quote and triple quote to quote a string. `"Hello World!"` and `"""Hello World!"""` are the same as `'Hello World!'`. You will see the usage of the three syntax formats.

Finally, `print('Hello World!')` is interpreted by Python to display the "Hello World!" to the console.

## Excute Python Code

It is usually a good idea to create a folder that works as your workspace for an application. An application usually consists of many files and data resources.

Open your terminal (MacOS) or command line (Windows). Create a new folder named as "hello-world" and change director to the folder. The two commands are:

```sh
mkdir hello-world
cd hello-world
```

You can use `pwd` command to check that you are in the correct folder. Then use `code .` command to run VS Code that uses the current folder `.` as the workspace. The `.` means the current folder, which is `hello-world` now.

With Python interpreter installed, you can run the code in Python interpreter (`python3`) or in IDLE (`idle`). Once you install VS Code, you have more ways to run Python code. Together, you can

- run `python3` or `python` in a terminal or in the VS Code terminal.
- use Python REPL within the VS Code. It is the same as runl `idle` in command line outside VS Code.
- when you create `.py` file such as `hello.py`, you can run the file from a terminal or command line using the command `python hello.py`.
- use menu or shortcut to run/debug a Python files that has `.py` appendix.
- run Jupyter Notebook cells for files that has `.ipynb` appendix.
- run cells marked by `% ##` in a `.py` files.
- write/wring Python code in an interactive Python window in VS Code. Usually this window opens when you run Jupyter notebook cells or Python cells.

## Use Packages

The Python interpreter comes with functions such as `print` and arithmatic operations. Most functions are developed by different companies and are shared/reused in a specific package format and are often called packages or libraries. To use these extra functions, you need to install the package and import them into your Python program.

Create a `plot.py` file in the current workspace with the following content:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
```

You don't need to understand the code here. Just know that it uses fucntions not built into the Python interpreter.

You will see underlines in `matplotlib` and `numpy` if you don't have the required packages installed. If you run the file regardlessly, you will see an error message: `ModuleNotFoundError: No module named 'matplotlib'`.

To fix the error, you need to install `matplotlib` package. The `matplotlib` package uses functions from `numpy` package. When you install `matplotlib`, it installs `numpy` package as a dependency.

In a terminal, run `pip install matplotlib`. Then you should be able to run the file inside VS Code, or from a terminal using command `python3 plot.py`.
