document.addEventListener("DOMContentLoaded", function() {
    var buttonCat = document.querySelector('.button_cat');
    var formContainer = document.querySelector('.form-container');

    buttonCat.addEventListener('click', function() {
        if(formContainer.style.display === 'none' || formContainer.style.display === '') {
            formContainer.style.display = 'block';
        } else {
            formContainer.style.display = 'none';
        }
    });
});

const menuButton = document.querySelector('.menu-container')
const openMenu = document.querySelector('.open-menu')

if (menuButton) {
    menuButton.addEventListener('click', function () {
        openMenu.classList.toggle('is-active');
    });
}

const profileButton = document.querySelector('.add-account-container')
const openAddAccount = document.querySelector('.add-account')

if (profileButton) {
    profileButton.addEventListener('click', function () {
        openAddAccount.classList.toggle('is-active');
    });
}
