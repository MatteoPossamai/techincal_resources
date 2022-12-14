## KNAPSACK PROBLEM

How can I optimize the value of the items I can carry in my backpack, given their weight and the weight that the backpack can carry?

## SOLUTIONS:

### BRUTE FORCE

You can try combine each combination and see which one has the best value. The complexity is O(2^n).

### BEST WAY: DYNAMIC PROGRAMMING

The idea is to use a matrix to store the best value for each weight. The complexity is O(nW), where n is the number of items and W is the maximum weight.

#### PSEUDOCODE 

        public void knapsackDyProg(int W[], int V[], int M, int n) {
            int B[][] = new int[n + 1][M + 1];
            
            for (int i=0; i<=n; i++)
                for (int j=0; j<=M; j++) {
                    B[i][j] = 0;
                }
            
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j <= M; j++) {
                    B[i][j] = B[i - 1][j];
                    
                    if ((j >= W[i-1]) && (B[i][j] < B[i - 1][j - W[i - 1]] + V[i - 1])) {
                        B[i][j] = B[i - 1][j - W[i - 1]] + V[i - 1]; 
                    }
                    
                    System.out.print(B[i][j] + " ");
                }
                System.out.print("\n");
            }
            
            System.out.println("Max Value:\t" + B[n][M]);
            
            System.out.println("Selected Packs: ");
            
            while (n != 0) {
                if (B[n][M] != B[n - 1][M]) {
                    System.out.println("\tPackage " + n + " with W = " + W[n - 1] + " and Value = " + V[n - 1]);
                    
                    M = M - W[n-1];
                }
                
                n--;
            }
        }