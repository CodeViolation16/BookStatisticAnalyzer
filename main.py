
def main():
    path_to_file = 'books/frankenstein.txt'
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        characterTable = countCharacter(file_contents)
        print(f'The book contains {word_count} words.')
        sortedTable  = sortResult(characterTable)
        print(sortedTable)

def count_words(text):
    words = text.split()
    return len(words)

def countCharacter(text):
    lowerText = text.lower()
    hashMap = {}
    for char in lowerText:
        if char in hashMap:
            hashMap[char] += 1
        else:
            hashMap[char] = 1
    return hashMap

def sort_on(d):
    return d["num"]

def sortResult(result):
    sortList = []
    for ch in result:
        sortList.append({"char": ch, "num": result[ch]})
    sortList.sort(reverse=True, key=sort_on)
    return sortList


if __name__ == "__main__":
    main()
