import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.StringTokenizer;

public class B2531 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));


        // 1. 초밥의 최대 가지수를 count하는 문제임
        // 2. 쿠폰 번호는 중첩 사용 불가 무조건 1번만 사용이 가능하다.
        
        StringTokenizer token = new StringTokenizer(input.readLine());
        HashSet<Integer> set = new HashSet<>();

        int N, d, k, c; 

        N = Integer.parseInt(token.nextToken()); // 배열의 크기
        d = Integer.parseInt(token.nextToken()); // 초밥의 가지수
        k = Integer.parseInt(token.nextToken()); // 연속해서 먹는 접시의 수
        c = Integer.parseInt(token.nextToken()); // 쿠폰 번호


        // 끝의 배열을 만났다면 처음 배열로 돌아감
        int[] array = new int[N];

        for(int i = 0; i< N; i++) {
            array[i] = Integer.parseInt(input.readLine());
        }
        
        // 만약 다시 초기화 시 % N+1 해주면 재자리로 돌아가게 됨
        
        // for문을 단 한번만 쓰고 문제는 푸는 방법
        int index = 0;
        int increase_num = 0;
        int current_num = 0;
        int answer = 0;

        while(index < N) {
            set.add(c); // 쿠폰 부터 추가

            set.add(array[(index+increase_num)%N]);

            increase_num++;

            if(increase_num == k) {
                index++;
                increase_num = 0;

                current_num = set.size();

                if(answer < current_num) {
                    answer = current_num;
                }
                set.clear();
            }

            if(index == N-1) {
                break;
            }
        }  
        
        output.write(String.valueOf(answer));

        input.close();
        output.close();
    }
}
