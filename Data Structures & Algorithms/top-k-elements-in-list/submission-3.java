class Solution {
    //Goal:
    // - given nums[], return k-most frequent elements
    
    //Initial plan (bad if k is large):
    // - create hashmap counts, keep track of input and frequency
    // - loop over nums[] and update hashmap
    // - go over hashmap k-times and get the value corresponding to the most frequent values
    // - return new list.of...

    //Initial complexities:
    //- Space: O(d + k) where d = num of distinct hashmap elements, k = num of k-most elements
    //- Time: O(k * d + n) where n = insertion into the hashmap for length n of nums[], k and d same as above
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (counts.containsKey(nums[i])){
                int currKey = nums[i];
                counts.put(currKey, counts.get(currKey) + 1);
            } else {
                counts.put(nums[i], 1);
            }
        }

        int[] result = new int[k];
        int freeResultIndex = 0;

        int mostFrequentCount = -1;
        int mostFrequentKey = 0;

        for (int i = 0; i < k; i++){
            for (Map.Entry<Integer, Integer> entry : counts.entrySet()){
                if (entry.getValue() > mostFrequentCount){
                    mostFrequentCount = entry.getValue();
                    mostFrequentKey = entry.getKey();
                }
            }

            result[freeResultIndex] = mostFrequentKey;
            freeResultIndex++;
            counts.remove(mostFrequentKey);
            
            mostFrequentCount = -1;
        }

        return result;
    }
}
