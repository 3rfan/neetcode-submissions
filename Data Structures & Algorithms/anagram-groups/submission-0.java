class Solution {
    //Goal:
    //- return sublists of anagram groupings, given a string array
    //- order not important
    //- single char == anagram

    //Initial plan (naive solution):
    //- iterate over array
    //- sort each string
    //- use a <String, List<Integer>> hashmap, to store sorted strings and indices of array
    //- we check each array item against the hashmap and update it accordingly
    //- Then we create a new ArrayList
    //- Then we loop over hashmap entries, and make sublists for each grouping (key)
    //- Return the new List<List<String>>

    //Initial Complexities:
    //- Space: O(m * n)
    //- Time: O(m * nlogn)
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<Integer>> map = new HashMap<>();

        for(int i = 0; i < strs.length; i++){
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            if (!map.containsKey(key)){
                map.put(key, new ArrayList<>());
            }

            map.get(key).add(i);
        }

        List<List<String>> result = new ArrayList<>();
        for (List<Integer> indices : map.values()){
            List<String> group = new ArrayList<>();
            for (int index : indices){
                group.add(strs[index]);
            }

            result.add(group);
        }

        return result;
    }
}
