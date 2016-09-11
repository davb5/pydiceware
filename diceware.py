import random


def read_list(filename):
    words = []
    with open(filename, "r") as wordfile:
        started = False
        for line in wordfile:
            if not started and line == "\n":
                started = True
            elif started:
                if line == "\n":
                    break
                else:
                    words.append(line.split("\t")[1].strip())
    return words

if __name__ == "__main__":
    wordlist = read_list("diceware.wordlist.asc")
    words = [random.choice(wordlist) for x in range(5)]
    print("-".join(words))
