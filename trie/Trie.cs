using System;
using System.Collections.Generic;

class TrieNode
{
    public char c;
    public Dictionary<char, TrieNode> children;
    public bool isWord;

    public TrieNode()
    {
        children = new Dictionary<char, TrieNode>();
    }

    public TrieNode(char c)
    {
        this.c = c;
        children = new Dictionary<char, TrieNode>();
    }
}

public class Trie
{
    private TrieNode root;

    public Trie()
    {
        root = new TrieNode();
    }

    /// <summary>
    /// Inserts a word into the Trie
    /// Time Complexity: O(len(word))
    /// </summary>
    /// <param name="word">The word to insert</param>
    public void Insert(String word)
    {
        TrieNode curr = root;

        foreach (char c in word)
        {
            if (!curr.children.ContainsKey(c))
                curr.children[c] = new TrieNode(c);

            curr = curr.children[c];
        }

        curr.isWord = true;
    }

    /// <summary>
    /// Searches the trie for a word
    /// Time Complexity: O(len(word))
    /// </summary>
    /// <param name="word">The word to search for</param>
    /// <returns>True if the word was found, false otherwise</returns>
    public bool Search(String word)
    {
        TrieNode curr = root;

        foreach (char c in word)
        {
            if (!curr.children.ContainsKey(c))
                return false;

            curr = curr.children[c];
        }

        return curr.isWord;
    }

    public static void Main()
    {
        Trie dictionary = new Trie();
        // Input keys words
        dictionary.Insert("the");
        dictionary.Insert("a");
        dictionary.Insert("there");
        dictionary.Insert("answer");
        dictionary.Insert("any");
        dictionary.Insert("by");
        dictionary.Insert("bye");
        dictionary.Insert("their");
        // Search for different keys words
        Console.WriteLine(dictionary.Search("the"));
        Console.WriteLine(dictionary.Search("these"));
        Console.WriteLine(dictionary.Search("thaw"));
        Console.WriteLine(dictionary.Search("their"));
    }
}
