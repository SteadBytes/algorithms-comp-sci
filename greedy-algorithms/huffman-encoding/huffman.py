from queue import PriorityQueue
import re
import unittest


class Node:
    """ Class representing a Node in a binary tree.

    Contains pointers to left and right children.
    Can also be associated with a symbol and a weight.
    """
    left = None
    right = None
    symbol = None
    weight = 0

    def __init__(self, i, w):
        self.symbol = i
        self.weight = w

    def setChildren(self, left, right):
        """Add pointers to children nodes.
        Args:
            left (:obj:`Node`): Node object to the left in tree
            left (:obj:`Node`): Node object to the right in tree
        """
        self.left = left
        self.right = right

    def __str__(self):
        return ("Node object: \n symbol = %s \n weight = %s \n"
                "children= % s, % s") % (self.symbol, self.weight, self.left, self.right)

    # Comparison methods for use in PriorityQueue
    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight


def create_huffman_codes(f):
    """Generates huffman codes for symbols with frequencies

    Args:
        f (dict): Symbols and corresponding frequencies {symb1:freq,...}
    Returns:
        (dict): Symbols and corresponding codes {symb1:code,...}
    """
    q = PriorityQueue()

    # create nodes for each input symbol and add to priority queue
    # in order of frequency
    for symbol, frequency in f.items():
        q.put(Node(symbol, frequency))

    # generate tree from smallest frequency symbols up
    # stop when just root node remains in priority queue
    while q.qsize() > 1:
        l = q.get()
        r = q.get()
        n = Node(None, r.weight + l.weight)
        n.setChildren(l, r)
        q.put(n)

    # dict for codes mutated by encode() function below
    prefix_codes = {}

    def encode(code_str, node):
        """Recursively generates prefix codes from huffman tree.

        Used internally within `huffman()` function, mutates `prefix_codes`
        dict defined within outer function.

        Args:
            code_str (str): Binary string to build codes from
            node (:obj:`Node`): Node object from huffman tree to traverse from
                                -> root node when calling initially
        """
        # only leaf nodes will have a symbol
        if node.symbol:
            if not code_str:
                # root node
                prefix_codes[node.symbol] = "0"
            else:
                prefix_codes[node.symbol] = code_str
        # not leaf node -> continue traversal
        else:
            # full binary tree: left->0, right -> 1
            encode(code_str + "0", node.left)
            encode(code_str + "1", node.right)

    # q now only contains root node
    encode("", q.get())

    return prefix_codes


def huffman_encode(s):
    """Encode a string to binary using Huffman Encoding.

    Args:
        s (str): String to encode
    Returns:
        (str, dict): Tuple containing the encoded string and a dict of the
                        input character->prefix code mapping.
    """
    symb_freqs = {ch: s.count(ch) for ch in set(s)}
    codes = create_huffman_codes(symb_freqs)
    pattern = re.compile('|'.join(codes.keys()))
    return pattern.sub(lambda x: codes[x.group()], s), codes


def huffman_decode(s, codes):
    """Decode a Huffman-encoded binary string.

    Args:
        s (str): Huffman-encoded binary string.
        codes (dict): Input character->prefix code mapping
    Returns:
        (str): Decoded string
    """
    code_to_char = {code: char for char, code in codes.items()}
    pattern = re.compile('|'.join(code_to_char.keys()))
    return pattern.sub(lambda x: code_to_char[x.group()], s)

# Example:
# input_string = "Hello World!"
# coded_string, codes = huffman_encode(input_string)
# decoded_string = huffman_decode(coded_string, codes)

# print("Input: %s" % input_string)
# print("Coded String: %s" % coded_string)
# print("Prefix Codes: %s" % codes)
# print("Decoded String: %s" % decoded_string)


class HuffmanTest(unittest.TestCase):
    def setUp(self):
        self.input_string = "Hello World!"
        self.symb_freqs = symb_freqs = {
            ch: self.input_string.count(ch) for ch in set(self.input_string)}
        self.encoded, self.codes = huffman_encode(self.input_string)

    def test_prefix_free(self):
        """Test all codes are prefix codes

        No whole code word is a prefix of any other code word in the system
        """
        code_re_patterns = [re.compile(code)
                            for char, code in self.codes.items()]

        for char, code in self.codes.items():
            for pattern in code_re_patterns:
                if pattern != re.compile(code):
                    self.assertIsNone(re.match(pattern, code))

    def test_code_lengths(self):
        """Test code lengths are inversely proportional frequency of character
        """
        # characters in self.input_string ASCENDING order by frequency
        char_order = sorted(self.symb_freqs, key=self.symb_freqs.get)
        # low freq -> long code, high freq -> short code

        # loop through adjacent values
        for x, y in zip(char_order, char_order[1:]):
            # compare adjacent values in char_order
            # 1st has lower freq than 2nd -> longer code than second
            self.assertGreaterEqual(len(self.codes[x]), len(self.codes[y]))

    def test_all_characters_encoded(self):
        """Test all characters have exactly one prefix code
        """
        self.assertEqual(set(self.codes.keys()), set(self.input_string))

    def test_decode(self):
        """Test encoded string is decoded back to the original
        """
        self.assertEqual(huffman_decode(
            self.encoded, self.codes), self.input_string)


if __name__ == '__main__':
    unittest.main()
