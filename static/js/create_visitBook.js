function create_visitBook() {
    let nickname = $("#nickname").val();
    let comment = $("#comment").val();
    let password = $("#password").val();

    let formData = new FormData();
    formData.append("nickname", nickname);
    formData.append("comment", comment);
    formData.append("password", password);

    fetch("http://localhost:5001/board", { method: "POST", body: formData })
        .then((res) => res.json())
        .then((data) => {
            console.log(data["msg"]);
            alert(data["msg"]);
        });
}
