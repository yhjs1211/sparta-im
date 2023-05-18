function save_member() {
    let name = $("#name").val(); //id가 name인 곳에 input된 값을 가져와 name 변수에 저장한다.
    let position = $("#position").val();
    let s_i = $("#self_introduce").val();
    let mbti = $("#mbti").val();
    let comment = $("#comment").val();
    let blog = $("#blog").val();
    let img = $("#image").val();

    let formData = new FormData();
    formData.append("name_give", name); //formData.append(name, value) : name_give에 name 저장
    formData.append("po_give", position);
    formData.append("s_i_give", s_i);
    formData.append("mbti_give", mbti);
    formData.append("comment_give", comment);
    formData.append("blog_give", blog);
    formData.append("img_give", img);

    fetch("/im", { method: "POST", body: formData }) //웹에서 ("/im") 서버 주소로 요청 부탁
        .then((res) => res.json())                   //요청이 끝나면 then 이것을 해라
        .then((data) => {                            // 해당 fetch의 요청은 입력 값을 서버에 저장해달라
            alert(data["msg"]);                      // 서버에 저장했으면 msg를 띄워라 > app.py Post msg
            window.location.reload(); //새로고침
        });
}
