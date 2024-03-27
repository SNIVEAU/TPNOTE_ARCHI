<script setup>
import { ref } from 'vue';
import TodoItem from './components/TodoItem.vue';


</script>

<script>
const data = ref([]);

const fetchTask = async () => {
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    try {
        const response = await fetch(`http://localhost:5000/quiz/api/v1.0/tasks?_limit=20`, options);
        const json = await response.json();
        data.value = json;
        console.log(data.value); // Ajout du console.log pour afficher les données initialisées
    } catch (err) {
        console.log('Error getting documents', err);
        data.value = [];
    }
};
export default {
    data() {
        return {
            title: "Liste de tâches",
            nouvelleTache: ''
        };
    },

    async created() {
        await fetchTask();
    },

    methods: {
        ajouterTache() {
            this.data.push({ text: this.nouvelleTache, checked: false });
            console.log(this.data);
            this.nouvelleTache = '';
        },
        removeTask(task) {
            this.data = this.data.filter(todo => todo.id !== task.id);
        },
        updateTask(task) {
            this.data = this.data.map(todo => {
                if (todo.id === task.id) {
                    return task;
                }
                return todo;
            });
        }
    }
};
</script>

<template>
    <div>
        <h1>{{ title }}</h1>
        <ul>
            <TodoItem v-for="task in data" :key="task.id" :todo="task" @remove="removeTask"></TodoItem>
        </ul>
        <hr />
        <em>Ajouter une tâche</em>
        <input v-model="nouvelleTache" type="text" />
        <button @click="ajouterTache">Ajouter</button>
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
