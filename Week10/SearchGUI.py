import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sqlite3
class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create the GUI elements
        self.label = QLabel("Enter search query:")
        self.line_edit = QLineEdit()
        self.search_button = QPushButton("Search")
        
        # Add the GUI elements to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.search_button)
        
        # Set the layout for the window
        self.setLayout(layout)
def search_database(query):
    # Connect to the SQLite database
    conn = sqlite3.connect("C:/Users/Nattavee Narischat/Desktop/softdev2/Week10/inverted_index2.db")
    
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    
    # Execute the search query
    cursor.execute("SELECT * FROM documents WHERE Body LIKE ?", (f"%{query}%",))
    
    # Fetch the results
    results = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Return the results
    return results
class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create the GUI elements
        self.label = QLabel("Enter search query:")
        self.line_edit = QLineEdit()
        self.search_button = QPushButton("Search")
        
        # Add the GUI elements to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.search_button)
        
        # Set the layout for the window
        self.setLayout(layout)
        
        # Connect the search button to a function
        self.search_button.clicked.connect(self.perform_search)
    
    def perform_search(self):
        # Get the search query from the line edit
        query = self.line_edit.text()
        
        # Search the database
        results = search_database(query)
        
        # Display the results in a message box
        if results:
            message = "\n".join([f"{result[0]} - {result[1]}" for result in results])
        else:
            message = "No results found."
        
        QMessageBox.information(self, "Search Results", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())
