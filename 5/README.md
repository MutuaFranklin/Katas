You have to create a function calcType, which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

Example:
calcT_type(1, 2, 3) -->   1 ? 2 = 3   --> "addition"




BDD
A function to determine the unknown operation given 3 arguments which includes 2 numbers and the result

PSEUDOCODE
- Define the function to determine the operation taking in the three argument variable ie num1,num2,result
- perform if statement to determine specific operation and store to variable operation such that:
     if(num1+num2)==result:
        operation = "addition"
- Return the operation
- Declare a variable result to store the returned function results 
- Print result


