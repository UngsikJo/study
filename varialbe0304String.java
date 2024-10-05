package JumpToJava.chap03;

public class varialbe0304String {
    public static void main(String[] args) {
        //문자열의 앞과 뒤는 쌍따옴표로 감싸야 한다.("")
        String a = "Happy java";
        String b = "a";
        String c = "123";

        //new키워드는 객체를 만들 떄 사용한다. 문자열을 표현할 떈 가급적 첫번쨰 방식을 사용하는 것이 좋다.
        String a1 = new String("Happy java");
        String b1 = new String("a");
        String c1 = new String("123");

        //원시 자료형 int, long, double, float, boolean, char은 new키워드로 값을 생성 불가
        boolean result = true;
        char  a2 = 'A';
        int i =10000;


        //equals 메서드는 문자열 2개가 같은지를 비교하여 결괏값을 리턴한다.
        String a3 = "hello";
        String b3 = "java";
        String c3 = "hello";
        System.out.println(a3.equals(b3));
        System.out.println(a3.equals(c3));

        //메서드대신 ==연산자를 사용한 예
        String a4 ="hello";
        String b4 = new String("hello");
        System.out.println(a4.equals(b4));
        System.out.println(a4==b4);//false를 리턴한다 왜냐하면 ==연산자는 2개의 자료형이 같은 객체인지를 판별하기 떄문이다.

        //indesOf메서드 몇번째 인덱스에 해당 문자열이 포함되어 있는지 알려줌
        String a5 = "Hello Java";
        System.out.println(a5.indexOf("Java"));//포함 되어 있지 않을 시 -1리턴
        //contains메서드는 문자열이 포함되어 있는 여부를 리턴
        String a6 = "Hello Java";
        System.out.println(a.contains("Java"));

        //charAt메서드
        String a7 = "Hello java";
        System.out.println(a6.charAt(6));//6번째 인덱스의 문자를 리턴해준다.

        //replaceAll메서드
        String a8 = "Hello Java";
        System.out.println(a8.replaceAll("Java", "World"));//Java를 World로 대체하여 출력

        //substring메서드
        String a9 = "Hello java";
        System.out.println(a9.substring(0,4));//Hell출력 입력지점 유의사항 (시작위치<= a < 끝위치)

        //toUpperCase메서드 모두 대문자로 변경
        String a10 = "Hello java";
        System.out.println(a10.toUpperCase());

        //split메서드
        String a11 = "a:b:c:d";
        String[] result1 = a11.split(":");//result는 {"a", "b", "c", "d"}

        //문자열 포매팅
        System.out.println(String.format("I eat %d apples.", 3)); //숫자//C언어랑 비슷함. 근데 foramt메서드를 적어줘야지 쓸 수 있음.
        System.out.println(String.format("I eat %s apples", "five"));//문자열

        //숫잣값을 나타내는 변수 대입
        int number = 3;
        System.out.println(String.format("I eat %d apples", number));//number를 %d에 대입

        /*
        * <%s 문자열  : 자동으로 문자열로 바꾸기 때문에 숫자든 문자열이든 아무거나 대입 가능>
        *- %10s hi를 대입 하면 공백 8칸에 h,i를 2칸을 채워서 출력한다.
        *- %-10s 앞에 h,i채우고 그 뒤로 8칸을 공백으로 출력한다.
        * %c 문자 1개
        * %d 정수
        * <%f 무동 소수>
        * -%.4f : 소수점 4자리까지만 출력하라
        * -%10.4f : 전체길이 10칸 소수점 4자리와 .을 포함하여 6칸을 뒤로 채우고 앞에 4칸을 공백으로 채운다.
        * %o 8진수
        * %x 16진수
        * %% %w자체 출력
        *
        * */

        //System.out.printf메서드
        System.out.printf("I eat %d apples.", 3 );//
    }
}
