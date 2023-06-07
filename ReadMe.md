# Classes

In this assignment you'll create 3 classes as described below. 

All object property variables for each class should be hidden using the double underscore variable naming (__variable).  Create getters and setters to access and modify object properties where needed. 

Each Class file has a class definition stub and and driver function.  Use the driver function to write test your class as you develop it.   

Style counts:
   * Each object should have Object summary comment at the top of the file
   * Each function should have a comment that describes what the function does.  Can include what values it takes as parameters and what value it returns  
   * Include comments for and "tricky" sections of code
   * Use good descriptive variable names
   * Avoid "Magic Numbers"
   * Do Not Repeat yourself

## Road Class
The Road object will take width in feet and length and return the cubic feet asphalt to pave a road at a given thickness in inches.

Create a the Road Class with these following methods, be sure to use the measurement units as noted below.

    1. setWidth(width)              // in feet
    2. setLength(length)            // in miles
    3. getWidth                     // feet 
    4. getLength                    // miles
    5. asphalt_needed(thickness)    // thickness in inches , return Cubic feet
    
Use the test_Road.py to check your work

***Note: There are 5,280 feet in a mile*** (yes this is a "Magic Number")

## TimeCalculator Class
The Time object will take seconds, minutes, and hours add them up and return the total number of hours, minutes or seconds.

Create a the TimeCalculator Class with these following methods:

    1. setHours
    2. setMinutes
    3. setSeconds
    4. timeInHours
    5. timeInMinutes
    6. timeInSeconds

Use the test_TimeCalculator.py to check your work

## Knight Class

The Knight Class is meant to simulate the beginnings of a character in an RPG type game.  A Knight object is created with a name and starting hit points.  The Knight object can then be damaged and healed for hit points.  And has a status of alive or dead.  

Implement the following methods for the Knight Class:
 
    1. Constructor (init)  // sets the Knight's name and starting hit points
    2. name() // returns the knight's name 
    3. hitPoints() // returns the knight's hit points
    4. damage(points) // reduces the knight's hit points by the passed in value
    5. heal(points) // increases the knight's hit points by the passed in value
    6. isDead() // returns a True or False based on if the Knight's hit points are gone
    7. __str__() // returns a string with the format "{name} is {alive/dead}!}
Additional rules:
    
    1. A knight can not be damaged or healed for more than 25 points at a time
    2. Once a knight is dead they can no longer be healed
    3. A knight can not have negative hit points
    
## Turn it in
Once you're done make sure to commit and push your changes to the github repository.  Then submit the assignment on Blackboard with a link to the repository URL. 
