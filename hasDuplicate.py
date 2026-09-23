class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for j in hashmap:
            if hashmap[j] > 1: 
                return True
        return False

# often in problems where u have to compare stuff in a given set of items, the brute way force has shit time complexity 
# we can use hashmaps to store the value of an item of the list in a more organized way so we dont have nested loops
# create a hashmap, and go through the items of the list, add the item of the list into the hashmap so that the key value pairs are the items and the amount of times they show up
# at the end, check if any values are > 1 => true that the list has dupes