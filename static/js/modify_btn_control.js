// 페이지 수정(정확히는 회원 정보 수정) 버튼을 생성하는 함수
function show_modify_btn() {
    // 같은 클래스 이름을 갖는 elment들을 찾을 때 아래 함수를 사용한다.
    // 이 코드에서는 클래스가 control_info인 element들을 찾는다.
    let btns = document.getElementsByClassName('control_info');
    // console.log(btns);
    // 버튼 안보이면 보이게 하기
    if ($('.control_info').css('display') == 'none') {
        for (let i = 0; i < btns.length; i++) {
            // console.log(btns[i]);
            // console.log(i);
            // btns.show();
            btns[i].style.display = "block";
        }
        $('#modify_info').text("수정 취소하기");
    } // 버튼 보이면 안보이게 하기
    else {
        for (let i = 0; i < btns.length; i++) {
            btns[i].style.display = "none";
            // btns.hide();
        }
        $('#modify_info').text("페이지 수정");
    }
}
