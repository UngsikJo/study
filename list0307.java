package JumpToJava.chap03;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class list0307 {
    public static void main(String[] args) {
        //list는 배열과 비슷하지만 편리한 기능이 더 추가적으로 많은 자료형이다.
        //장점은 배열은 크기가 정해져 있지만, 리스트는 변할 수 있다는 데 있다.
        ArrayList pitches = new ArrayList();
        //ArrayList의 add메서드를 사용하면 요솟값을 추가 가능하다.
        pitches.add("138");
        pitches.add("129");
        pitches.add("142");
        pitches.add(0,"133");//첫번째 위치에 133을 삽입하고 싶다.
        pitches.add(1,"133");

        System.out.println(pitches.get(1));//get메소드는 특정 인덱스의 값을 추출할 수 있다
        System.out.println(pitches.size());//size 메소드는 요소의 개수 리턴한다.
        System.out.println(pitches.contains("142"));//contains메서드는 리스트안에 해당 항복이 있는지 판별해 그 결과를
        //boolean으로 리턴
        System.out.println(pitches.remove("129"));//삭제시 true
        System.out.println(pitches.remove(0));//삭제시 항목 리턴

        //제네릭스 : 자료형을 안전하게 사용할 수 있도록 만들어 주는 기능
        //String one = (String) pitches.get(0);//Object자료형을 String 자료형으로 형 변환

        ArrayList<String> pitches2 = new ArrayList<>();//제네릭스 사용예제
        pitches2.add("138");
        pitches2.add("129");

        String one = pitches2.get(0);//형 변환이 필요없다.
        String two = pitches2.get(1);

        //제네릭스사용 후 add 메소드로 Arraylsit 객체에 요소를 추구할 수 있다.
        //ArrayList<String> pitches3 = new ArrayList<>();

        //pitches3.add("138");
        //pitches3.add("129");
        //pitches3.add("142");
        //System.out.println(pitches3);

        //이미 문자열 배열이 있음녀 ArrayList를 좀 더 편하게 생성가능
        String[] data = {"138", "129", "142"};

        ArrayList<String> pitches3 = new ArrayList<>(Arrays.asList(data));

        System.out.println(pitches3);

        //String 배열 대신 String 자료형을 여러 개 전달하여 생성할 수 도 있다.
        ArrayList<String> pitches4 = new ArrayList<>(Arrays.asList("143", "153", "154"));

        System.out.println(pitches4);


        //String.join 138, 129, 142 세 요소로 이루어진 ArrauList를 만들었다. 그렇다면 ArrayList의 각 요소를
        //콤마(,)로 구분해서 1개의 문자열로 만들기
        ArrayList<String> pitches5 = new ArrayList<>(Arrays.asList("138", "129", "142"));
        String result3 = "" ;
        for(int i =0; i <pitches5.size();i++){
            result3 += pitches5.get(i);
            result3 += ",";
        }
        result3 = result3.substring(0,result3.length()-1/*마지막 콤마는 제거*/);
        System.out.println(result3);
        //join사용시 ->더 간단
        ArrayList<String> pitches6 = new ArrayList<>(Arrays.asList("154","142","123"));

        String result4 = String.join(",",pitches6);//요소들 사이에 ","콤마를 끼워 처리
        System.out.println(result4);

        //String.join("구분자", 리스트 객체)
        //<배열>에서도 사용가능
        String[] pitches7 = new String[]{"138","129","142"};//배열선언
        String result5 = String.join(",",pitches7);
        System.out.println(result5);

        //리스트 정렬하기
        ArrayList<String> pitches8 = new ArrayList<>(Arrays.asList("138","129","142"));
        pitches8.sort(Comparator.naturalOrder());//오름차순으로 정렬
        System.out.println(pitches8);
        //Comparator.naturalOrder()오름차순 정렬
        //Comparator.reverseOrder()내림차순 정렬
    }
}
