# Othello-Game-Project

## Introduction
This project implements the classic Othello game in either Prolog or Python, adhering to specific guidelines and requirements for implementation and gameplay.

## Project Requirements
- **Game Mode**: Human vs. Computer mode and Human vs Human.
- **Algorithm**: Utilize alpha-beta pruning algorithm for computer moves.
- **Game Features**:
  - Game controller to manage player roles, moves, and game state.
  - Proper knowledge representation of the game state.
  - Utility function for evaluating game states.
  - Implementation of alpha-beta pruning algorithm.
  - Support for different difficulty levels (Easy, Medium, Hard) based on algorithm depth.

## Game Overview
Othello is a strategy board game played on an 8×8 board where players compete to capture the opponent's pieces by outflanking them with their own pieces.

## Game Setup
- Initially, the board is set up with two black and two white disks in the center.
- Each player starts with 30 disks of their color.

## How to Play
1. Black makes the first move.
2. Players take turns placing their disks on empty squares adjacent to opponent's pieces to outflank and capture them.
3. Captured disks are flipped to the capturing player's color.
4. Game ends when no more moves are possible or when a player runs out of disks.
5. The player with more disks of their color wins.

## Game Rules
- Black always moves first.
- Missing a turn occurs if no disks can be outflanked.
- Disks can outflank multiple opponent's disks in a straight line.
- Players cannot skip over their own disks to outflank opponents.
