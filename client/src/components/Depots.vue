<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Depots</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>

        <router-link :to="{ path: '/forms' }">
          <button 
            type="button" 
            class="btn btn-success btn-sm">
            Add Depot
          </button>
        </router-link>
        
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Depot name</th>
              <th scope="col">Depot number</th>
              <th scope="col">In use?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(depot, index) in depots" :key="index">
              <td>{{ depot.depot_name }}</td>
              <td>{{ depot.depot_number }}</td>
              <td>
                <span v-if="depot.in_use">Yes</span>
                <span v-else>No</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
    
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      depots: [],
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getDepots() {
      const path = 'http://localhost:5001/depots';
      axios.get(path)
          .then((res) => {
            this.depots = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
  },
  created() {
      this.getDepots();
  },
};
</script>
