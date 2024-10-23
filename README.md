**The Typing Test Game** challenges players to accurately and quickly type a random sentence while measuring their typing speed (in words per minute), accuracy, and total time taken. The game follows a clear progression of stages, from starting the test to resetting for another attempt. These stages are controlled by a **Finite-State Machine (FSM)** that ensures smooth transitions and a structured flow.

### **How the Game Works**

#### **Starting the Game**
- **Initial Screen**: When the game starts, the user sees an introductory screen or a prompt with an invitation to begin the typing test. This screen sets the tone for the test, and no interactions have taken place yet.
- **State**: The game is in the **Start** state. Here, the game waits for the user to click on the input box, signaling their readiness to start typing.

#### **Preparing to Type**
- **Input Box Activation**: Once the player clicks on the input box, they are placed in the **Waiting** state. The sentence to be typed appears, and the player is mentally preparing to type. The game is poised to start tracking their performance, but no time is being recorded until they press a key.
- **Idle Time**: The player can take as long as they need to prepare, as the timer will not start until the first keystroke. This gives users flexibility and helps them focus before the typing begins.

#### **Typing Stage**
- **Active Typing**: Upon the first keypress, the **Typing** state is triggered, and the timer begins counting down. The user types the sentence shown on the screen, and their input is displayed in real-time within the input box. The game tracks the user’s typing speed and accuracy, continuously monitoring each character typed.
- **Real-Time Feedback**: As the user types, they can see their input, and they can correct mistakes by using the backspace key. However, the focus remains on finishing the sentence as accurately and quickly as possible.
- **Ending the Typing Test**: When the user presses the Enter key, the test ends, and the system stops the timer.

#### **Result Calculation**
- **Post-Typing Analysis**: The game immediately transitions to the **Result** state, where it calculates three key metrics:
  - **Total Time**: The time taken from the first keystroke to the submission.
  - **Accuracy**: The percentage of correctly typed characters compared to the given sentence.
  - **Words Per Minute (WPM)**: The number of words typed per minute, based on the standard 5-character-per-word calculation.
- **Displaying the Results**: The game shows these results on the screen, giving players insight into their performance. It highlights their strengths and areas for improvement, providing encouragement to try again.

#### **Resetting the Game**
- **Preparing for Another Round**: After viewing the results, the player has the option to reset the game by clicking a **Reset** button. This triggers the **Reset** state, which clears the input box, generates a new sentence, and resets the timer.
- **Back to Start**: The game then returns to the **Start** state, ready for the player to take on another typing challenge.


This table outlines the states and transitions for the deterministic finite automaton (DFA) of the typing test game:

| Current State | Input                | Next State |
|---------------|----------------------|------------|
| START         | Game starts           | WAITING    |
| WAITING       | Type Character        | TYPING     |
| TYPING        | Key press             | TYPING     |
| TYPING        | Press Enter           | RESULT     |
| RESULT        | Click Reset button    | RESET      |
| RESET         | Game is reset         | START      |


