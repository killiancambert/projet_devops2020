//environnement
const json_url = '/automate/json/paramunite_4_25-04-2020-18-54-50.json';
async function getData() {
  const response = await fetch(json_url);
  const data = await response.json();

  xlabels.push(data.pH);

  console.log(data);

  document.getElementById('ph').textContent = data.pH;
}

const xlabels = [];

async function chartIt() {
  await getData();
  var ctx = document.getElementById('chart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
          datasets: [{
              label: 'pH',
              data: xlabels,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)'
              ],
              borderWidth: 1
          }]
      }
  });
}

chartIt();

