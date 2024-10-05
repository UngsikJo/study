package JumpToJava.chap03;

public class StringBuffer0305 {
    public static void main(String[] args) {
        //StringBuffer : 문자열을 추가하거나 변경할 때 주로 사용하는 자료형
        StringBuffer sb = new StringBuffer();//객체 생성
        sb.append("hello");//문자열 생성하는 예제
        sb.append(" ");
        sb.append("jump to java");
        String result = sb.toString();//StringBuffer 자료형을 String자료형으로 변경함.
        System.out.println(result);

        //첫번째 예제와 결과는 같지만 내부적으로는 메모리를 사용하는 과정이 다르다.
        //StringBuffer사용시 객체를 한번만 생성하지만 두번쨰 예제에서는 +를 만날 때마다 String객체를 생성하므로 4개의 String자료형 객체를 만들어진다.
        String result1 = "";
        result1 += "hello";
        result1 += " ";
        result1 += "jump to java";
        System.out.println(result1);
        //문자열을 추가하거나 변경하는 작업이 많을 시 StringBuffer를 사용하고 적으면 String

        //StringBuilder는 StringBuffer 비슷한 자료형으로 사용법도 같다.
        StringBuilder sb1 = new StringBuilder();
        sb1.append("hello");
        sb1.append(" ");
        sb1.append("jump to java");
        String result2 = sb1.toString();
        System.out.println(result2);
        //StringBuffer는 멀티스레드 환경에서 안전하고 StringBuilder는 StringBuffer보다 성능이 우수하다는 장점이 있다.
        //따라서 동기화를 고려할 필요가 없는 상황에서는 StringBuffer보다 StringBuilder를 사용하는 것이 유리하다

        //insert메서드는 특정 위체에 문자열을 삽입가능
        StringBuffer sb3 = new StringBuffer();
        sb3.append("jump to java");
        sb3.insert(0, "hello ");
        System.out.println(sb3.toString());

        //substring메서드
        StringBuffer sb4 = new StringBuffer();
        sb4.append("Hello jump to java");
        System.out.println(sb4.substring(0,4));
    }
}
