### Python Timeline Application (Doubly-Linked List)

Developed a custom chronological event management application in Python using a doubly-linked list data structure.

#### Key Features
- Dynamic event insertion while maintaining chronological order  
- Targeted event removal using bidirectional search (`front` and `back`)  
- In-place sorting of events  
- Event counting and traversal support  
- Object-oriented design:
  - `Timeline` and `Event` classes  
  - Encapsulated pointer management (`next`, `previous`)  
  - Ensures list integrity across all operations

#### Technical Design
- Implemented using Python and OOP principles  
- Doubly-linked list allows efficient insertion, deletion, and traversal  
- Supported operations include:
  ```python
  add_event(...)      # Insert chronologically
  remove_event(...)   # Remove via bidirectional search
  sort(...)           # Sort ascending or descending
  get_count(...)      # Return number of events
