import java.util.*;

class Solution {
    public long solution(long n) {
        
        String[] arr = Long.toString(n).split("");
        Arrays.sort(arr, Collections.reverseOrder());
        
        String tmp = "";
        
        for(String s : arr) {
            tmp += s;
        }
        
        return Long.parseLong(tmp);
    }
}