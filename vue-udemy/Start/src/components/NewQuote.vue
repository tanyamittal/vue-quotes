<template>
  <div class="container">
    <div class="row">
      <form>
        <div class="col-sm-8 col-sm-offset-2 col-xs-12 col-md-6 col-md-offset-3 form-group">
          <label for="new">Quote</label>
          <textarea name="new" id="newQuote" cols="30" rows="3" v-model="quote"></textarea>
        </div>
        <div class="col-sm-8 col-sm-offset-2 col-xs-12 col-md-6 col-md-offset-3 form-group">
          <button class="btn btn-primary" @click.prevent="newQuote">Add Quote</button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      quote: ""
    };
  },
  methods: {
    newQuote() {
      this.$emit("quoteAdded", this.quote);
      this.quote = "";
    }
  }
};
</script>
<style scoped>
textarea {
  margin-top: 20px;
}
</style>
