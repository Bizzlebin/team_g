"""
File: view.py
The view for testing graph processing algorithms.
"""

from model import GraphDemoModel

from algorithms import shortestPaths, spanTree, topoSort

class GraphDemoView(object):
    """The view class for the application."""

    def __init__(self):
        self.model = GraphDemoModel()

    def run(self):
        """Menu-driven command loop for the app."""
        menu = "Main menu\n" + \
               "  1  Input a graph from the keyboard\n" + \
               "  2  Input a graph from a file\n" + \
               "  3  View the current graph\n" \
               "  4  Single source shortest paths\n" \
               "  5  Minimum spanning tree\n" \
               "  6  Topological sort\n" \
               "  7  Exit the program\n"
        while True:
            command = self.getCommand(7, menu)
            if   command == 1: self.getFromKeyboard()
            elif command == 2: self.getFromFile()
            elif command == 3:
                print(self.model.getGraph())
            elif command == 4:
                print("Paths:\n", self.model.run(shortestPaths))
            elif command == 5:
                print("Tree:", \
                      " ".join(map(str, self.model.run(spanTree))))
            elif command == 6:
                print("Sort:", \
                      " ".join(map(str, self.model.run(topoSort))))
            else: break

    def getCommand(self, high, menu):
        """Obtains and returns a command number."""
        prompt = "Enter a number [1-" + str(high) + "]: "
        commandRange = list(map(str, range(1, high + 1)))
        error = "Error, number must be 1 to " + str(high)
        while True:
            print(menu)
            command = input(prompt)
            if command in commandRange:
                return int(command)
            else:
                print(error)

    def getFromKeyboard(self):
        """Inputs a description of the graph from the keyboard
        and creates the graph."""
        rep = ""
        while True:
            edge = input("Enter an edge or return to quit: ")
            if edge == "": break
            rep += edge + " "
        startLabel = input("Enter the start label: ")
        print(self.model.createGraph(rep, startLabel))

    def getFromFile(self):
        """Inputs a description of the graph from a file
        and creates the graph."""
        fileName = input("Enter the file name: ")
        theFile = open(fileName, 'r')
        rep = theFile.readline().strip()
        startLabel = theFile.readline().strip()
        print(self.model.createGraph(rep, startLabel))
            
# Start up the application

GraphDemoView().run()

            
