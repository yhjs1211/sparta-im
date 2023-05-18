// 멤버 정보 수정용 modal을 생성하는 함수
// 현재 생각나는 문제점 :
// modal을 수정하고 수정사항이 있어 수정을 하면 괜찮음
// 하지만 수정 완료를 안하고 닫기를 눌러버리면 modal이 남지 않을까 하는 생각은 듦
function render_modify_form(post_id) {
    // id가 modify_form인 element가 있다면 제거
    // 만약 제거를 안하면 render_modify_form() 함수에서 id가 mod_form인 element에 modify_form이 계속 쌓임
    if ($("#modify_form").length)  // 이 부분이 modify_form이 있는지 확인하는 작업이다. 있으면 true, 없으면 false를 나타낸다.
        $("#modify_form").remove();
    let html_form = `
        <div class="modal fade" id="modify_form" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">멤버 정보 수정</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input id="mod_name" class="form-control" type="text" placeholder="이름" />
                        <input id="mod_position" class="form-control" type="text" placeholder="직책" />
                        <input id="mod_mbti" class="form-control" type="text" placeholder="당신의 MBTI는?" />
                        <input id="mod_self_introduce" class="form-control" type="text" placeholder="자기소개를 적어주세요." />
                        <input id="mod_comment" class="form-control" type="text" placeholder="한마디 !" />
                        <input id="mod_blog" class="form-control" type="text" placeholder="블로그 주소" />
                        <input id="mod_image" class="form-control" type="text" placeholder="Image URL을 입력해주세요." />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Close
                        </button>
                        <button data-post_id="${post_id}" onclick="modify_member(this.dataset.post_id)" type="button" class="btn btn-primary">
                            수정하기
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;

    $("#mod_form").append(html_form);
}

function load_info(post_id) {
    // uri의 동적인 생성을 위해 동적인 부분은 변수로 사용
    let uri = "/info/" + post_id;
    
    fetch(uri)
        .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            let rows = data["result"];
            // console.log(rows);
            // 아래 함수를 통해 modal을 새로 랜더링하고 post_id도 같이 넘겨줌
            render_modify_form(post_id);

            // 데이터가 한 세트밖에 없어서 왜 반복문을 쓰나 의아할것임
            // 이게 rows를 콘솔에 출력해보면 배열처럼 0: 데이터 이런 식으로 나와서 이렇게 했음
            // 아마 rows[0]['name'], rows[0]['position'] 이런 식으로 사용해도 될 것이다.
            rows.forEach((element) => {
                $("#mod_name").val(element["name"]);
                $("#mod_position").val(element["position"]);
                $("#mod_self_introduce").val(element["self_introduce"]);
                $("#mod_mbti").val(element["mbti"]);
                $("#mod_comment").val(element["comment"]);
                $("#mod_blog").val(element["blog"]);
                $("#mod_image").val(element["image"]);
            });

            // 입력 폼을 modal이라고 하는데 아래 함수를 실행하면 입력폼이 나타남
            $("#modify_form").modal("show");
        }) // 아래는 에러 발생했을 때 그 내용을 보여주는 함수. 약간 문법적인 부분이 있어 모르면 그냥 넘어가도 무관하다. 나중에 익숙해지면 그때 봐도 됨.
        .catch((err) => {
            console.log(err);
        });
}

function modify_member(post_id) {
    // console.log(post_id);
    // modal 안에 input 태그들의 값들을 읽어옴
    if (confirm("정말로 정보를 삭제하시겠습니까?")) {
        let name = $("#mod_name").val();
        let position = $("#mod_position").val();
        let s_i = $("#mod_self_introduce").val();
        let mbti = $("#mod_mbti").val();
        let comment = $("#mod_comment").val();
        let blog = $("#mod_blog").val();
        let img = $("#mod_image").val();

        let formData = new FormData();

        formData.append("post_id_give", post_id);
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
    else {
        alert("수정 작업이 취소됐습니다.");
    }
}

// 원하는 DB 정보 삭제 요청을 하는 함수
function remove_member(post_id) {
if (confirm("정말로 정보를 삭제하시겠습니까?")) {
        let formData = new FormData();
        formData.append("post_id_give", post_id);

        fetch("/im", { method: "DELETE", body: formData })
            .then((res) => res.json())
            .then((data) => {
                alert(data["msg"]);
                window.location.reload();
            });
    } else {
        alert("삭제를 취소하였습니다.");
    }
}
