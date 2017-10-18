# Depth first traversal in a Graph ( Directed and undirected )
module Traversal
  class DepthFirstTraversal
    
    def initialize(graph)
      @graph = graph
    end

    # Method to traverse the graph from a node in a depth first manner.
    def dfs(src)
      @visited = Array.new(@graph.number_of_nodes, false)
      @output = []
      dfs_recursive(src)
      puts @output.join(' --> ')
    end

    private

    # Recursively traverse the unvisited edges of the graph
    # and mark the nodes visited.
    def dfs_recursive(src)
      @visited[src] = true
      @output << src
      @graph.edges[src].each do |node|
        unless @visited[node]
          dfs_recursive(node)
        end
      end
    end
  end
end

# Module contains the Directed and undirected graph representations
module Graph
  # Adjacency List Representation of Undirected Graph
  class UndirectedGraph
    attr_reader :number_of_nodes, :edges

    def initialize(number_of_nodes)
      @number_of_nodes = number_of_nodes
      @edges = Array.new(@number_of_nodes, Array.new())
    end

    def add_edge(src, dest)
      @edges[src] << dest
      @edges[dest] << src
    end
  end

  # Adjacency List represenetation of Directed Graph
  class DirectedGraph
    attr_reader :number_of_nodes, :edges
    
    def initialize(number_of_nodes)
      @number_of_nodes = number_of_nodes
      @edges = Array.new(@number_of_nodes, Array.new())
    end
    
    def add_edge(src, dest)
      @edges[src] << dest
    end
  end
end


# Sample Test code for the above code.
# In future, when the Rspec is setup in the project, will be moved.
graph = Graph::UndirectedGraph.new(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

Traversal::DepthFirstTraversal.new(graph).dfs(2)

graph = Graph::DirectedGraph.new(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

Traversal::DepthFirstTraversal.new(graph).dfs(2)
