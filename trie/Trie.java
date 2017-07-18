import java.util.HashMap;
import java.util.Map;

/**
 * Implement a trie with insert, search, and starts with methods using hash map.
 */
class TrieNode {
    char ch;
    // has map store trie node
    HashMap<Character, TrieNode> children = new HashMap<Character, TrieNode>();
    boolean isLeaf;

    public TrieNode() {
    }

    public TrieNode(char ch) {
        this.ch = ch;
    }
}

public class Trie {
    private TrieNode root;
    // constructor
    public Trie() {
        root = new TrieNode();
    }

    /* Insert into the Trie
     * args :
     * key : String to insert into Trie
     * Time Complexity: O(len(word))
     */
    public void insert(String word) {
        HashMap<Character, TrieNode> children = root.children;
        // insert word char by char
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt (i);
            TrieNode root;
            /* Check status of that child node
             * If it is empty, them fill it
             * If it is present, them use this as the next root
             */
            if (children.containsKey(ch)) {
                root = children.get(ch);
            } else {
                root = new TrieNode(ch);
                children.put(ch, root);
            }
            children = root.children;

            //set leaf node
            if (i == word.length() - 1)
                root.isLeaf = true;
        }
    }

    /* Searches into the Trie
     * args:
     * key : string to search into Trie
     * Time complexity : O(len(word))
     */
    public boolean search(String word) {
        TrieNode root = searchNode(word);
        // if valid words return true
        if (root != null && root.isLeaf) {
            return true;
        }
        else {
            return false;
        }
    }

    /** Returns if there is any word in the trie
     * that start with the given prefix.
     */
    public boolean startsWith(String prefix) {
        // words not start with prefix then return false
        if (searchNode(prefix) == null) {
            return false;
        }
        else {
            return true;
        }
    }

    public TrieNode searchNode(String str) {
        Map<Character, TrieNode> children = root.children;
        TrieNode root = null;
        // validate the words
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (children.containsKey(ch)) {
                root = children.get(ch);
                children = root.children;
            } else {
                return null;
            }
        }
        return root;
    }

    public static void main(String[] args) {
        Trie node = new Trie();
        // Input keys words
        node.insert("the");
        node.insert("a");
        node.insert("there");
        node.insert("answer");
        node.insert("any");
        node.insert("by");
        node.insert("bye");
        node.insert("their");
        // Search for different keys words
        System.out.println(node.search("the"));
        System.out.println(node.search("these"));
        System.out.println(node.search("thaw"));
        System.out.println(node.search("their"));
    }
}
