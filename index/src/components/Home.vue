<template>
  <div class="container">
    <router-link
      class="unit-container"
      ripple
      v-for="(unit, i) in units"
      :key="i + 1"
      v-bind:to="'/details/' + unit"
    >
      <div class="unit">
        <div class="title">
          Unité
        </div>
        <div class="number">
          {{ i + 1 }}
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>

export default {
  name: "Home",
  data() {
    return {
      units: [1, 2, 3, 4, 5]
    };
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.container {
  padding: 50px 100px;
  text-decoration: none;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.unit-container {
  text-decoration: none;
  color: #1D2020;
  margin: 50px 100px;
  width: 300px;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 30px;
  background-color: white;
  border: 5px solid #1D2020;
  transition: 0.3s ease-in;
}

.unit-container:hover {
  color: white;
  background-color: #1D2020;
  cursor: pointer;
}

.unit {
  display: flex;
  align-items: center;
  border-radius: 10px;
  padding: 5px;
  font-size: 30px;
  font-weight: bold;
}

.title {
  padding: 0 10px;
}

.number {
  padding: 5px 10px;
}

</style>