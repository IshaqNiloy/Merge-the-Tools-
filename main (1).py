import re

def merge_the_tools(string, k):
    my_list = []
    my_list = re.findall('[A-Z]{0,%s}' %k, string)
    for i in range(len(my_list) - 1):
        #Converting the string to a set to keep only the distinct characters.
        #The second parameter of the sorted function maintains the order of characters in the list as it was in the initial input
        s = sorted(set(my_list[i]), key = my_list[i].index)
        s = ''.join(s)
        print(s)
    # your code goes here



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k

