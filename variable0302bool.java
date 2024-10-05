package JumpToJava.chap03;

public class variable0302bool {
    public static void main(String[] args) {
        //boolean 불린또는 불리언이라고 읽는다.

        boolean isSuccess = true;
        boolean isTest = false;

        //사용예제
        int base=180;
        int height = 185;
        boolean isTall = height > base;

        if(isTall){
            System.out.println("키가 큽니다.");
        }
        int i = 3 ;
        boolean isodd = i%2==1;
        System.out.println(isodd);
    }
}
