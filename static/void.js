function usercheck() {
    var mail = document.getElementById("email").value;
    axios.post('/generateotp', {
            "email": mail,
        })
        .then(res => {
            if (res['data']['result'] == 'Success')
                alert("otp send to " + mail)
            else
                alert(res['data']['result']);
        });
}

document.getElementById("otpgen").addEventListener("click", usercheck);