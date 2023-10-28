document.getElementById("bg-color").addEventListener("input", function() {
    // Встановлюємо колір для елементу з id="colorful-object" на основі вибраного кольору
    document.getElementById("colorful-object").style.backgroundColor = this.value;
});


const submitButton = document.querySelector('.submit-btn');
submitButton.addEventListener('click', () => {
  const form = document.querySelector('.form-container');
  form.style.display = 'none';
});

const closeButton = document.querySelector('.close-button');
closeButton.addEventListener('click', () => {
  const form = document.querySelector('.form-container');
  form.style.display = 'none';
});


const showModalBtn = document.getElementById('showModal');
const modal = document.getElementById('modal');
const saveChangesBtn = document.getElementById('saveChanges');
const categoriesGrid = document.getElementById('categoriesGrid');
let categoriesCount = 0;

showModalBtn.addEventListener('click', () => {
    modal.classList.remove('hidden');
});

saveChangesBtn.addEventListener('click', () => {
    const categoryName = document.getElementById('category-name').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const limit = document.getElementById('limit').value;
    const spent = document.getElementById('spent').value;

    const categoryCard = document.createElement('div');
    categoryCard.innerHTML = `
        <p>Name: ${categoryName}</p>
        <p>Period: ${startDate} - ${endDate}</p>
        <p>Limit: ${limit}</p>
        <p>Currently Spent: ${spent}</p>
    `;
    categoryCard.style.cssText = 'display: inline-block; width: calc(33% - 10px); margin: 5px; border: 1px solid black; padding: 10px;';
    categoriesGrid.appendChild(categoryCard);

    categoriesCount++;
    if (categoriesCount % 3 === 0) {
        const breakLine = document.createElement('br');
        categoriesGrid.appendChild(breakLine);
    }

    modal.classList.add('hidden');
});