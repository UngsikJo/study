books = []
while True:
 print('=====================')
 print('하실 명령을 번호로 입력하세요')
 print('1. 책입력')
 print('2. 책삭제')
 print('3. 책검색')
 print('4. 책 전체 제목 출력')
 print('5. 종료')
 print('=====================')
 number = int(input('번호를 입력하시오'))  #input을 통해 받는 모든 것은 문자임. 숫자도 문자로 인식
 if number == 1 :
    book1 = input('책을 입력하시오')
    books.append(book1)
    print(books)
 if number == 2:
    book2 = int(input('삭제할 책의 번호를 입력하시오'))
    books.remove(books[book2-1])
    print('삭제되었습니다.')
    print(books)
 if number == 3:
    book3 = int(input('검색할 책의 번호를 입력하시오'))
    found = books[book3-1]
    print(found)
 if number == 4:
    print(books)
 if number == 5:
     break
 else :
    print('입력하신 번호는 없습니다')


