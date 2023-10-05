import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.split(" ");
        
        for (int i = 0; i < str.length; i++) {
            String tmp = str[i];
            String result = "";
            
            if (tmp.length() == 0) {
                answer += " ";
                continue;   
            }
                    
            result += tmp.substring(0, 1).toUpperCase();
            result += tmp.substring(1).toLowerCase();
            
            answer += result + " ";
        }
        
        if (s.substring(s.length()-1, s.length()).equals(" ")) {
            return answer;
        }
        
        return answer.substring(0, answer.length()-1);
    }
}