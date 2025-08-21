# Basic calculator with pyqt5
A simple calculator performs addition, subtraction, multiplication, division, logarithm, squaring, and square root operations.

![Screenshot](basic-calculator-image.png)

## Features
- Addition
- Substraction
- Multiplication
- Division
- Logarithm
- Square root
- Square

## Operation Rules
There are a total of **7 operations**. For **3 specific operations** (logarithm, square, square root):  
- If **both numbers are the same**, the operation is applied only once.  
- If **the two numbers are different**, the operation is applied to both numbers and the results are **summed**.  
Examples:  
- Square (`square`): if `a ≠ b`, result = `a² + b²`  
- Logarithm (`log`): if `a ≠ b`, result = `log(a) + log(b)`  
- Square Root (`square root`): if `a ≠ b`, result = `√a + √b`  

## İnstallation and Use
pip install pyqt5  --> requirement
python calculatorApp.py --> runs
