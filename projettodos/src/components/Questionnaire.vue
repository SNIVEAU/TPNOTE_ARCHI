<script setup>
import Question from './Question.vue'
</script>
<script>
export default {
  props: {
    questionnaire: {
      type: Object,
      required: true
    }
  }
}
</script>
<template>
    <h2>{{questionnaire.name}}</h2>
    <Question v-for="question in questionnaire.questions" :key="question.id" :question="question"></Question>

</template>