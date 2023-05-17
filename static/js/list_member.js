function list_member() {
    fetch("/im")
        .then((res) => res.json())
        .then((data) => {
            $("#member_intro").empty();
            // console.log(data);
            let rows = data["result"];
            
            rows.forEach((element) => {
                let obj_id = element["_id"];
                let name = element["name"];
                let position = element["position"];
                let self_intro = element["self_introduce"];
                let mbti = element["mbti"];
                let comment = element["comment"];
                let blog = element["blog"];
                let image = element["image"];
                console.log(obj_id);

                let render = `
                    <div class="flip-box">
                        <a href="${blog}">
                            <div class="flip">
                                <div class="front">
                                    <div class="col">
                                        <div class="card">
                                            <img src="${image}"
                                                class="card-img-top" height="300px" />
                                            <div class="card-body" style="height: 200px;">
                                                <h2 id="name" style="color:black">${name}</h2>
                                                <h5 id="position" style="color:black">${position}</h5>
                                                <h6 id="comment" style="color:red">${comment}</h6>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="back">
                                    <div class="col">
                                        <h3 style="color:blueviolet">${mbti}</h3>
                                        <h2 style="color:black">${self_intro}</h2>
                                    </div>
                                </div>
                            </div>
                        </a>
                        <div class="control_info">
                            <button type="button" data-post_id="${obj_id}" class="btn btn-outline-secondary" id="modify_info"
                                onclick="load_info(this.dataset.post_id)">수정</button>
                            <button type="button" data-post_id="${obj_id}" class="btn btn-outline-danger" id="delete_info"
                                onclick="remove_member(this.dataset.post_id)">삭제</button>
                        </div>
                    </div>
                `;
                $("#member_intro").append(render);
            });
        });
}