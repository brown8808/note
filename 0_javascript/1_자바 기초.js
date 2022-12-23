// developer.mizilla.org 참고 사이트 엠디엔?

// name = "mike"; // 문자형 String
// age = 30;
// 이렇게 변수를 선언하는건 위험함 / 유일하지 않을 수 있기 때문

// let name = "mike"; // let은 변경 가능한 함수, 생략 가능
// const message = "I'm a boy"; // 'I\'m a boy' 특문 선언
// Nan = not a number
// const 절대로 바뀌지 않는 상수 / 수정X
// 일단 모두 const로 선언 후 변경 건만 let으로 변경
// Boolean = true / false
// typeof 연산자
// console.log(typeof 3); "number"
// console.log(typeof name); "string"
// console.log(typeof true); "boolean"
// console.log(typeof null); "object" 오브잭트는 객체형임 null != 객체 / 객체가 아님! 
// console.log(typeof undefined); "undefined"

// alert 알려줌 / 알림창
// prompt 입력 받음 
// confirm 확인받음 컨펌은 확인, 취소 두 개의 선택이 있음
// const name = prompt("이름을 입력하세요."); 함수를 실행하는 괄호 안에서 들어가는 것을 인수라고함
// alert('안녕하세요, ${name}님. 환영합니다.')
// const name = prompt("예약일을 입력해주세요.", "2020-10-") 프롬프트는 2개의 인수값을 받을 수 있음
// const isAdult = confirm("당신은 성인 입니까?");
// console.log(isAdult);
// 창이 떠있는 동안은 스크립트가 정지됨, 스타일링X

// prompt로 입력 받은 자료는 -> 문자형임, 자동 형변환에 유의 "6" + "2" = 62  // "6" + "2" / 2 = 4
// 의도를 가지고 원하는 타입으로 변환해주는 것을 '명시적 형변환'
// console.log(Number("1234")); 이것은 숫자형으로 변환 Int가 아니네? 안에 글자가 들어있다면 NaN으로 반환
// True, False는 숫자형으로 변환시 1, 0 으로 변환됨
// Number(null) = 0
// Number(undefined) = NaN
// Boolean(0) // false
// Boolean('0') // true
// Boolean('') //false
// Boolean(' ') //true


// 이건 그냥 외우는 수 밖에 없음
// String Number Boolean을 잘 구분

// 연산자
// + - * / % 
// 여기서 퍼센트는 나머지 값을 구할 때 쓰임
// 홀수 : X % 2 = 1
// 짝수 : Y % 2 = 0
// 어떤 값이 들어와도 5를 넘기면 안돼
// X % 5 = 0 ~ 4 사이의 값만 반환
// 거듭제곱
// const num = 2**3 // 8

// let num = 10;
// num = num + 5;
// 위를 줄이면
// num +=5; // 동일 한 값을 출력
// 증가 연산자, 감소 연산자
// let num = 10;
// let result = ++num; // 11을 출력

// 비교 연산자, 조건문
// < > <= >= ==(같은가) !=(같지 않다) =(이건 할당)
// !=의 반환형은 항상 boolean형
// == 은 동등 연산자
// const a = 1;
// const b = '1';
// console.log( a == b) // True를 반환함 === 는 3개를 넣으면 타입까지 비교해줌
// 어떤 버그를 만들어 낼지 모르니 ===를 추천함

// if(age > 19){
//     console.log('환영합니다.');
// }
//     else if(age === 19) {
//         console.log('수능 잘치세요.')
// }   else {
//     console.log('안녕히 가세요.');
// }

// 이 코드는 True일때 중괄호 안의 코드가 실행됨 False일때는 else가 실행

// 논리 연산자
// or and not
// or는 첫 조건이 만족하는 순간 정지함
// and는 첫 false를 발견하는 즉시 평가를 멈춤
// 성능 최적화에 도움이 되도록 순서를 배치
// || (OR) # shift + 역슬레쉬
// && (AND)
// ! (NOT)

// const name = "Mike";
// const age = 30;

// if(name ==='Tom' || age > 19){
//     console.log('통과');
// }

// if(name ==='Mike' && age > 19){
//     console.log('통과');
// } else {
//     console.log('돌아가.')
// }

// NOT
// 나이를 입력받아 성인이 아니면 돌아가
// const age = prompt('나이가..?');
// const isAdult = age > 19;

// if(!isAdult){
//     console.log('돌아가..')
// }

// 비교 연산자에도 우선순위가 있음 and가 or보다 높음

// const gender ='F';
// const name = 'Jane';
// const isAdult = true;

// // 이 코드는 의도한 바와 달리 우선순위가 적용되어 True가 나옴
// if(gender === 'M' && name === 'Mike' || isAdult){
//     console.log('통과')
// } else {
//     console.log('돌아가.')
// }

// 반복문 loop
// for (let i = 0; i < 10; i++){ //초기값   //조건    //코드 실행 후 작업
//     // 실행할 코드
// }
// 초기값을 지정하고 조건이 트루이면 코드를 실행하고 다음 작업을 반복

