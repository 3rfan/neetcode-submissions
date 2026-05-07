class Solution {
    public String mergeAlternately(String word1, String word2) {
        int w1 = 0;
        int w2 = 0;
        String res = "";

        while (w1 < word1.length() && w2 < word2.length()){
            res += "" + word1.charAt(w1) + word2.charAt(w2);

            w1++;
            w2++;
        }

        res+= word1.substring(w2);
        res+= word2.substring(w2);

        return res;
    }
}