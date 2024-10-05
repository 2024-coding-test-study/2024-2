import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


class Main {
    static void add_graph(int[][] graph, int x, int y, int weight) {
        graph[x][y] = weight;
        graph[y][x] = weight;
    }

    static long DFS(int[][] graph, int start, long total) {
        for(int i = 1; i< (graph[0].length); i++) {
                total += graph[start][i]; // weight 추가
        }
        return total;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer token = new StringTokenizer(input.readLine());
        int vertax = Integer.parseInt(token.nextToken()); // vertax
        int edge = Integer.parseInt(token.nextToken()); // edge

        int[][] graph = new int[vertax+1][vertax+1]; // graph 값에 가중치를 넣으면 됨
        
        /** 깊이 우선 탐색으로 graph가 0이라면 더해주고 방문처리 */

        for(int i =1 ; i<= edge; i++) { // index = graph
            StringTokenizer token2 = new StringTokenizer(input.readLine());

            int x = Integer.parseInt(token2.nextToken());
            int y = Integer.parseInt(token2.nextToken());
            int weight = Integer.parseInt(token2.nextToken());

            add_graph(graph, x, y, weight);
        }

        long[] result_arr = new long[vertax+1];
        long answer = 2147483647;

        for(int i =1; i <= vertax; i++) {
            long total = 0;
            
            result_arr[i] = DFS(graph, i, total);

            if(result_arr[i] <= answer) {
                answer = result_arr[i];
            }
        }

        output.write(String.valueOf(answer));

        input.close();
        output.close();
    }
}

