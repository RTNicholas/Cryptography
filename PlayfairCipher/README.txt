Author: Rhys Nicholas
Date: 28/11/2019
Created during a decryption project during university
======================
Playfair Cipher Guide: 


======================
Function Outline:
Given a collection of assumed mappings (e.g Common digraphs) for a cipher text encrypted by Playfair, the possible arrangement of these in the Playfair grid is finite. A mapping must be one of:-
-	Row
-	Column
-	Square
By attempting to arrange assumed  mappings with respect to these it is possible to find conflicts and in turn reduce the number of possible Playfair grids. With enough mappings the number reduced may be small enough to allow for any encryption keyword to be solved for. 

Coding:
This module takes an input of mappings and constructs every possible arrangement for each returning only those without conflicts. This is done by considering 4 notable variables: 
- GRID  = A matrix (List of Lists) representing the Playfair grid itself 
	- Elements are only assigned here if they have a known position 
	- Matrix is Row biased and does not check if elements are in the right column order
- GRID2  = List of Row based mappings without known position on the board
	- Allows for row/column conflict to found
	- Allows for mapping to be input to board if a position is found later in loop
- GRID3  = List of Column based mappings without known position on the board
	- Allows for row/column conflict to found
	- Allows for mapping to be input to board if a position is found later in loop
- Unknown = Reference of letters in GRID1 & GRID2
---------------------
======================
Final Comments:
This project proved a larger scope than feasible given the project timeframe however was still successful in the specific goal when combined with external steps to find the encryption keyword. 

Given time, in future I would like to come back to this idea and attempt to finish it full. Removing the bias of columns, returning only possible grids with the exact possible arrangements. Combing with functions that read cipher texts and attempt to find possible mappings and functions that solve for possible keys. 
