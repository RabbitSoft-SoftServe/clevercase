const ctx = document.getElementById('canvas1').getContext('2d');

const weekArray = ['Monday', 'Tuesday', 'Wednesday', 'Thursday' , 'Friday', 'Saturday', 'Sunday']

const monthArray = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'Septermber', 'October', 'November', 'December'];

const greenToBlueArray = ['#15740d', '#1b7b1f', '#208131', '#269743', '#2ca255',
'#33a768', '#3ab07a', '#41b88d', '#4ac09f', '#56c8b4', '#6cd1c9', '#8fdbee']

const chart = new Chart (ctx, {
    type: 'bar',
    data: {
        datasets: [{
            label: 'Monthly Spendings',
            data: [200, 400, 150, 170, 230, 400, 650, 320, 530, 320, 220, 140],
            backgroundColor: greenToBlueArray
          }],
          labels: monthArray
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    suggestedMin: 0
                }
            }]
        }
    }
})