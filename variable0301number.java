package JumpToJava.chap03;

public class variable0301number {
    public static void main(String[] args) {
        //정수
        int age = 10;
        long countOfStar =  81723987132132L;

        //실수
        float pi = 3.14F;
        double morePi = 3.14432535345;
        double d1 = 1.234e2; //지수 표현식

        //8진수 16진수
        int octal = 023;//십진수 19
        int hex = 0xC3;//십진수 195

        //숫자연산
        int a = 10;
        int b = 5;
        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/b);

        //나눗셈 나머지
        System.out.println(7%3);//1
        System.out.println(3%7);//3

        //증감연산
        int i = 0;
        int j = 10;
        i++;
        j--;
        System.out.println(i);//1
        System.out.println(j);//9

        //증감연산 위치를 이용한 결과값 확인
        int t = 0;
        System.out.println(t++);//0
        System.out.println(t);//1

        int r = 0;
        System.out.println(++r);
        System.out.println(r);

    }
}
