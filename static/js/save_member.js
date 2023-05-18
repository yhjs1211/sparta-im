function save_member() {
    let name = $("#name").val();
    let position = $("#position").val();
    let s_i = $("#self_introduce").val();
    let mbti = $("#mbti").val();
    let comment = $("#comment").val();
    let blog = $("#blog").val();
    let img = $("#image").val();

    let formData = new FormData();
    formData.append("name", name);
    formData.append("position", position);
    formData.append("self_introduce", s_i);
    formData.append("mbti", mbti);
    formData.append("comment", comment);
    formData.append("blog", blog);
    formData.append("image", img);

    fetch("http://localhost:5001/members", { method: "POST", body: formData })
        .then((res) => res.json())
        .then((data) => {
            alert(data["msg"]);
            window.location.reload();
        });
}