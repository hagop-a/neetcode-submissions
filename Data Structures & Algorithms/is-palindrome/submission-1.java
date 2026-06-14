class Solution {
    public boolean isPalindrome(String s) {
        // use pointer starting beginning and right of string
        
        int pl = 0;
        int pr = s.length() - 1;

        while (pl < pr) {
            // check if alphanumeric
            while (pl < pr && !alphaNum(s.charAt(pl))) {
                pl++;
            }
            while (pl < pr && !alphaNum(s.charAt(pr))) {
                pr--;
            }

            char plc = Character.toLowerCase(s.charAt(pl));
            char prc = Character.toLowerCase(s.charAt(pr));
            if (plc != prc) {
                return false;
            }
            pl++; 
            pr--;
        }
        return true;
    }
    public boolean alphaNum(char c) {
    return (c >= 'A' && c <= 'Z' ||
        c >= 'a' && c <= 'z' ||
        c >= '0' && c <= '9');
    }
}



        /* 
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
        */
