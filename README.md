# LinesPy

LinesPy is a simple yet powerful Python program that allows users to transition from a console environment to an interactive, fully functional window on both Mac and Windows. It enables the easy creation and manipulation of vector graphics, such as lines, rectangles, circles, and customizable arcs. The program offers a straightforward interface for rendering and modifying shapes with adjustable properties like thickness, color, and radius. With LinesPy, users can display their graphics in real-time on a canvas, making it an accessible tool for both artistic and technical drawing projects. Its simplicity and intuitive design make it an ideal choice for those looking to quickly create and visualize graphics.

Try to create a game !
  

# How to use

- Read the Documentation section below to know how to use it
- Put your code in the `code.py` file
- Run the `main.py` file with Python
  

## Documentation

### cls()

The `cls()` function clears everything on the screen and can also replace it with a specific color if desired.
You can also insert a color or a HEX color, as shown in these two examples below:  
  
`cls(color="blue")`  
`cls(color="#FEFEFE")`  
  
  
  

### plot()

Place a pixel at coordinates `x` and `y`, with a specified color.  
  
`plot(x, y, color="black")`  
`plot(x, y, color="#FEFEFE")`
  
  
  

### line()

Draw a line from point `(x1, y1)` to point `(x2, y2)`, with optional thickness, color, and a “cap” style.   
  
`line(x1, y1, x2, y2, thickness=1, color="black", cap="butt")`  
`line(x1, y1, x2, y2, thickness=1, color="#FEFEFE", cap="butt")`  
  
  

The “cap” can be:  
	•	`butt` (default value): no cap at the ends;  
	•	`round`: a rounded cap is added to the ends of the line;  
	•	`square`: a square cap is added to the ends of the line.  
  
  
  

### rect()

Draw a rectangle with the top-left corner at `x` `y`, width `w`, and height `h`, with optional thickness, color, and radius for rounded corners:  

`rect(x, y, w, h, thickness=1, color="black", radius=0)`
  
  
  

### frect()

Draw a filled rectangle with the top-left corner at `x` `y`, width `w`, and height `h`, with optional, color, and radius for rounded corners:  

`frect(x, y, w, h, color="black", radius=0)`
  
  

### circle()

Draw a circle with the center at `x` `y` and radius `r`, with optional thickness and color:  

`circle(x, y, r, thickness=1, color="black")`
  
  
### fcircle()

Draw a filled circle with the center at `x` `y` and radius `r`, with optional color:  

`fcircle(x, y, r, color="black")`
  

### print()

Display the text `text` in the standard output with options for size, color, anchor point, and blinking:   

`print(text, size=12, color="black", anchor="no", blink=0)`

Display the text text at coordinates `x` `y` with options for size, color, anchor point, and blinking:

`print(text, x, y, size=12, color="black", anchor="no", blink=0)`  

The different options are:  
	
  •	`size`: text size (default is `12 pt`);  
	•	`color`: text color (default is black);  
	•	`anchor`: defines the anchor point (default is northwest “no”) with values: `no`, `nc`, `ne`, `co`, `cc`, `ce`, `so`, `sc`, and `se`;  
	•	`blink`: text blinking duration in seconds (no blinking by default).  
  
  
### input()

Display the text prompt in the standard output, wait for user input, and return the entered value as a `string`:  

`input(prompt, size=12, color="black", anchor="no", width=10)`  

Display the text prompt at coordinates `x` `y`, wait for user input, and return the entered value as a `string`:  

`input(prompt, x, y, size=12, color="black", anchor="no", width=10)`  
  
  
### pause()

Pause the program for `t` milliseconds:  

`pause(t)`  
  
  
### key()

Test a keyboard key and return True if the key is pressed, False otherwise: 

`key(key)`
