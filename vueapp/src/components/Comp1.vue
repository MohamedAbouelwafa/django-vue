<template>
  <div class="hello">
    <h1>Vue Comp 1 - Yay</h1>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';

  @Component({
    components: {
    },
  })
  export default class Comp1 extends Vue {}
  </script>
