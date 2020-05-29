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
  margin-top: 20px;
  margin-right: 50px;
}
button {
  width: 200px;
  background: #000;
  font-weight: bold;
  color: white;
  border: 0 none;
  border-radius: 1px;
  cursor: pointer;
  padding: 10px 10px;
}

</style>

<script>

import "vue-select/dist/vue-select.css";

export default {
  name: "details"
}
</script>
