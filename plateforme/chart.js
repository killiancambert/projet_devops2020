const json_url = '/automate/json/paramunite_test.json';

// var mysql = require('mysql');

// var con = mysql.createConnection({
//   host: "localhost",
//   user: "root",
//   password: "root",
//   database: "testdevops"
// });

// con.connect(function(err) {
//   if (err) throw err;
//   con.query("SELECT * FROM automate ", function (err, result, fields) {
//     if (err) throw err;
//     console.log(result);
//   });
// });


async function getData() {
  const response = await fetch(json_url);
  const data = await response.json();

  var i, j, k, x = "";

  for (i in data.unites) {
    for (j in data.unites[i].automates) {
      // console.log(data.unites[i].automates[j].infos);
      for (k in data.unites[i].automates[j].infos) {

        // Data pH 
        datapH = data.unites[i].automates[j].infos[k].pH;
        x_datapH.push(datapH);

        // Data température cuve
        dataTempCuve = data.unites[i].automates[j].infos[k].temperature_cuve;
        x_dataTempCuve.push(dataTempCuve);

        // Data température exterieur
        dataTempExt = data.unites[i].automates[j].infos[k].temperature_exterieur;
        x_dataTempExt.push(dataTempExt);

        // Data poids lait cuve
        dataPoidsLait = data.unites[i].automates[j].infos[k].poids_lait_cuve;
        x_dataPoidsLait.push(dataPoidsLait);

        // Data produit fini
        dataProdFini = data.unites[i].automates[j].infos[k].poids_produit_fini;
        x_dataProdFini.push(dataProdFini);

        // Data K
        dataK = data.unites[i].automates[j].infos[k].K;
        x_dataK.push(dataK);

        // Data NaCl
        dataNaCl = data.unites[i].automates[j].infos[k].NaCl;
        x_dataNaCl.push(dataNaCl);

        // Data salmonelle
        dataSal = data.unites[i].automates[j].infos[k].salmonelle;
        x_dataSal.push(dataSal);

        // Data Ecoli
        dataEco = data.unites[i].automates[j].infos[k].Ecoli;
        x_dataEco.push(dataEco);

        // Data listeria
        dataLis = data.unites[i].automates[j].infos[k].listeria;
        x_dataLis.push(dataLis);
      }
    }
  }  
}

// const pH_min = 1;
// const pH_max = 14;

// const x_pH = [];
// for (let i = 0; i < 61; i++) {
//   result = Math.random() * (pH_max-pH_min) + pH_min;
//   x_pH.push(result);
// }

const x_datapH = [];
const x_dataTempCuve = [];
const x_dataTempExt = [];
const x_dataPoidsLait = [];
const x_dataProdFini = [];
const x_dataK = [];
const x_dataNaCl = [];
const x_dataSal = [];
const x_dataEco = [];
const x_dataLis = [];

// const ylabels = [];
// for (let i = 0; i <= 60; i++) {
//   ylabels.push(i);
// }

async function chartIt() {
  await getData();
  var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
          // labels: ylabels,
          datasets: [{
              label: 'pH',
              data: x_datapH,
              fill: false,
              backgroundColor: 'rgba(255, 99, 132)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1
          }, {
              label: 'K+ en mg/L',
              data: x_dataK,
              fill: false,
              backgroundColor: 'rgba(252, 207, 3)',
              borderColor: 'rgba(252, 207, 3, 1)',
              borderWidth: 1
          }, {
              label: 'Température Cuve en °C',
              data: x_dataTempCuve,
              fill: false,
              backgroundColor: 'rgba(66, 135, 245)',
              borderColor: 'rgba(66, 135, 245, 1)',
              borderWidth: 1
          }, {
              label: 'Température Extérieur en °C',
              data: x_dataTempExt,
              fill: false,
              backgroundColor: 'rgba(66, 245, 209)',
              borderColor: 'rgba(66, 245, 209, 1)',
              borderWidth: 1
          }, {
              label: 'Poids Lait Cuve en kg',
              data: x_dataPoidsLait,
              fill: false,
              hidden: true,
              backgroundColor: 'rgba(72, 245, 66)',
              borderColor: 'rgba(72, 245, 66, 1)',
              borderWidth: 1
          }, {    
              label: 'Poids Produit Fini',
              data: x_dataProdFini,
              fill: false,
              backgroundColor: 'rgba(37, 125, 34)',
              borderColor: 'rgba(37, 125, 34, 1)',
              borderWidth: 1
          }, {
              label: 'NaCl en g/L',
              data: x_dataNaCl,
              fill: false,
              backgroundColor: 'rgba(128, 64, 184)',
              borderColor: 'rgba(128, 64, 184, 1)',
              borderWidth: 1
          }, {
              label: 'Salmonelle en ppm',
              data: x_dataSal,
              fill: false,
              backgroundColor: 'rgba(184, 64, 176)',
              borderColor: 'rgba(184, 64, 176, 1)',
              borderWidth: 1
          }, {
              label: 'Ecoli en ppm',
              data: x_dataEco,
              fill: false,
              backgroundColor: 'rgba(0, 26, 255)',
              borderColor: 'rgba(0, 26, 255, 1)',
              borderWidth: 1
          }, {
              label: 'Listeria en ppm',
              data: x_dataLis,
              fill: false,
              backgroundColor: 'rgba(255, 0, 0)',
              borderColor: 'rgba(255, 0, 0, 1)',
              borderWidth: 1
          }]
      },
      options: {
        scales: {
            xAxes: [{
              ticks: {
                beginAtZero: true
              }
            }],
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
        }
    }
  });
}

chartIt();

