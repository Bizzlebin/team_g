"""
File: model.py
The model for testing graph processing algorithms.
"""

from graph import LinkedDirectedGraph

class GraphDemoModel(object):
    """The model class for the application."""

    def __init__(self):
        self.graph = None
        self.startLabel = None

    def createGraph(self, rep, startLabel):
        """Creates a graph from rep and startLabel.
        Returns a message if the graph was successfully
        created or an error message otherwise."""
        self.graph = LinkedDirectedGraph()
        self.startLabel = startLabel
        edgeList = rep.split()
        for edge in edgeList:
            if not '>' in edge:
                # A disconnected vertex
                if not self._graph.containsVertex(edge):
                    self.graph.addVertex(edge)
                else:
                    self.graph = None
                    return "Duplicate vertex"
            else:
                # Two vertices and an edge
                bracketPos = edge.find('>')
                colonPos = edge.find(':')
                if bracketPos == -1 or colonPos == -1 or \
                   bracketPos > colonPos:
                    self._graph = None
                    return "Problem with > or :"
                fromLabel = edge[:bracketPos]
                toLabel = edge[bracketPos + 1:colonPos]
                weight = edge[colonPos + 1:]
                if weight.isdigit():
                    weight = int(weight)
                if not self.graph.containsVertex(fromLabel):
                    self.graph.addVertex(fromLabel)
                if not self.graph.containsVertex(toLabel):
                    self.graph.addVertex(toLabel)
                if self.graph.containsEdge(fromLabel, toLabel):
                    self.graph = None
                    return "Duplicate edge"
                self.graph.addEdge(fromLabel, toLabel, weight)
        vertex = self.graph.getVertex(startLabel)
        if vertex is None:
            self.graph = None
            return "Start label not in graph"
        else:
            vertex.setMark()
            return "Graph created successfully"

    def getGraph(self):
        """Returns the string rep of the graph or None if
        it is unavailable"""
        if not self.graph:
            return None
        else:
            return str(self.graph)

    def getStartLabel(self):
        return self.startLabel

    def run(self, algorithm):
        """Runs the given algorithm on the graph and
        returns its result, or None if the graph is
        unavailable."""
        if self.graph is None:
            return None
        else:
            return algorithm(self.graph, self.startLabel)
   
