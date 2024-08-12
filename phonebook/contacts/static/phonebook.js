function modalSwitch() {
  let modal = document.getElementById("modal");
  if (modal.style.display == "none") {
    modal.style.display = "flex";
  } else {
    modal.style.display = "none";
  }
}

function modalReset() {
  let inputs = document.getElementsByClassName("modalInput");
  for (let value of inputs) {
    value.value = "";
  }
}


function mainReset() {
  let inputs = document.getElementsByClassName("mainInput");
  for (let value of inputs) {
    value.value = "";
  }
}

function contactModalOpen(id) {
  let contactModal = document.getElementById(id);
  if (contactModal.style.display == "none") {
    contactModal.style.display = "flex";
  }
  let searchedContact = document.getElementsByClassName("ser_contacts_content" + id);
  let pOfContactModal = searchedContact[0].children[0].innerHTML;
  let modal = document.getElementById(id);
  let modalInput = modal.getElementsByTagName("input");
  modalInput[1].value = searchedContact[0].children[0].innerHTML.slice(7, (searchedContact[0].children[0].innerHTML.length));
  modalInput[2].value = searchedContact[0].children[1].innerHTML.slice(7, (searchedContact[0].children[1].innerHTML.length));
  modalInput[3].value = searchedContact[0].children[2].innerHTML.slice(7, (searchedContact[0].children[2].innerHTML.length));
  modalInput[4].value = searchedContact[0].children[3].innerHTML.slice(11, (searchedContact[0].children[3].innerHTML.length));
  modalInput[5].value = searchedContact[0].children[4].innerHTML.slice(7, (searchedContact[0].children[4].innerHTML.length));
}

function contactModalClose(id) {
  let contactModal = document.getElementById(id);
  contactModal.style.display = "none";
  }