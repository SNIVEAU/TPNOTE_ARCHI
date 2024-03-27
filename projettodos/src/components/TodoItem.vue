<template>
  <div class="checkbox">
    <label>
        <input type="checkbox" v-model="todo.checked">
        {{ todo.text }}
        <button class="btn btn-danger" @click="suppr">Supprimer</button>
        <button class="btn btn-danger" @click="modif">Modifier</button>
    </label>
  </div>
  </template> 
  
<script>
export default {
  props: {
    todo: Object
  },
  methods: {
    suppr() {
      this.$emit('remove', this.todo);
    },
    updateTextTask() {
      this.$emit('update', this.todo);
    }
  },
  emits: ['remove']
}
</script>

<style scoped>
input {
  margin: 1em;
}

button {
  margin: 1em;
}

button:hover {
  background-color: #d3d3d3;
  color: white;
}

.checkbox {
  margin: 1em;
  padding: 1em;
  border: 1px solid #42b883;
  border-radius: 5px;
  background-color: #f2f2f2;
}

.checkbox:hover {
  background-color: #e6e6e6;
}

</style>