
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B2467 {
    public static void binSearch(int[] array ,int start, int end) {
        
        int left = start;
        int right = end;
        
        long answer1 = array[left];
        long answer2 = array[right];
        long min = array[left] + array[right];

        while(left < right) {
            int current_num = array[left] + array[right];

            if(Math.abs(min) > Math.abs(current_num)) {
                min = Math.abs(current_num);
                answer1 = array[left];
                answer2 = array[right];
            } 

            if(current_num > 0) {
                right--;
            } else if(current_num < 0) {
                left++;
            } else if(current_num == 0) {
                break;
            }

        }
        System.out.print(answer1 + " "+ answer2);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int repeat_num = Integer.parseInt(input.readLine());

        int[] array = new int[repeat_num];

        StringTokenizer token = new StringTokenizer(input.readLine());

        for(int i =0; i< repeat_num; i++) {
            array[i] = Integer.parseInt(token.nextToken());
        }

        // 10만개라 브루트포스...음... O(n^2) X
        // 이분 탐색으로 가장 작은 값을 골랐을 때의 최적 값을 고르는 것
        // 기준이 0이 되야함

        binSearch(array, 0, repeat_num-1);

        input.close();
        output.close();
    }
}
