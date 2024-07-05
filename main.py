import FreeSimpleGUI as gui
from zip_creator import make_archive

"""Created by Brandon Mathews during 20 Python Projects in 60 Days on Udemy."""


# Define the window title
window_title = "File Compressor"

# Define the layout of the GUI window
layout = [
    [gui.Text("Select files to compress"), gui.Input(), gui.FilesBrowse("Choose", key="file")],
    [gui.Text("Select Destination Folder"), gui.Input(), gui.FolderBrowse("Choose", key="folder")],
    [gui.Button("Compress")],
    [gui.Text("", key="output")]
]

# Create the GUI window with specified title and layout
window = gui.Window(window_title, layout)

# Event loop to handle user interactions
while True:
    # Read events and values from the window
    event, values = window.read()

    # Close the window if the close button is clicked
    if event == gui.WIN_CLOSED:
        break
    # Handle compress button click event
    elif event == "Compress":
        # Get selected file paths and destination folder from the GUI input fields
        filepaths = values["file"].split(";")  # Split file paths by ';' as they are returned as a string
        folder = values["folder"]

        # Validate if files are selected
        if not filepaths:
            gui.popup("Please select files to compress!")
            continue

        # Validate if destination folder is selected
        if not folder:
            gui.popup("Please select a destination folder!")
            continue

        try:
            # Attempt to create a zip archive with selected files in the specified folder
            make_archive(filepaths, folder)
            # Update output text to inform user about successful compression
            window["output"].update(value="Compression Completed!")
        except Exception as e:
            # Display error message if any exception occurs during compression
            gui.popup_error(f"Error during compression: {e}")

# Close the GUI window after the event loop ends
window.close()
