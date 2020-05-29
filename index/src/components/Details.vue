<template>
  <div class="container">
    <div class="selection">
      <v-select v-model="defaultData" :options="options" @input="request()" :clearable="false"></v-select>
    </div>
    <line-chart :styles="chartStyle" :chart-data="datacollection" />
    <div class="button">
      <button @click="createPdf()">Exporter au format PDF</button>
    </div>
  </div>
</template>

<style scoped>

.container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  justify-content: center;
  text-align: end;
  min-height: 95vh;
}
.selection {
  cursor: pointer;
  width: 300px;
  align-self: flex-end;
  margin-bottom: 15px;
  margin-right: 50px;
}
.button {
  margin-top: 50px;
  align-self: center;
}
button {
  background: #0084B8;
  box-shadow: 0px 10px 20px rgba(0, 132, 184, 0.3);
  font-size: 20px;
  font-weight: bold;
  color: white;
  border: 0 none;
  border-radius: 20px;
  cursor: pointer;
  padding: 20px;
}

</style>

<script>

import "vue-select/dist/vue-select.css";

import LineChart from '../components/Chart'
import jsPdf from 'jspdf'

export default {
  components: {
    LineChart
  },
  data() {
    return {
      id: this.$route.params.id,
      defaultData: "Mesure pH",
      options: [
        "Température cuve",
        "Température extérieure",
        "Poids du lait en cuve",
        "Poids du produit fini réalisé",
        "Mesure pH",
        "Concentration de NaCl",
        "Niveau bactérien salmonelle",
        "Niveau bactérien E-coli",
        "Niveau bactérien Listéria"
      ],
      datacollection: null,
      label: [],
      automates: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      automate: [],
      response: []
    }
  },
  created() {
    this.axios
      .get("http://localhost:5000:unites?id=" + this.id)
      .then(response => {
        this.response = response.data;
        this.request();
      })
      .catch(error => {
        console.log(error);
      })
  },
  methods: {
    request() {
      let dataPosition = this.options.indexOf(this.defaultData)
      this.automate = []
      for (let j = 1; j < this.automates.length + 1; j++) {
        this.label = []
        let label = []
        let positionArray = []
        let timeArray = []
        let timeVariable = 61
        for (let k = 1; k < this.response.length; k++) {
          if (this.response[k][1] == j) {
            positionArray.push(this.response[k])
          }
        }
        for (let l = 0; l < positionArray.length; l++) {
          timeArray.push(positionArray[l][dataPosition + 3])
        }
        if (timeArray.length < timeVariable) {
          timeVariable = timeArray.length
        }
        for (let i  = 0; i < timeVariable; i++) {
          label.push(i)
          this.label.push(i)
        }
        this.automate.push(
          timeArray.slice(timeArray.length - timeVariable, timeArray.length)
        )
      }
      this.fillData()
    },
    fillData() {
      this.datacollection = {
        labels: this.label,
        datasets: [
          {
            label: "Automate 1",
            backgroundColor: "#0D3B66",
            data: this.automate[0]
          },
          {
            label: "Automate 2",
            backgroundColor: "#FFBA08",
            data: this.automate[1],
            hidden: true
          },
          {
            label: "Automate 3",
            backgroundColor: "#A30000",
            data: this.automate[2],
            hidden: true
          },
          {
            label: "Automate 4",
            backgroundColor: "#009B72",
            data: this.automate[3],
            hidden: true
          },
          {
            label: "Automate 5",
            backgroundColor: "#F95738",
            data: this.automate[4],
            hidden: true
          },
          {
            label: "Automate 6",
            backgroundColor: "#30323D",
            data: this.automate[5],
            hidden: true
          },
          {
            label: "Automate 7",
            backgroundColor: "#0F5727",
            data: this.automate[6],
            hidden: true
          },
          {
            label: "Automate 8",
            backgroundColor: "#009DDC",
            data: this.automate[7],
            hidden: true
          },
          {
            label: "Automate 9",
            backgroundColor: "#A2D729",
            data: this.automate[8],
            hidden: true
          },
          {
            label: "Automate 10",
            backgroundColor: "#94386E",
            data: this.automate[9],
            hidden: true
          }
        ]
      }
    },
    createPdf() {
      let chart = document.getElementById("line-chart");
      let canvas = document.getElementById("line-chart").toDataURL("image/png");
      let doc = new jsPdf("l", "mm", [chart.width - 350, chart.height - 100]);
      doc.addImage(canvas, "PNG", 10, 10);
      doc.save("graphique.pdf");
    }
  },
  computed: {
    chartStyle() {
      return {
        height: "500px"
      }
    }
  }
}
</script>
