class MyMainClass {

    // properties
    int x = 5;
    int y = 6;


    // constructor
    public MyMainClass(int x, int y) {
        System.out.println("Constructor");
        this.x = x;
        this.y = y;
    }


    // getters and setters
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }


    // methods
    public void myMethod() {
        System.out.println("Hello World!");
    }

    // main method
    public static void main(String[] args) {
        int i = 22;
        if (i == 11) {
            System.out.println("Success");
        } else {
            System.out.println("Fail");
        }
        for (int j = 1; j <= 5; j++) {
            System.out.println(j);
        }
        // int non_init;
        // System.out.println(non_init + 2);

    }


}