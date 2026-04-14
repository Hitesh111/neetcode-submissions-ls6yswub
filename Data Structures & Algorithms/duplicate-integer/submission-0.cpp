class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, bool> numMap;
        for (int num : nums) {
        // If the number is already in the map, we found a duplicate
            if (numMap.find(num) != numMap.end()) {
                return true;
            }
            // Otherwise, add the number to the map
            numMap[num] = true;
        }

    // If no duplicates were found, return false
    return false;
    }
};
