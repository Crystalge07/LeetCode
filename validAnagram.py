class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # obvi to be an anagram, they gotta be the same length
        s_hash_table = {} #initialize hash table for key value pairs
        for i in range(0, len(s)): #going through s
            if s[i] in s_hash_table: #looks through the keys
                s_hash_table[s[i]] += 1
            else: 
                s_hash_table[s[i]] = 1 

        t_hash_table = {}
        for i in range(0, len(s)): 
            if t[i] in t_hash_table: 
                t_hash_table[t[i]] += 1
            else: 
                t_hash_table[t[i]] = 1 

        return t_hash_table == s_hash_table

# firstly checks the length to make sure they have an equal num of chars
# checks the char of s, then puts it as a key in a hash table if not alr seen, and if seen, then assigns +1 to that keys value
# the key value pairs are the letter than the number of times it shows up
# same thing for t
# returns if they hash tables are the same bc order doesnt matter in python


        