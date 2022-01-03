
function login() {
    
    let user = document.getElementById('user').value;
    let password = document.getElementById('password').value
    var formdata = new FormData();
    formdata.append("user", user);
    formdata.append("password", password);

    var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/login", requestOptions)
        .then(
            response => {
                if (response.redirected) {
                    $('#meuModal').modal('show');
                    setTimeout(() => {
                        window.location.href = response.url
                        $('#meuModal').modal('toggle');
                    },
                        2000);

                } else {
                    response.text().then(result => JSON.parse(result)).then(result => {
                        alert(result.message)
                    })
                }

            }
        )




}