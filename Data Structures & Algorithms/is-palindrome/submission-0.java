class Solution {
    public boolean isPalindrome(String s) {
        // reverse order, and check if string matches each letter
        // check for even or odd, if even, compare incrementally with first and last alphanumerical char,

        s = s.replaceAll("[^a-zA-Z0-9]", ""); 
        s = s.toLowerCase(); 
        int len = s.length();
        
        for (int i = 0; i < len/2; i++) {
            if (s.charAt(i) != s.charAt(len-1-i)) {
                return false;
            }
        }
        return true;
    }
}
