public class Setbits {
    public static void main(String[] args) {
        int n = 5;
        int ans = 0;
        while (n > 0){
            if ((n & 1)== 1){
                ans++;
            }
            n = n >> 1;
        }
        System.out.println(ans);
    }
}
