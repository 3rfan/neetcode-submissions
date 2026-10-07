/*
* Goal: return true if s and t are anagrams of eachother, else return false
* Inputs: String s, String t
*
* Info/constraints: 
* - s and t only have lowercase english chars
* - s and t are non empty/null
* - s and t could be of unequal length -> guardrail
* 
* Initial plan:
* - sort the strings, then iterate through them if the chars at a certain index are not equal, return false
* - otherwise return true
* 
* Initial complexities:
* - time: O(nlogn), n = size of s, (quicksort)
* - space: O(logn), (stack) 
*/

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        int sPointer = 0;
        int tPointer = 0;
        while (sPointer < sChars.length){
            if (sChars[sPointer] != tChars[tPointer]) return false;
            sPointer++;
            tPointer++;
        }

        return true;
    }
}
