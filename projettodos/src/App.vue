<script setup>
import TodoItem from './components/TodoItem.vue'
</script>

<script>
let data = {
  todos: [
    { id:1, text: 'Courses', checked: false },
    { id:2, text: 'Apprendre REST', checked: false },
    { id:3, text: 'Faire un projet magnifique', checked: false }
  ],
  title: 'Ma liste de tâches',
  nouvelleTache: ''
};

export default {
  data() {
    return data;
  },

  methods: {
    ajouterTache() {
      this.todos.push({ text: this.nouvelleTache, checked: false})
      console.log(this.todos)
      this.nouvelleTache = ''
    },
    removeTask(task) {
      this.todos = this.todos.filter(todo => todo.id !== task.id)
    },
    updateTask(task) {
      this.todos = this.todos.map(todo => {
        if (todo.id === task.id) {
          return task
        }
        return todo
      })
    }
  }
}
</script>

<template>
  <div>
    <h1>{{ title }}</h1>
    <ul>
      <TodoItem v-for="task in todos" :key="task.id" :todo="task" @remove="removeTask"></TodoItem>
    </ul>
    <hr/>
    <em>Ajouter une tâche</em>
    <input v-model="nouvelleTache" type="text"/>
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


