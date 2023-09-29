import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> tmp = new ArrayList<Integer>();
        
        for (int a : arr) {
            if (a % divisor == 0) {
                tmp.add(a);        
            }
        }
        
        if (tmp.size() == 0) {
            tmp.add(-1);
        }
        
        tmp.sort(null);
        int[] answer = new int[tmp.size()];
        
        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i).intValue();
        }
        
        // Arrays.sort(answer);
        return answer;
    }
}


// import java.util.ArrayList;
// import java.util.Arrays;

// class Solution {
//     public int[] solution(int[] arr, int divisor) {
//         int[] answer = {};
//         ArrayList<Integer> list = new ArrayList<Integer>();
        
//         for(int i = 0;i<arr.length;i++){
//         	//배열의 값이 divisor로 나누어 떨어지면 리스트에 저장
//             if(arr[i]%divisor==0)
//                 list.add(arr[i]);
//         }
        
//         //리스트의 크기가 0인 경우 -1 저장
//         if(list.size()==0){
//             list.add(-1);
//         }
        
//         //list의 크기만큼 answer 생성
//         answer = new int[list.size()];
        
//         //list의 값 answer에 복사
//         for (int i = 0; i < list.size(); i++) {
//             answer[i] = list.get(i);
//         }
        
//         //answer을 오름차순으로 정렬
//         Arrays.sort(answer);
        
//         return answer;
//     }
// }