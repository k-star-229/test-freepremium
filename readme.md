## Approach: 
The idea is to count the elements with remainders when divided by x, i.e 0 to x-1, each remainder separately. Suppose we have x as 6, then the numbers which are less than 6 and have remainders which add up to 6 gives sum as 6 when added. For example, we have elements, 2,4 in the array and 2%6 = 2 and 4%6 =4, and these remainders add up to give 6. Like that we have to check for pairs with remainders (1,5),(2,4),(3,3). if we have one or more elements with remainder 1 and one or more elements with remainder 5, then surely we get a sum as 6. Here we do not consider (0,6) as the elements for the resultant pair should be less than 6. when it comes to (3,3) we have to check if we have two elements with remainder 3, then we can say that “There exists a pair whose sum is x”. 

## Algorithm:  

1. Create an array with size x. 

2. Initialize all rem elements to zero.

3. Traverse the given array

    Do the following if arr[i] is less than x:
    r=arr[i]%x which is done to get the remainder.
    rem[r]=rem[r]+1 i.e. increasing the count of elements that have remainder r when divided with x.
4. Now, traverse the rem array from 1 to x/2.   

    If(rem[i]> 0 and rem[x-i]>0) then print pair and come out of the loop. This means that we have a pair that results in x upon doing.
5. Now when we reach at x/2 in the above loop   

    If x is even, for getting a pair we should have two elements with remainder x/2.
    If rem[x/2]>1 then print pair else print “NO”
    If it is not satisfied that is x is odd, it will have a separate pair with x-x/2.
    If rem[x/2]>1 and rem[x-x/2]>1 , then print pair else, print”No”;

## Sample Input
nums = [2,7,11,15], target = 9

## Output
(2,7)