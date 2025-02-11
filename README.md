---
# File Compressor - 
### Created by Brandon M.

## Overview

The File Compressor project is a Python application that allows users to compress multiple files into a single ZIP archive. It provides a simple graphical user interface (GUI) for selecting files to compress and choosing a destination folder for the compressed file.

This project was created while studying from the 20 projects in 60 days Udemy Course. 
## Features

- Compress multiple files into a single ZIP archive.
- Graphical User Interface (GUI) using FreeSimpleGUI library.
- Select files using a file browser dialog.
- Choose destination folder using a folder browser dialog.
- Provides feedback on the compression status. 

## Getting Started

### Prerequisites

- Python 3.x installed on your system. (Used 3.10.7)
- Required Python libraries: `FreeSimpleGUI`, `zipfile`, and `pathlib`.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-compressor.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd file-compressor
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Select files to compress:
   - Click on the "Choose" button next to "Select files to compress".
   - Navigate to and select one or more files. You can select multiple files using Ctrl (Cmd on macOS) or Shift.
   - Click "Open" to confirm your selection.

3. Select destination folder:
   - Click on the "Choose" button next to "Select Destination Folder".
   - Navigate to and select the destination folder where you want to save the compressed file.
   - Click "OK" or "Select Folder" to confirm your selection.

4. Compress files:
   - Click the "Compress" button to start compressing the selected files.
   - The application will display a message indicating the compression status.
   - Once compression is completed, a message "Compression Completed!" will appear.

### Notes

- Ensure that all selected files are accessible and not in use by other applications during compression.
- The application uses the FreeSimpleGUI library for the graphical interface. Make sure it is correctly installed and compatible with your Python environment.

### Contributing

Contributions are welcome! If you want to contribute to this project, please fork the repository and 
create a pull request with your proposed changes.


---
