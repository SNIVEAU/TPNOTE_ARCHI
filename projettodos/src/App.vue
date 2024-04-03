<script setup>
import TodoItem from './components/TodoItem.vue';
import Questionnaire from './components/Questionnaire.vue';

import { ref, onMounted } from 'vue';

const data = ref([]);

const fetchTask = async () => {
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    try {
        const response = await fetch(`http://127.0.0.1:5000/quiz/api/v2.0/questionnaires`, options);
        const json = await response.json();
        data.value = json.questionnaires; 
    } catch (err) {
        console.log('Error getting documents', err);
        data.value = []; 
    }
};

onMounted(fetchTask); 
</script>

<template>
  <div>
      <Questionnaire v-for="questionnaire in data" :key="questionnaire.id" :questionnaire="questionnaire"></Questionnaire>
    <hr />
    <!-- <em>Ajouter une tâche</em>
    <input v-model="nouvelleTache" type="text" />
    <button @click="ajouterTache">Ajouter</button> -->
  </div>
</template>



<style scoped>
.logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
}
.logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
}

ul {
    list-style-type: none;
    padding: 0;
}

em {
    font-size: 1.5em;
    margin-right: 1em;
}
</style>
