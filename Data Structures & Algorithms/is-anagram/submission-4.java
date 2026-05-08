class Solution {
    //input: s, t
    //types: String
    
    //Goal:
    // - if s and t contain the exact same characters (order doesn't matter) -> return true
    // - else -> return false

    //Initial plan:
    // - if length of s != t -> return false
    // - loop over characters in s, put into hashmap
    // - loop over characters in t, put into hashmap
    // - compare both hashmaps and if they have a mismatch in characters/values -> return false
    // - else -> return true

    //Complexities:
    // - space: O(1)
    // - time: O(n + m)
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> mapS = new HashMap<>();
        HashMap<Character, Integer> mapT = new HashMap<>();
        for (char c : s.toCharArray()){
            if (mapS.containsKey(c)){
                mapS.put(c, mapS.get(c) + 1);
            } else {
                mapS.put(c,1);
            }
        }
        for (char c : t.toCharArray()){
            if (mapT.containsKey(c)){
                mapT.put(c, mapT.get(c) + 1);
            } else {
                mapT.put(c,1);
            }
        }

        if (mapS.equals(mapT)) return true;
        return false;
    }
}
