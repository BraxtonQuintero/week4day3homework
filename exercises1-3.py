# Exercise 1

words = ['this' , 'is', 'a', 'sentence', '.']
print(words)

def swap(words1, index0, index1, index2, index3, index4):
    words1[index0], words1[index1], words1[index2], words[index3], words[index4] = words1[index4], words1[index3], words1[index2], words[index1], words[index0]
    return words1


swap(words, 0, 1, 2, 3, 4)

# Exercise 2

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def word_count(str):
    counts = {}
    words = str.split()

    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

word_count(a_text)

# Exercise 3

nums_list = [10,23,45,70,11,15]

def search_nums(nums_list, target):
    for n in range(len(nums_list)):
        if nums_list[n] == target:
            return n
    else:
        return 'This number is not in the list'

search_nums(nums_list, 15)