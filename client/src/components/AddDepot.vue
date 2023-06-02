<template>

    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Input data</h1>
                <hr><br><br>
                <alert :message=message v-if="showMessage"></alert>
                <br><br>

                <form @submit.prevent="submitForm" v-on:submit="handleAddSubmit">
                    <span>Depot Name</span><br>
                    <input 
                        v-model="depot_name"
                        type="text"
                        placeholder="Enter depot name" 
                    /><br>
                    <span>Number</span><br>
                    <input 
                        v-model="depot_number"
                        type="number"
                        placeholder="Enter depot number" 
                    /><br>
                    <span>In use</span><br>
                    <label>Yes</label>
                    <input type="radio" v-model="in_use" v-bind:value="true">
                    <label>No</label>                    
                    <input type="radio" v-model="in_use" v-bind:value="false">
                    <br>
                    <input 
                        class="submit" 
                        type="submit" 
                        value="Submit"
                    >
                </form>

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
        depot_name: "",
        depot_number: "",
        in_use: "",
        depots: [],
        message: '',
        showMessage: false,
      };
    },
    components: {
        alert: Alert,
    },
    methods: {
        addDepot(payload) {
            const path = 'http://localhost:5001/depots';
            axios.post(path, payload)
            .then(() => {
                this.message = 'Depot added!';
                this.showMessage = true;
            })
            .catch((error) => {
                console.log(error);
            });
        },
        handleAddSubmit() {
            const payload = {
                depot_name: this.depot_name,
                depot_number: this.depot_number,
                in_use: this.in_use
            };
            this.addDepot(payload);
        },
    },
  };
</script>

<style>
  form {
    padding: 10px;
    border: 2px solid black;
    border-radius: 5px;
  }

  input {
    padding: 4px 8px;
    margin: 4px;
  }

  span {
    font-size: 18px;
    margin: 4px;
    font-weight: 500;
  }

  .submit {
    font-size: 15px;
    color: #fff;
    background: #222;
    padding: 6px 12px;
    border: none;
    margin-top: 8px;
    cursor: pointer;
    border-radius: 5px;
  }

</style>
