class Solution {
    public boolean isPalindrome(String s) {
        //Java Strings are immutable, you have to reassign 
        // otherwise you work with original (unmodified) String
        s = s.toLowerCase().replaceAll("[^\\p{Alnum}]", "");
        int start = 0;
        int end = s.length() - 1;

        while (start < end){
            if (s.charAt(start) != s.charAt(end)){
                return false;
            }

            start++;
            end--;
        }

        return true;
    }
}
