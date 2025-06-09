import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        PrintWriter out = new PrintWriter(System.out);
        
        int T = in.nextInt();
        while (T-- > 0) {
            int n = in.nextInt();
            int m = in.nextInt();
            // your logic here …
            // for example, build the fib array and result string:
            int[] fib = {0,1,2,3,5,8,13,21,34,55,89,144};
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < m; i++) {
                int x = in.nextInt(), y = in.nextInt(), z = in.nextInt();
                int mi = Math.min(x, Math.min(y, z));
                int ma = Math.max(x, Math.max(y, z));
                if (mi < fib[n]) sb.append('0');
                else if (fib[n] + fib[n-1] <= ma) sb.append('1');
                else sb.append('0');
            }
            out.println(sb);
        }
        
        out.flush();
    }
    
    // Fast input reader
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() throws IOException {
            while (st == null || !st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) return null;
                st = new StringTokenizer(line);
            }
            return st.nextToken();
        }
        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
        long nextLong() throws IOException {
            return Long.parseLong(next());
        }
        String nextLine() throws IOException {
            return br.readLine();
        }
    }
}
