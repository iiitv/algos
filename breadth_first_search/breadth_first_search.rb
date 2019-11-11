# Binary tree node
class Node
  attr_accessor :value, :left, :right

  def initialize(value)
    @value = value
  end
end

def build_tree(array, *indices)
  array.sort.uniq!
  mid = (array.length-1)/2
  first_element = indices[0]
  last_element = indices[1]

  return nil if !first_element.nil? && first_element > last_element

  root = Node.new(array[mid])
  root.left = build_tree(array[0..mid - 1], 0, mid - 1)
  root.right = build_tree(array[mid + 1..-1], mid + 1, array.length - 1)

  root
end

def breadth_first_search(search_value, tree)
  queue = [tree]
  visited = [tree]

  until queue.empty?
    current = queue.shift
    visited << current
    left = current.left
    right = current.right

    if current.value == search_value
      puts current
      exit
    end

    if !left.nil? && !visited.include?(left)
      if left.value == search_value
        puts left
        exit
      else
        visited << left
        queue << left
      end
    end

    if !right.nil? && !visited.include?(right)
      if right.value == search_value
        puts right.value
        exit
      else
        visited << right
        queue << right
      end
    end
  end
  puts 'nil'
end

binary_tree = build_tree([4, 7, 2, 8, 1, 1, 1, 30, 22, 4, 9])

breadth_first_search(9, binary_tree)
