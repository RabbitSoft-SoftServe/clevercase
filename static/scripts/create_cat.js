const colorSaveElement = document.getElementById("color_save");
if (colorSaveElement) {
    colorSaveElement.addEventListener("input", function() {
        // ...
    });
}
const submitButton = document.querySelector('.submit-btn');
submitButton.addEventListener('click', (event) => {
    event.preventDefault();
  const form = document.querySelector('.form-container');
  console.log(form);
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
    const categoryName = document.getElementById('cat_name').value;
    const startDate = document.getElementById('date_of_rent').value;
    const endDate = document.getElementById('due_date').value;
    const limit = document.getElementById('the_limit').value;
    const spent = document.getElementById('currently_spent').value;

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