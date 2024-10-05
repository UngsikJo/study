package JumpToJava.chap03;

public class array0306 {
    public static void main(String[] args) {
        //배열선언시 자료형[]+배열명을 입력하여 선언한다.
        int[] odds = {1,3,5,7,9};

        String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};

        String[] weeks2 = new String[7];//배열의 길이 설정하기
        weeks2[0] = "월";//인덱스는 역시나 0부터 시작
        weeks2[1] = "화";
        weeks2[2] = "수";
        weeks2[3] = "목";
        weeks2[4] = "금";
        weeks2[5] = "토";
        weeks2[6] = "일";
        //String[] weeks = new String[]; 이렇게 초깃값없이 길이를 정해주지 않으면 오류가 발생한다.

        System.out.println(weeks2[3]);//배열값에 접근하기 : 인덱스를 활용하여 들어간다. 3이면 4번째 항목을 의미한다.

        for(int i = 0 ; i < weeks2.length ; i++){//반복문 C언어와 닮아 있다.
            System.out.println(weeks2[i]);
        }



    }
}
