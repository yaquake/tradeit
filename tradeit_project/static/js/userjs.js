function CheckPassword(inputtxt) {
    const passw = "^(?=.*[a-z])(?=.*[0-9])(?=.{8,})";
    if (inputtxt.value.match(passw)) {
        document.getElementById("passwordDescription").innerHTML = "<small>Good password</small>";
    }
    else {
        document.getElementById("passwordDescription").innerHTML = "<small><p style='color: red;'>" +
            "Minimum eight characters, at least one letter and one number</p></small>";
    }
}


function comparePassword(p1, p2)
{
    if (p1.value === p2.value) {
        document.getElementById("passwordMatching").innerHTML = "<small>Passwords match</small>";
    }
    else  if (p2.value === "") {
        document.getElementById("passwordMatching").innerHTML = "<small>Null password</small>";
    }
    else {
        document.getElementById("passwordMatching").innerHTML = "<small><p style='color: red;'>Different passwords</p></small></small>";
    }


}

function emailValidation(email) {
    const emailName = /\S+@\S+\.\S+/;
    if (email.value.match(emailName)) {
        document.getElementById("emailValid").innerHTML = "<small>Good e-mail address</small>";
    }
    else {
        document.getElementById("emailValid").innerHTML = "<small><p style='color: red;'>Bad e-mail address</p></small>";
    }
}



function preview_image(event)
{
 let reader = new FileReader();
 reader.onload = function()
 {
  let output = document.getElementById('output_image');
  output.src = reader.result;
 }
 reader.readAsDataURL(event.target.files[0]);
}
