class Solution {
    public boolean validPalindrome(String s) {
        int l = 0;
        int r = s.length() -1;

        while (l < r){
            if (s.charAt(l) != s.charAt(r)){
                boolean leftRange = validRange(s,l + 1,r);
                boolean rightRange = validRange(s,l,r - 1);

                return (leftRange || rightRange);
            }

            l++;
            r--;
        }

        return true;
    }

    public boolean validRange(String s, int l, int r){
        while (l < r){
            if (s.charAt(l) != s.charAt(r)){
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
}