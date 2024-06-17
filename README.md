# Tic-Tac-Net

Course Project for **PCS-2** (CSL2090)

Principles of Computer Systems-2 (PCS-2) covers the following concepts: 

       - Operating Systems
       - Computer Networking
       - Virtualization

## Description
This project combines the classic **Tic-Tac-Toe** game with **Socket Programming**. It allows two players to play against each other over a network, with one player acting as the server and the other as the client. The game runs on a **virtual machine** set up using Virtual Box. The main game logic is implemented using **pygame**. 

## File Structure
```
├── assets
│   ├── cover.png
│   ├── o.png
│   └── x.png
├── Presentation.pdf
├── README.md
├── Report.pdf
├── client.py 
├── server.py 
└── tic_tac_toe.py 

```

- `assets`: Directory containing images that provide the UI.
- `client.py`: Implements the client-side functionality to connect to the server.
- `server.py`: Implements server-side functionalities using **sockets**.
- `tic_tac_toe.py`: Contains the main game logic using **Pygame**.

## Pre-requisites

- **Python 3**: It can be  downloaded from [Python's official website](https://www.python.org/downloads/).
- **Pygame**: The game uses the Pygame library for graphics and game logic. Install Pygame using:

   ```sh
   pip install pygame


## Running Instructions

### Setup
- Clone the repository:
    ```bash
    git clone https://github.com/Anushka-1603/Tic-Tac-Net.git
    ```
### Starting the Game
- **Start the Server**:
   - Open a terminal.
   - Navigate to the project directory.
        ```bash
        cd Tic-Tac-Net
        ```
   - Run the following command:
     ```sh
     python3 server.py
     ```
   - The server will start listening for incoming connections.

- **Connect to the Server**:
   - Open another terminal tab or window.
   - Navigate to the project directory.
   - Run the following command:
     ```sh
     python3 client.py
     ```
   - This connects the client to the server, and the Tic Tac Toe window opens.

### Gameplay
   - Players take turns clicking on the game board to place their 'X' or 'O'.
   - The game ends when one player wins by achieving a row, column, or diagonal of their symbol ('X' or 'O') or if there's a draw.
   - The result is displayed on the screen.

## Demo
Click [here](https://drive.google.com/file/d/1jDkTQQH6JErs4v7CZwq__kgG7WSc_Fgv/view) to watch the demo.

## Contributers
- Anushka Singh(B22AI008) : [Anushka-1603](https://github.com/Anushka-1603)
- Hari Shubha(B22AI021) : [harishubha](https://github.com/harishubha)