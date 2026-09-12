## Welcome to The Pathways : The Game
An adventure game based on my story world of The Pathways, a civilization for criminals located on the interconnected rings of planets outside of Earths orbit. Created using the pygame library  in Visual Studio Code.

 Currently a work in progress as this is going to be a long project which will continue even after the end of the Stardance Challenge.

<img width="623" height="360" alt="Elli Kourousi_s Video - Sep 12, 2026" src="https://github.com/user-attachments/assets/78895c30-b1f0-4057-a12d-7ed958077979" />

## Authors

 - Elli Kourousi ([@Misted-River on GitHub](https://github.com/Misted-River/Python/tree/main))

## Installation

Try it:

_Currently only supports windows_
-> Unzip the folder and download the .exe file to run locally on your windows device

## How to play
 - Player controls Comet, a canine-like character using w,a,s,d keys
 - Shift to speed Comet up
 - Press and hold on all objects in scene 1 (click and hold on them) to pass into scene 2 and the end of the path!
 - (Scene 2 gameplay is under construction, but you can move around on the path to just look around so far)


## Features

**Scene 1 Coding**
 - Main character is moved by pressing w,a,s,d keys on a keyboard in the respective directions
 - Main character movement can be accelerated by pressing shift while w,a,s,d keys are pressed
 - If player hits on the edge of the path on-screen, a collision occurs which blocks character movement in direction of the obstacle -> Pixel perfect collision 
 - Screen scrolls along with character in both axes x and y, depending on characters distance to the edge of screen -> Character is always visible on-screen as the path moves.
 - Clickable items are present along the course of the path, when they a player clicks and holds with their mouse a label is shown on-screen.
 - End of scene is reached at the end of the path where a visible item, when touched by character, brings the player into scene 2.
 - Animated player character goes through a loop of 5 individual drawn frames to make the character appear to move visually

***Scene 2 Coding: (not complete yet):***
 - Different path is shown
 - Player movement is the same as scene 1, path scrolls as player moves
 - In scene 1, edge of path is not shown for aesthetic purposes, here in this scene I have yet to implement this
 
***Art :*** 
 - The art for the path, background, objects and some bits of the characters animation are work in progress for now
 - All art is drawn by me using Ibis Paint X drawing software on Ipad
 
 ***Music:***
 - Custom music created by me using Beepbox, which plays indefinitely

## Credits:

I used various tutorials in YouTube to form an undertanding of pixel perfect collision along with the basics of pygame.
 
