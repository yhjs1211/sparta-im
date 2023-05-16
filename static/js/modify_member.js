function modify_member() {
    let name = $("#mod_name").val();
    let position = $("#mod_position").val();
    let s_i = $("#mod_self_introduce").val();
    let mbti = $("#mod_mbti").val();
    let comment = $("#mod_comment").val();
    let blog = $("#mod_blog").val();
    let img = $("#mod_image").val();

    let formData = new FormData();
    formData.append("name_give", name);
    formData.append("po_give", position);
    formData.append("s_i_give", s_i);
    formData.append("mbti_give", mbti);
    formData.append("comment_give", comment);
    formData.append("blog_give", blog);
    formData.append("img_give", img);

    fetch("/im", { method: "PUT", body: formData })
        .then((res) => res.json())
        .then((data) => {
            alert(data["msg"]);
            window.location.reload();
        });
}
