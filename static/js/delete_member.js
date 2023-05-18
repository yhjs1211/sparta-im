function delete_member() {
    let _id = $("#personal_id").val();

    formData = new FormData();
    formData.append("_id", _id);

    fetch("http://localhost:5001/members", { method: "POST", body: formData })
        .then((res) => res.json())
        .then((data) => {
            alert(data["msg"]);
            window.location.reload();
        });
}
