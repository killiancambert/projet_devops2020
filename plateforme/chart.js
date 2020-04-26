//environnement
const json_url = '/automate/json/paramunite_1_25-04-2020.json';
async function getData() {
  const response = await fetch(json_url);
  const data = await response.json();

  // xlabels.push(data.pH);

  console.log(data);

  document.getElementById('ph').textContent = data.pH;
}

const pH_min = 1;
const pH_max = 14

const x_pH = [];
for (let i = 0; i < 61; i++) {
  result = Math.random() * (pH_max-pH_min) + pH_min;
  x_pH.push(result);
}

const ylabels = [];
for (let i = 0; i <= 60; i++) {
  ylabels.push(i);
}

async function chartIt() {
  await getData();
  var ctx = document.getElementById('chart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: ylabels,
          datasets: [{
              label: 'pH',
              data: x_pH,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)'
              ],
              borderWidth: 1
          }, {
              label: 'K',
              data: [ 12, 9, 10, 5, 4],
              backgroundColor: [
                  'rgba(252, 207, 3, 0.2)'
              ],
              borderColor: [
                  'rgba(252, 207, 3, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
        scales: {
            xAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Temps en min'
              }
            }]
        }
    }
  });
}

chartIt();

