function load_member() {
    fetch("http://localhost:5001/members/list")
        .then((res) => res.json())
        .then((data) => {
            let arr = data["member_li"];

            arr.forEach((m) => {
                $("#member-card").append(render_member_template(m));
            }).catch((error) => console.log(error));
        });
}

function render_member_template(data) {
    return `
        <a href="${data["blog"]}">
            <div class="flip-box">
                <div class="flip">
                    <div class="front">
                        <div class="col">
                            <div class="card">
                            <img
                                src=${data["image"]}
                                class="card-img-top"
                                height="300px"
                            />
                            <div class="card-body" style="height: 200px;">
                                <h1 id="name" style="color:black">${data["name"]}</h1>
                                <h5 id="position" style="color:black">${data["position"]}</h5>
                                <h4 id="comment" style="color:red">${data["comment"]}</h4>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div class="back">
                        <div class="col">
                            <h3 style="color:blueviolet">${data["mbti"]}</h3>
                            <h2 style="color:black">${data["self_introduce"]}</h2>
                        </div>
                    </div>
                </div>
            </div>
        </a>`;
}
