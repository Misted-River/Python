

## Welcome to The Pathways : The Game
An adventure game based on my story world of The Pathways, a civilization for criminals located on the interconnected rings of planets outside of Earths orbit. Created using the pygame library  in Visual Studio Code.

 Currently a work in progress as this is going to be a long project which will continue even after the end of the Stardance Challenge.

https://github.com/user-attachments/assets/1f09ea2a-8bbe-432d-aba1-5a5671f70825

## Authors

 - Elli Kourousi 

https://github.com/user-attachments/assets/e4e5c9d0-1830-4262-a68f-74d77b3ee02d














## Installation

Try it: https://ek-7.itch.io/welcome-to-the-pathways-the-game [ Fixing in progress do not play this version yet! ]

_Currently only supports windows_
-> Unzip the folder and download the .exe file to run locally on your windows device

## How to play
 - Player controls Comet, a canine-like character using w,a,s,d keys (avoid pressing two keys at a time as player is intended to go up,down,left,right and not combined keys like wa being pressed at the same time etc.)
 - Press and hold on all objects observed in scene 1 (click and hold on them) to pass into scene 2 and the end of the introduction path!
 - (Scene 2 gameplay is under construction, but you can move around on the path to just look around so far)


## Features

**Scene 1 Coding**
 - Main character is moved by pressing w,a,s,d keys on a keyboard in the respective directions.
 - If player hits on the edge of the path on-screen, a collision occurs which blocks character movement in direction of the obstacle -> Pixel perfect collision 
 - Screen scrolls along with character in both axes x and y, depending on characters distance to the edge of screen -> Character is always visible on-screen as the path moves.
 - Clickable items are present along the course of the path, when they a player clicks and holds with their mouse a label is shown on-screen.
 - End of scene is reached at the end of the path where an invisible line, when touched by character, brings the player into scene 2.
 - Animated player character goes through a loop of 5 individual drawn frames to make the character appear to move visually on-screen.

***Scene 2 Coding: (not complete yet):***
 - Different path is shown - Crossroads area before allowing player to choose their intended with with its respective gameplay and story depending on direction chosen.
 - Player movement is the same as scene 1, path scrolls as player moves
 
***Art :*** 
 - The art for the path, background, objects and some bits of the characters animation are work in progress for now
 - All art is drawn by me using Ibis Paint X drawing software on Ipad
 
 ***Music:***
 - Custom music created by me using Beepbox, which plays indefinitely.
 - Other tunes, which will also be made by me on Beepbox are yet to be added.

## Credits:

I used various tutorials in YouTube to form an understanding of pixel perfect collision along with the basics of pygame and the official pygame support documentation.
 
