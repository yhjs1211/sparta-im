function load_visitBook() {
    fetch("http://localhost:5001/board/list")
        .then((res) => res.json())
        .then((data) => {
            let arr = data["visitBook_li"];
            let visit_num = 1;
            arr.forEach((v) => {
                $("#visitBook-card").append(render_visitBook_template(v));
            });
        });
}

function render_visitBook_template(data) {
    return  `<div class="card position-relative" style="width: 18rem;">
                <h3>${data["nickname"]}</h3><hr/>
                <div class="card-body">
                    <p class="card-text">${data["comment"]}</p>
                </div>
                <button type="button" data-bs-toggle="modal" data-bs-target="#deleteModal" class="btn-close position-absolute top-0 end-0" aria-label="Close"></button>
            </div>`;
}