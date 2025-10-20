# Add item to table app Application

Welcome to the Add item to table app Application repository! This Tkinter-based GUI application allows users to enter a row into a table.

## The Design

### Functional Requirements

- The application shall display a window titled "Add item to table app".
- The application window shall have dimensions 1200x600 pixels.
- The background color of the application window shall be white or dark grey depending on light mode.
- The application shall display a label with the text "Enter a new item".
- The application shall provide an input field for the user to enter information for 3 rows.
- The application shall provide a "Submit" button. When clicked, the button shall trigger the action to save the item to a table.
- The application shall allow deleting of items.
- The appliation shall have appropriate data input such as dropdowns or text input.

### Non-Functional Requirements

- The application shall have an intuitive and user-friendly interface.
- The application shall respond to user input within 1 second.
- The application shall handle invalid input gracefully without crashing.
- The application code shall be well-structured and documented.
- The application shall run on any system that supports Python and Tkinter.
- The application shall use appropriate font sizes and color contrasts for readability.
- The application design shall allow for easy addition of new features.

### Screen mockups

The app was prototyped using [Figma](https://www.figma.com/design/CgwDsn1tYo8YffaNimjVfq/IFCS-HelloWorld?node-id=0-1&t=fSJk46k665IlDYDs-1).

![mockups](HelloName_proto.png)

### Code Design

The code design is summarised in the class diagram below.

The `App_Window` class inherits from the `ctk.CTk` class, which provides the foundational GUI window functionality. This inheritance allows `App_Window` to use and extend the methods and attributes of `ctk.CTk` to create a customised application window with specific features.  All the other classes are placed inside this class.

The `Frame` and `Table` class inherits from the `ctk.CTkFrame` class, which provides foundational responsive component functionality. This inheritance allows `Frame` and `Table` to be placed inside themselves in order to create a reponsive app. `Frame` is extended with flaxible layout and colour option and `Table` is extended with an interactive tkinter table.

![class-diagram](HelloName.png)
