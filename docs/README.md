# Documentation for Ydra

## Python Code Documentation

#### main.py

###### Main Loop
Main Game Loop that repeats instances of itself to create animation (stop motion effect). Imports everything from *constants.py* and *logicope.py*

###### Surface Handling


#### logicope.py

Basic Logical Operator functions that return boolean values. The list of the logical operaters are:

##### AND
- *_and(bool1, bool2)* & represent **AND**
	- If both *bool1* and *bool2* are **True**, output _True_

##### OR
- *_or(value1, value2)* & represent **OR**
	- If either *bool1* or *bool2* are **True**, output _True_

##### NOT
- *_not(bool)* & represent **NOT**
	- If *bool* is **True**, output the opposite _False_

##### NAND
- *_nand(bool1, bool2)* & represents **NAND**
	- If both *bool1* and *bool2* are **True**, output _False_

##### NOR
- *_nor(value1, value2)* & represent **NOR**
	- If either *bool1* or *bool2* are **True**, output _False_



#### constants.py


## Pygame

#### Surface
- Display Surface
    *The Game Window.* Anything displayed goe on here
    Can only have ***ONE*** Display Surface and the Display Surface is always shown. So we can never hide it

- (Regular) Surface or in short => Surface
    Essentially a single image (something imported, rendered text or plain color)
    Can have ***AS MANY AS WE WANT***, there is no limitation. It's only visible within the Display Surface.

*Surface* needs to be put **on** *Display Surface* to be visible

##### VARIABLES
* Initialize surface
	test_surface = pygame.Surface((width, height))

- Fill the Surface with a color
	test_surface.fill('Red') [can also read RGB values]

- In The Main Game Loop after events and pygame.quit()
	screen.blit(test_surface, (positionX, positionY))