// for문
//for (초기세팅 ; 조건 ; 코드 실행 후 작업){ 실행할 코드 }
// for (let i = 0 ; i < 100 ; i++){
//     console.log(i+1)
// }

// while문
// let i = 0;
// while (i<10){
//     // 코드
//     i++;
// }

// let i = 0;
// while(i<10){
//     console.log(i);
//     i++
// }

// do while문 while문에서 조건문만 아래로 내린 것 (적어도 1번은 실행 후 조건을 확인하는게 큰 차이임)
// let i =0;

// do{
//     // 코드
//     i++;
// } while(i<10)

// break
// 조건을 만족할 때까지 실행
// while(true){ 
//     let answer = confirm('계속 할까요?');
//     if(!answer){
//         break;
//     }
// }

//continue 짝수만 
// for (let i = 0; i < 10; i++){
//     if(i%2){ // 2로 나눴을때 나머지가 1이면 if문을 통과함
//         continue;
//     }
//     console.log(i)
// }
// 최초의 0을 2로 나누면 나머지가 0이기 떄문에 컨티뉴문을 통과하지 못하고 로그를 찍음 / 1을 2로 나누면 나누기가 1이기 때문에 컨티뉴 문을 만나게 됨
// Boolean(0) = false이기 때문
// for (let i = 0; i < 10; i++){
//     if(i%2){ 
//         continue;
//     }
//     console.log(i)
// }
// 명확한 횟수가 정해져있다면 for문 그렇지 않다면 while문 나머지는 잘 사용하지 않음

// switch(평가){
//     case A :
//         // A일때 코드
//     case B :
//         // B일때 코드
//     ...
// }
// 스위치문은 이프문과 거의 동일

// let fruit = prompt('무슨 과일을 사고 싶나요?');

// switch(fruit){
//     case '사과' :
//         console.log('100원 입니다.')
//         break;
//     case '바나나' :
//         console.log('200원 입니다.')
//         break;
//     case '키위' :
//     case '수박' :
//         console.log('300원 입니다.')
//         break;
//     default :
//         console.log('그런 과일은 없습니다.')
// }
// break를 넣지 않으면 최초 만족하는 조건 이후의 값을 모두 반환

// 함수(function)
// 브라우져가 가지고 있는 내장함수
// 함수 / 함수명 / 매개변수(name) / 실행코드

// function sayHello(name){
//     console.log('Hello, ${name}');
// }

// sayHello('ola');
// 이거 왜 안되지?;

// function showError(){
//     console.log('에러가 발생했습니다. 다시 시도해주세요.');
// }

// showError();

// function sayHello(name){
//     const msg = 'Hello, ${name}';
//     console.log(msg);
// }

// sayHello('Mike');
// 이건 크롬 콘솔창에서도 안되니 안되는걸로..

// function sayHello(name){
//     let msg = 'Hello';
//     if(name){
//         msg += ', ' + name; 
//     }
//     console.log(msg);
// }

// sayHello('Mike'); // 이건 되고
// 함수 안에서만 사용하는 변수를 지역 변수라고 하는데, 함수 밖에서는 사용이 불가 / 밖으로 꺼내주면 쓸 수 있음
// 어디서나 호출 가능한 함수를 전역 변수라고 함 / 전역변수와 지역변수는 서로 영향을 받지 않음
// += 동일한 값을 출력

// function sayHello(name){
//     let msg = 'Hello';
//     if(name){
//         msg += ',  + ${name}';
//     }
//     console.log(msg);
// }

// sayHello('Mike'); // 이걸 인식을 못하넹

// or
// function sayHello(name){
//     let newName = name || 'friend';
//     let msg = 'Hello, ' + name
//     console.log(msg)
// }

// sayHello();
// sayHello('Jane');
// // 이름이 비어있으면 'freind'에서 true값이 적용됨

// 디폴트값 설정
// function sayHello(name = 'friend'){
//     let msg = 'Hello, ' + name
//     console.log(msg)
// }
// sayHello();
// sayHello('Jane');

// return 으로 값 반환
// function add(num1, num2){
//     return num1 + num2
// }

// const result = add(2, 3);
// console.log(result)

// 팁 : 한번에 한 작업에 집중 / 읽기 쉽고 어떤 동작인지 알 수 있게 네이밍
// showError // 에러를 보여줌
// getName // 이름을 얻어옴
// createUserData // 유저데이터 생성
// checkLogin // 로그인 여부 체크

// 함수 선언문 vs 함수 표현식
// 함수 선언문 : 어디서든 호출가능 / 자바스크립트 내부 알고리즘때문임, 호이스팅(hoisting) 실행전 선언된 함수를 모두 위로 끌어올림
// 함수 표현식 : 인터프리터 방식 / 순서대로 읽어 내려가고 값을 반환함
// 장, 단점 : 함수 선언문을 사용하는게 더 자유롭게 사용 가능

// let sayHello = function(){
//     console.log('Hello');
// }
// sayHello('Maria');

// 화살표 함수(arrow function)

// // 일반적인 함수 표현식
// let add = function(num1, num2){
//     return num1 + num2;
// }

