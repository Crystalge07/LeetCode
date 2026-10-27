class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count; 
        // initializing hash map, key = num, value = how many times it appears
        for (int n: nums){
            count[n]++; 
        } // the first time it sees a num, it creates a spot for it, then ++ to make it 1, and if it sees a number it's alr seen it ++ to increment the value 

        vector<vector<int>> buckets(nums.size()+1); // creates a vector of vectors (a vector is an array that can grow)
        for (auto p : count) { // goes through the count hash map, and p.first is the key, p.second is the value. the numnber gets put into this vector at the index matching its count
            buckets[p.second].push_back(p.first); // we bother to do this because now the most frequent numbers sit at the end, so we don't have to sort
        }

        vector<int> result;
        for (int i = buckets.size() - 1; i > 0; i--) { // starts at the back slot, walking left (so we start @ the largest)
            for (int num : buckets[i]) { // every number in this slot
                result.push_back(num); // adds to the answer
                if (result.size() == k) {
                    return result;
                }
            }   
        }
        return result;  // OUTSIDE both loops
    }  
};    