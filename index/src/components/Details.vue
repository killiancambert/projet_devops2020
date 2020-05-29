<template>
  <div class="container">
    <div class="selection">
      <v-select v-model="defaultData" :options="options" @input="request()" :clearable="false"></v-select>
    </div>
    <line-chart :styles="chartStyle" :chart-data="datacollection" />
    <div class="button">
      <button>
    </div>
  </div>
</template>