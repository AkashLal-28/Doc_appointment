// form validation

let datepicker = document.getElementById("date-picker");
let form = document.querySelector("form");
let phone = document.querySelector("#mobile");
let username = document.querySelector("#name");

datepicker.addEventListener("change", (e) => {
  let chosenDate = new Date(e.target.value);
  let today = new Date();

  if (chosenDate < today) {
    alert("Please select a future date");
    datepicker.value = "";
  }
});

username.addEventListener("change", function(e){
    let nameinput = e.target.value
    if(nameinput.length < 2 || typeof nameinput !== string){
        alert('Enter a valid name')
        username.value = ""
    }
})
phone.addEventListener("change", function (e) {
  let userPhone = e.target.value;
  if (userPhone.length < 10 || userPhone.length >= 11 ||(userPhone = "") || typeof userPhone !== number) {
    alert("please enter a valid 10 digit phone number");
    phone.value = "";
  }
});

// signup/password validation in signup

let pass1 = documemt.getElementById('password_1')
let pass2 = documemt.getElementById('password_2')
let signupbtn = document.getElementsByClassName('signupbtn')
let usernm = document.querySelectorAll('#username')

usernm.addEventListener('change', function(){
    let enteruser = usernm.value
    if(enteruser.length<2){
      alert('test')
    }
}) 

pass1.addEventListener("change", function(){
  let userpass1 = pass1.value
  if(userpass1.length > 3){
    alert('test')
  }
})

//close button

let closebtn = document.getElementById("closed");

closebtn.addEventListener("click", function () {
  closebtn.style.display = "none";
});



//signup

var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}




