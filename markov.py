"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return contents



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = input_text.split()
   
    #creates dictionary
    chains = {}
  

    #iterates over str(words)
    for i in range(len(words)-2):
        # chains.get(key) returns value or None 
        #if dict empty, returns None and else statement initiated
        # if the key exists, returns the value
        # key = (words[i], words[i +1])
        if chains.get((words[i], words[i + 1])):
            #there is a key that exist, its value is returned; append value to key
            chains.get((words[i], words[i + 1])).append(words[i + 2])

        # if dict is empty or key not exist, create the key=value     
        else:
            chains[(words[i], words[i + 1])] = [words[i + 2]]

        #rememberd: chains.get(key) returns value, and holds type; value is list for this function 

    print chains
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #create a link that is a key from dict
    #key is adding a word from value to lst(words)
    # for key, value in chains.items():
    #     words.append(random.choice(value))
        #random_word = random.choice(["words","first"])
        # print random_word
        # words.append(random_word)

        # chains[key[1],random from values] =
        # look up values with of above new key .get


        #words.append(chains.values())

    random_key = choice(chains.keys())
    words.append(random_key)

    while True:
        if random_key in chains:
            random_value = choice(chains.get(random_key))
            words.append(random_value)

            random_key = (random_key[1], random_value)

        else:
            break
   

    #print words
        # print link 
    #return " ".join(words)


#random.choice(values)

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
