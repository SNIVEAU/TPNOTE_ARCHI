
<script>
export default {
  props: {
    question: {
      type: Object,
      required: true
    }
  }
}

</script>
<template>
    <h3>{{question.title}}</h3>
    <div>
        <p>
            {{question.p1}}
        </p>
        <p>
            {{question.p2}}

        </p>
        <p>
            
            {{question.p3}}

        </p>
        <p>
            {{question.p4}}

        </p>
    </div>
</template>