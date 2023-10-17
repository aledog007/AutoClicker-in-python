# AutoClicker-in-python

Perfect for Cookie Clicker! ;)

This code creates a simple Auto Clicker application using Python. It uses PySimpleGUI for the graphical user interface (GUI) and the pynput library to handle mouse clicking and keypress events.

The GUI window displays a message "Press '-' to start/stop the Auto Clicker" and a button to close the application. It listens for keyboard events, specifically the '-' key, to toggle the Auto Clicker on and off.

The Auto Clicker itself is implemented in a separate thread. It repeatedly clicks the left mouse button with a slight delay between clicks while the clicking variable is set to 'True'.

The 'toggle_event' function handles keyboard events and toggles the clicking variable when the '-' key is pressed.

The main part of the program starts the Auto Clicker thread, and then it enters a loop to handle the GUI events. If the user closes the application window or clicks the "Close Application" button, the loop exits, and the program gracefully shuts down, closing the GUI window and stopping the Auto Clicker thread.

This code provides a basic Auto Clicker functionality with a user-friendly interface and the ability to start and stop clicking using the '-' key

see in picture

![AutoClicker](https://github.com/aledog007/AutoClicker-in-python/assets/141751722/22e262e8-4ffb-4a71-acb9-54c5ce34e636)
