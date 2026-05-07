class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        Map<Character,Character> closeAndOpen = new HashMap<>();

        closeAndOpen.put(')','(');
        closeAndOpen.put(']','[');
        closeAndOpen.put('}','{');

        for (Character c : s.toCharArray()){
            if (closeAndOpen.containsKey(c)){
                if (!stack.isEmpty() && stack.peek() == closeAndOpen.get(c)){
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}
