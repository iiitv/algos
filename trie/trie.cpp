#include <iostream>
#include <cstring>
using namespace std;

// Determine size of array
#define ARRAY_SIZE(a) sizeof(a) / sizeof(a[0])
// Alphabet size (# of symbols)
#define ALPHABET_SIZE 26
// Convert char to int value
// only 'a' to 'z' are allowed chars
#define CHAR_TO_INT(c) ((int)c - (int)'a')

// TrieNode class
class TrieNode {
	private:
		// Children of every Node
		class TrieNode *children[ALPHABET_SIZE];
		// Status of Leaf Node
		bool isLeaf;

	public:
		// Default Constructor
		TrieNode() {
			this->isLeaf = false;
			for (int i = 0; i < ALPHABET_SIZE; ++i)
				this->children[i] = NULL;
		}

		// Get leaf node status
		bool get_leaf_status() { return isLeaf; }
		// Set leaf node status
		void set_leaf_status(bool status) { this->isLeaf = status; }
		// Get Child status
		// Check if it is null or not
		bool get_child_status(int index) {
			if (!(this->children[index]))
				return true;
			return false;
		}

		// Initialize the child node, at specific index
		void initialize_child(int index) {
			this->children[index] = new TrieNode();
		}

		// Get child node at specific index
		class TrieNode *get_children(int index) {
			return this->children[index];
		}

		// Insert into the Trie, Implemetation is below
		void insert(string key);

		// Search into the Trie, Implementation is below
		bool search(string key);
};

/* Insert into the Trie
 * args :
 * key : String to insert into Trie
 * Time Complexity: O(len(key))
 */
void TrieNode::insert(string key) {
	// Determines the length of the key
	int length = key.length();

	// Temp variable for Crawling into the Trie
	class TrieNode *pCrawl = this;
	for (int level = 0; level < length; ++level) {
		// determine the index of the child node to use
		int index = CHAR_TO_INT(key[level]);
		/* Check status of that child node
		 * If it is empty, them fill it
		 * If it is present, them use this as the next root
		 */
		if (pCrawl->get_child_status(index))
			pCrawl->initialize_child(index);
		pCrawl = pCrawl->get_children(index);
	}
	// set the last node status as leaf node
	pCrawl->set_leaf_status(true);
};

/* Searches into the Trie
 * args:
 * key : string to search into Trie
 * Time complexity : O(len(key))
 */
bool TrieNode::search(string key) {
	// determines the length of the key
	int length = key.length();

	// Temp variable for crawling into the Trie
	class TrieNode *pCrawl = this;
	for (int level = 0; level < length; ++level) {
		// determine index of the child node to use
		int index = CHAR_TO_INT(key[level]);
		/* Check status of the child node
		 * If it is empty, them return false i.e. key not present into Trie
		 * If it is present, them start crawling from that node
		 */
		if (pCrawl->get_child_status(index))
			return false;
		pCrawl = pCrawl->get_children(index);
	}

	// Check that the last node reached is leaf node and not null as well
	return (pCrawl != NULL && pCrawl->get_leaf_status());
};

// Driver function
int main() {
	// keys to insert into Trie
	char keys[][8] = {"the", "a", "there", "answer", "any",
		"by", "bye", "their"};
	// Output the status of key
	char output[][32] = {"Not present in trie", "Present in trie"};
	// Root of Trie (Crawling starts from root, insertion as well)
	class TrieNode *root = new TrieNode();
	// Insertion into Trie
	for (unsigned long i = 0; i < ARRAY_SIZE(keys); ++i)
		root->insert(keys[i]);
	// Output of searched keys
	cout << output[root->search("the")] << endl;
	cout << output[root->search("these")] << endl;
	cout << output[root->search("thaw")] << endl;
	cout << output[root->search("their")] << endl;
	return 0;
}

