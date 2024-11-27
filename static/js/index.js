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

//close button

let closebtn = document.getElementById("cls");

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