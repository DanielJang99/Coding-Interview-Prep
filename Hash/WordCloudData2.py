import unittest


class WordCloudData(object):

    def __init__(self, input_string):
        
        self.words_to_counts = {}
        self.parse_words(input_string)
        
    def parse_words(self, input_string):
        
        current_start_index = 0 
        current_word_length = 0
        
        for i, character in enumerate(input_string):
            if i == len(input_string) -1 :
                if character.isalpha():
                    current_word_length +=1 
                if current_word_length > 0:
                    current_word = input_string[current_start_index: current_start_index+current_word_length]
                    self.add_word_to_dict(current_word)
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_start_index: current_start_index+current_word_length]
                    self.add_word_to_dict(current_word)
                    current_word_length = 0 
            elif character == '.':
                if i < len(input_string) -1 and input_string[i+1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_start_index: current_start_index+current_word_length]
                        self.add_word_to_dict(current_word)
                        current_word_length = 0 
            elif character.isalpha() or character =='\'':
                if current_word_length == 0:
                    current_start_index = i 
                current_word_length += 1 
            elif character == '-':
                if i > 0 and input_string[i-1].isalpha() and input_string[i+1].isalpha():
                    current_word_length +=1 
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_start_index: current_start_index+current_word_length]
                        self.add_word_to_dict(current_word)
                        current_word_length = 0
    # Careful—if you thought of building up the word character by character (using +=), you'd be doing a lot more work than you probably think. Every time we append a character to a string, Python makes a whole new string. If our input is one long word, then creating all these copies is O(n^2) time. 
    #Instead, we keep track of the index where our word starts and its current length. Once we hit a space, we can use string slicing to extract the current word to append to the list. That keeps our split function at O(n)O(n) time.

    def add_word_to_dict(self, word):
        if word in self.words_to_counts:
            self.words_to_counts[word] +=1 
        elif word.lower() in self.words_to_counts: 
            self.words_to_counts[word.lower()] +=1 
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1 
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]
        else:
            self.words_to_counts[word] = 1

    
# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)