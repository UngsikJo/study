package JumpToJava.chap03;
import java.util.HashMap;
public class map0308 {
    public static void main(String[] args) {
        //맵 자료형은 파이썬의 딕셔너리와 닮아 있다
        //관계를 쉽게 표현해주는 자료형이다. Ex) 이름 = 홍길동, 생일 = 몇 월 며칠
        //Key와 value를 한쌍으로 갖는다.

        //1.기초적인 Hashmap
        //put메서드
        HashMap<String, String> map = new HashMap<>();//제네릭스를 사용한다.
        map.put("people", "사람");
        map.put("basball", "야구");
        System.out.println(map.get("people"));//사람 출력(people)Key에 저장된 "사람"value가 출력;
        System.out.println(map.get("Java"));//null출력
        //getOrDefault메소드 : get 메서드에서 value가 없으면 null이 리턴된다.
        //null대신 기본값을 얻고 싶다면 해당 메서드를 이용하면 된다.
        System.out.println(map.getOrDefault("java","자바"));//"자바" 출력

        //containsKey메서드 : 맴에 해당 Key가 있는지를 참 또는 거짓으로 리턴
        System.out.println(map.containsKey("people"));

        //remove메서드: 맵의 항복을 삭제하는 메서드. 해당 Key의 항복을 삭제한 후 value값을 리턴한다.
        System.out.println(map.remove("people"));//"사람"출력

        //size메서드는 맴 요소의 개수를 리턴
        map.put("peolpe","사람");
        System.out.println(map.size());

        //KeySet메서드 맴의 모든 Key를 모아서 리턴한다.
        System.out.println(map.keySet());





    }
}
