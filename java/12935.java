import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        
        if (arr.length == 1) {
            int[] result = {-1};
            return result;
        }
        
        int[] answer = new int[arr.length - 1];
        
        int min = arr[0]; //하나의 값을 기준으로 잡음.    
        for (int a : arr) {
            min = Math.min(a, min);
        }
        
        int idx = 0;
        for (int a : arr) {
            if (a == min) {
                continue;
            }
            
            answer[idx] = a;
            idx++;
        }
        
        return answer;
    }
}