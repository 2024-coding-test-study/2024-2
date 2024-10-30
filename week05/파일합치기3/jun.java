import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class B13975 {
    public static int solve(PriorityQueue<Integer> minmap) {
        int total =0;

        while(!minmap.isEmpty()) {
            int size = ((minmap.size()+1)/2);
            int num1 = minmap.poll();
            int num2 = 0;
            if(!minmap.isEmpty()) {
                num2 = minmap.poll();
            }
            int result = num1+num2;

            minmap.offer(result);
            total += result;

            if(size == 1) {
                break;
            }
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int tc = Integer.parseInt(input.readLine());
        
        for(int i =0; i < tc; i++) {
            int repeat_num = Integer.parseInt(input.readLine());

            StringTokenizer token = new StringTokenizer(input.readLine());
            PriorityQueue<Integer> minmap = new PriorityQueue<>();

            for(int j =0; j < repeat_num; j++) {
                minmap.offer(Integer.parseInt(token.nextToken()));
            }
            output.write(String.valueOf(solve(minmap)));

            if(i < tc-1) {
                output.write("\n");
            }
        }

        input.close();
        output.close();
    }
}
