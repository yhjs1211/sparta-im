function save_member() {
    let name = $("#name").val();
    let position = $("#position").val();
    let s_i = $("#self_introduce").val();
    let mbti = $("#mbti").val();
    let comment = $("#comment").val();
    let blog = $("#blog").val();
    let img = $("#image").val();

    let formData = new FormData();
    formData.append("name_give", name);
    formData.append("po_give", position);
    formData.append("s_i_give", s_i);
    formData.append("mbti_give", mbti);
    formData.append("comment_give", comment);
    formData.append("blog_give", blog);
    formData.append("img_give", img);

    fetch("/im", { method: "POST", body: formData })
        .then((res) => res.json())
        .then((data) => {
            alert(data["msg"]);
            window.location.reload();
        });
}
