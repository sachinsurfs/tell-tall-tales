import os
import torch

class Dictionary(object):
    def __init__(self):
        self.word2idx = {'<unk>':0}
        self.idx2word = ['<unk>']
        self.wordCount = {'<unk>':0}

    def add_word(self, word):
        word = word.lower()
        if self.wordCount[word] < 10:
            self.wordCount['<unk>'] += 1
            return self.word2idx['<unk>']
        else:
            if word not in self.word2idx:
                self.idx2word.append(word)
                self.word2idx[word] = len(self.idx2word) - 1
                return self.word2idx[word]

    def add_to_wordcount(self,word):
        word = word.lower()
        if word not in self.wordCount:
            self.wordCount[word] = 0
        self.wordCount[word] += 1
        return

    def __len__(self):
        return len(self.idx2word)

    def print_unknown_len(self):
        print(self.wordCount['<unk>'])

class Corpus(object):
    def __init__(self, path):
        self.dictionary = Dictionary()
        self.train = self.tokenize(os.path.join(path, 'train.txt'))
        self.valid = self.tokenize(os.path.join(path, 'valid.txt'))
        self.test = self.tokenize(os.path.join(path, 'test.txt'))
        self.dictionary.print_unknown_len()

    def tokenize(self, path):
        """Tokenizes a text file."""
        assert os.path.exists(path)

        #Replace low freq with unknown
        with open(path, 'r') as f:
            for line in f:
                words = line.split() + ['<eos>']
                for word in words:
                    self.dictionary.add_to_wordcount(word)


        # Add words to the dictionary
        with open(path, 'r') as f:
            tokens = 0
            for line in f:
                words = line.split() + ['<eos>']
                tokens += len(words)
                for word in words:
                    self.dictionary.add_word(word)

        # Tokenize file content
        with open(path, 'r') as f:
            ids = torch.LongTensor(tokens)
            token = 0
            for line in f:
                words = line.split() + ['<eos>']
                for word in words:
                    if word in self.dictionary.word2idx:
                        ids[token] = self.dictionary.word2idx[word]
                    else:
                        ids[token] = self.dictionary.word2idx['<unk>']
                    token += 1

        return ids
