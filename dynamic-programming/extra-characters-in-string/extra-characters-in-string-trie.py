class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes.
        self.is_word = False  # Flag to mark the end of a word.

def buildTrie(dictionary):
    root = TrieNode()
    for word in dictionary:
        node = root
        for ch in word:
            if ch not in node.children:  # If the character is not a child, create a new TrieNode.
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True  # Mark the end of the word.
    return root

def minExtraChar(s, dictionary):
    trie = buildTrie(dictionary)  # Build a Trie from the dictionary.
    n = len(s)
    dp = [float('inf')] * (n + 1)  # Initialize a dynamic programming table with infinity values.
    dp[-1] = 0  # The last position is initialized to 0 because no extra characters are needed there.

    for start in reversed(range(n)):
        dp[start] = dp[start + 1] + 1  # Initialize dp[start] by assuming an extra character is added.
        node = trie  # Start from the root of the Trie.
        for end in range(start, n):
            if s[end] not in node.children:
                break  # If the character is not in the Trie, break out of the loop.
            node = node.children[s[end]]  # Move to the next TrieNode.
            if node.is_word == True:  # If a word is found in the Trie, consider it.
                dp[start] = min(dp[start], dp[end + 1])  # Update dp[start] if necessary.
    return dp[0]  # The minimum number of extra characters needed at the beginning of the string is at dp[0].
