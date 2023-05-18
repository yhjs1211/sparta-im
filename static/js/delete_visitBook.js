function delete_visitBook() {
    let password = $("#delete-visitBook").val();

    let formData = new FormData();
    formData.append("password", password);

    fetch("http://localhost:5001/board", { method: "DELETE", body: formData })
        .then((res) => res.json())
        .then((data) => {
            alert(data["msg"]);
            window.location.reload();
        });
}
