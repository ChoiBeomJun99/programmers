// 최대공약수, 최대공배수 문제는 유클리드 호제법을 사용해서 풀면 쉽다. a * b / (a와 b에 최대공약수) = 최소공배수
import java.util.*;

class Solution {
    // 최대공약수 구하기
        public int abs(int a, int b) {
            
            int tmp = 1;
            int result = 0;
            
            while (tmp <= a) {
                if (a % tmp == 0 && b % tmp == 0) {
                    result = tmp;
                }
                
                tmp ++;
            }
            
            return result;
        }
    
    public int solution(int[] arr) {
        
        // 길이가 한 개인 경우
        if (arr.length == 1) {
            return arr[0];
        }
        
        // 오름차순으로 sort 해주기 위해 리스트로 변경했다가 다시 int[]로 변경.
        List<Integer> listArr = new ArrayList<>();
        
        for (int tmp : arr) {
            listArr.add(tmp);
        }
        
        Collections.sort(listArr);
        arr = listArr.stream().mapToInt(x->x).toArray();
        
        // 직전까지의 최소공배수
        int prevLcm = arr[0] * arr[1] / abs(arr[0], arr[1]);
        
        // 본격 for문 돌기
        for (int i = 2; i < arr.length; i++ ) {
            prevLcm = prevLcm * arr[i] / abs(prevLcm, arr[i]);
        }
        
        return prevLcm;
    }
}