# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True
        return
    
    def startsWithHelper(self, prefix: str) -> TrieNode(): # type: ignore
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return
            cur = cur.children[i]
        return cur

    def search(self, word: str) -> bool:
        cur = self.startsWithHelper(word)
        return False if not cur else cur.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        return True if self.startsWithHelper(prefix) else False

# Example usage
trie = Trie()
print(trie.insert("apple"))      # Output: None
print(trie.search("apple"))      # Output: True
print(trie.search("app"))        # Output: False
print(trie.startsWith("app"))    # Output: True
print(trie.insert("app"))        # Output: None
print(trie.search("app"))        # Output: True