// // 화살표 함수 
// led add = (num1, num2) =>{
//     return num1 + num2;
// }
// // 코드가 한줄이니 이렇게도 변경 가능 / 소괄호로 변경 및 리턴 삭제
// led add = (num1, num2) =>(
//     num1 + num2;
// )
// // 한줄로 변경시 괄호도 삭제 가능
// let add = (num1, num2) => num1 + num2;

// let showError = () => {
//     console.log('error');
// }

// showError()

// let sayHello = (name) =>{
//     const msg = 'Hello, ' + name;
//     console.log(msg)
// }

// sayHello('gura');

// 화살표 함수는 es6 이후부터 활발하게 사용중이기 때문에 확실히 알고 있어야함

// 객체(object)
// Superman
// name : clark
// age : 33

// 이것이 객체 / 객체는 키와 벨류로 이루어지고 각 프로퍼티는 쉼표로 구분됨 / 마지막 쉼표는 없어도 되지만 있는게 수정 삭제 이동 시 용의함
// const superman = {
//     name : 'clark',
//     age : 33,
// }

// Object - 접근, 추가, 삭제
// 접근 / 점이나 대괄호를 이용
// superman.name // 'clark'
// superman['age'] // 33

// 추가 / 추가도 점이나 대괄호를 이용
// superman.gender = 'male';
// superman['hairColor'] = 'black';

// 삭제 / 삭제는 딜리트를 이용
// delete superman.hairColor;

// 프로퍼티 존재 여부 확인
// superman.birthDay;
// // undefined
// 'birthDay' in superman;
// //false

// for in문 사용
// for(let key in superman){
//     console.log(key)
//     console.log(superman[key])
// }

// const superman = {
//     name : 'clark',
//     age : 30,
// }
// console.log(superman.name);
// console.log(superman['name']);
// console.log(superman);
// superman.hairColor = 'black';
// superman['hobby'] = 'football';
// console.log(superman);
// delete superman.age;
// console.log(superman);


// function makeObject(name, age){
//     return {
//         name : name,
//         age : age,
//         hobby : 'football'
//     }
// }

// const Mike = makeObject('Mike', 30);
// console.log(Mike)

// 축약형 객체
// function makeObject(name, age) {
//     return {
//         name,
//         age,
//         hobby: 'football'
//     };
// }
// const Mike = makeObject('Mike', 30);
// console.log(Mike);

// console.log('age' in Mike);

// 객체 in
// function isAdult(user){
//     if(user.age < 20){
//         return false;
//     }
//     return true;
// }

// const Mike = {
//     name : 'Mike',
//     age : 30
// }

// const Jane = {
//     name: 'jane'
// };

// console.log(isAdult(Mike))
// console.log(isAdult(Jane))
// 유저의 에이지가 없으면 언디파인이라서 항상 false를 반환하기 때문에 jane은 트루값을 반환하게됨

// function isAdult(user) {
//     if (!('age' in user) || user.age < 20) {
//         return false;
//     }
//     return true;
// }

// const Mike = {
//     name: "Mike",
//     age: 30,
// }

// const Jane = {
//     name: "Jane",
// }

// console.log(isAdult(Jane))
// console.log(isAdult(Mike))

// 이렇게 변경


// 객체 for ... in
// const Mike = {
//     name: "Mike",
//     age: 30
// };

// for(key in Mike){
//     console.log(Mike[key])
// }
// Mike['name'], Mike['age'] 이런 순으로 회전

// 객체 method / this
// 객체 프로퍼티로 할당 된 함수를 메소드라고 함
// 화살표 함수는 일반 함수와는 달리 자신만의 this를 가지지 않음 superman.name == this.name

// let boy = {
//     name: "Mike",
//     showName: function() {
//         console.log(this.name) // 메소드에서는 객체명을 직접 쓰는 것 보다 this를 활용하는게 좋음
//     }
// };

// boy.showName();
// let man = boy;
// man.name = "Tom"

// console.log(boy.name)
// console.log(boy)
// let man = boy;
// boy = null;

// man.showName();

// 배열(Array) : 순서가 있는 리스트
// 순서(index) : 리스트에서 0부터 시작하는 순서
// 배열의 길이(length)
// push() : 배열 끝에 추가
// pop() : 배열 끝 요소 제거
// unshift : 배열 앞에 추가
// shift : 배열 앞에 제거
// Push, unshift는 배열에 한번에 여러개를 추가할 수 있음

// for문
// let days = ['월', '화', '수'];

// for(let index = 0; index < days.length; index++){  // 초기세팅, 조건, 실행 후 코드 ,중간에는 조건 만족시 실행 코드
//     console.log(days[index])
// } // index는 0부터 시작, 인덱스가 배열의 렝쓰/ 즉 3보다 작다면 코드를 실행, 인덱스를 1 증가시켜줌

// for... of문
// let days = ['월', '화', '수'];

// for(let day of days){
//     console.log(day)
// } // 객체를 순회하는 for in과 혼동 주의

// array
let days = ['mon', 'tue', 'wed']

days.push("thu");
days[1] = '화요일';
console.log(days)

// for(let index=0; index < days.length; index++){
//     console.log(days[index]);
// }

// for(let day of days){
//     console.log(day);
// }
