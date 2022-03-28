# MultiCuberX
Here are 3 examples of solving Rubik's cubes (a big update is on the way):

3x3x3 - https://youtu.be/q7xPAZP0UFM 

4x4x4 - https://youtu.be/9T3FiTrAEHM 

5x5x5 - https://youtu.be/OyEfjKg2A2Y 

A lego robot that can solve 3x3x3, 4x4x4 and 5x5x5 Rubik's Cubes

It all started 3 years ago when I saw the CraneCuber:
https://github.com/dwalton76/lego-crane-cuber

So I decided to make something like that but with stepper motors and here we are.

For now, image analisys it's done with rubiksk-cube-tracker, rubiks-color-resolver and the solution is provided by rubiks-cube-NxNxN-solver. The links are available at the CraneCuber repository.

The 4x4x4 cube is solved using TPR by Chen Shuang:
https://github.com/cs0x7f/TPR-4x4x4-Solver

calibrate.py and colors.py is my tentative to develop a Color Extractor (OpenCV based) to get the colors of the cube... so far it's not really working as I wanted...
