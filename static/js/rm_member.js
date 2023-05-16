function remove_member() {
    let name = $("#rm_name").val();
    // let position = $("#rm_position").val();
    // let s_i = $("#rm_self_introduce").val();
    // let mbti = $("#rm_mbti").val();
    // let comment = $("#rm_comment").val();
    // let blog = $("#rm_blog").val();
    // let img = $("#rm_image").val();

    let formData = new FormData();
    formData.append("name_give", name);
    // formData.append("po_give", position);
    // formData.append("s_i_give", s_i);
    // formData.append("mbti_give", mbti);
    // formData.append("comment_give", comment);
    // formData.append("blog_give", blog);
    // formData.append("img_give", img);

    fetch("/im", { method: "DELETE", body: formData })
        .then((res) => res.json())
        .then((data) => {
            alert(data["msg"]);
            window.location.reload();
        });
}
