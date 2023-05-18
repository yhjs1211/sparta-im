function update_member() {
    let val = 'input[name="updateInfo"]:checked';
    let chk = document.querySelectorAll(val);

    let formData = new FormData();

    let formData_has_id = false;
    chk.forEach((t) => {
        let v = $("#" + t["id"] + "-value").val();
        // 고유 ID 1차 검증
        if (t["id"] == "_id") {
            // ID 값을 가지고 있으니 true
            formData_has_id = true;
            // ID의 값이 유효한지 검증
            formData_has_id = correct_id(v);
        }
        formData.append(t["id"], v);
    });

    if (formData_has_id == false) {
        alert("유효한 ID값을 입력해주세요.");
        return window.location.reload();
    }

    fetch("http://localhost:5001/members", { method: "POST", body: formData })
        .then((res) => res.json())
        .then((data) => {
            alert(data["msg"]);
            window.location.reload();
        });
}

function correct_id(id) {
    let correct = true;

    if (id.length < 24) {
        correct = false;
    }

    return correct;
}