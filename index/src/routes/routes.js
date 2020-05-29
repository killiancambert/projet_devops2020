import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Details from '../components/Details'

Vue.use(Router);

const router = new Router({
  mode: "hash"
  routes: [{
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/details/:id",
    name: "details",
    component: Details
  }]
});

export default router;