<script>

import { Line, mixins } from "vue-chartjs";

const { reactiveProp } = mixins;

export default {
  extends: Line,
  mixins: [reactiveProp],
  name: "LineChart",
  props: {
    chartData: {
      type: Object,
      required: false
    }
  },
  data() {
    return {
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }
          ],
          xAxes: [
            {
              gridLines: {
                display: false
              }
            }
          ]
        },
        legend: {
          display: true,
          position: "top",
          labels: {
            fontSize: 15
          }
        },
        responsive: true,
        maintainAspectRatio: false,
        fill: false
      }
    };
  },
  mounted() {
    this.renderChart(this.chartData, this.options);
  }
};

</script>