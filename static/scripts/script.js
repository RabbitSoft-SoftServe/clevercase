document.addEventListener("DOMContentLoaded", function() {
    var buttonCat = document.querySelector('.button_cat');
    var formContainer = document.querySelector('.form-container');

    buttonCat.addEventListener('click', function() {
        if (formContainer.style.display === 'none' || formContainer.style.display === '') {
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

function playSound() {
    var sound = document.getElementById("mySound");
    sound.currentTime = 0;
    sound.play();
}
function setTextColor(block) {
    const bgColor = window.getComputedStyle(block).backgroundColor;
    const rgb = bgColor.match(/\d+/g);
    const yiq = ((rgb[0]*299)+(rgb[1]*587)+(rgb[2]*114))/1000;
    block.style.color = (yiq >= 128) ? 'black' : 'white';
}
setTextColor(document.getElementById('colorful-object'));

