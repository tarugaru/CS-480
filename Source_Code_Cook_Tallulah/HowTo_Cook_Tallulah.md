# CS-480
Advanced Software Engineering: Dr. Vajda Fall 2023
Python Calculator App Testing

Running this file "test_cases.py" will prompt the user to input the number of test cases they wish the program to produce. At that point the program will compute two batches of testcases-- one of correct expressions and another batch of incorrect expressions. Each test case will be numbered and display the expression to the user, after that line it will say whether the test passed or failed. After all test cases have run, the program will say how many cases passed and what the success rate was. At this point the program will terminate! 

This is a python app that should have no requirements when it comes to hardware, just make sure the latest version of python is installed. The program calculator.py must also be saved in the same folder location! 

Please note that the incorrect functions are computed by passing through a correct expression through a function called typo_expression()... This function simulates different typos a user might make, like forgetting or adding an extra parenthesis (or other character). The expression is "typo'ed" a random amount of times (at least once)! 

In some of the incorrect expressions you will see "math.cos" or some other trig function written incorrectly, this is because the eval() function does not recognize cos() without specifying the math library.

There might also be some syntax warning messages after running the program, those are something I am currently working on fixing! 
