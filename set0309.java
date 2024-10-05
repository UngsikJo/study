package JumpToJava.chap03;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
public class set0309 {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>(Arrays.asList("H","e","l","l","o"));
        System.out.println(set);
        //중복을 허용하지 않는다.
        //순서가 없다.

        //교집합, 합집합, 차집합 구하기
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1,2,3,4,5,6));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4,5,6,7,8,9));

        //교집합 구하기 : retainAll메서드를 사용
        HashSet<Integer> intersection = new HashSet<>(s1);
        intersection.retainAll(s2);//교집합수행
        System.out.println(intersection);

        //합집합 구하기 : addAll메서드를 사용
        HashSet<Integer> union = new HashSet<>(s1);//s1으로 union생성
        union.addAll(s2);//합칩합 수행
        System.out.println(union);

        //차집합구하기
        HashSet<Integer> substract = new HashSet<>(s1);
        substract.removeAll(s2);//차집합수행
        System.out.println(substract);

        //집합자료형과 관련된 메서드 - add,addAll,remove
        //add메서드
        HashSet<String> set1 = new HashSet<>();
        set1.add("Jump");
        set1.add("To");
        set1.add("Java");
        System.out.println(set1);

        //addAll 한꺼번에 여러개 추가
        HashSet<String> set2 = new HashSet<>();
        set2.add("Jump");
        set2.addAll(Arrays.asList("To", "Java"));
        System.out.println(set2);

        //remove메서드
        HashSet<String> set3 = new HashSet<>(Arrays.asList("Jump","To","Java"));
        set.remove("To");
        System.out.println(set);


    }
}
