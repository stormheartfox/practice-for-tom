# Testing your code

In every language there is a way to test your code, writing tests ensures the reliability of your code & reduce the amount of code you write, by defining your tests first you only need to write enough code to satisfy the test. If the test fails, you refactor your code to improve upon it.

## Testing Libraries

Python has many testing libraries - and all have their use cases and learning curves. For this repository we will use unittest.

Unittest allows us to set test cases for each function within our code, evaluate the output of the function and determine whether this is correct or not, when compared to what we expect within our tests.

E.g we write a test that wants a First and Last name to be returned when it runs, but it returns only a First name.

Unittest will show that this code did not pass the test and will return the error based on what we have written for our errors.

Reading this will sound confusing at first, but once we run a few tests, you will find it is extremely easy to write tests and evaluate your code. 

### To run tests use:
```
unittest <filename>
```