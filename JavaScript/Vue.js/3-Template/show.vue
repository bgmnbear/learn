<script src="https://cdn.jsdelivr.net/npm/vue" xmlns:v-bind="http://www.w3.org/1999/xhtml"></script>

<div id="example">
    <span v-once>这个将不会改变: {{ msg }}</span>
    <p>Using mustaches: {{ rawHtml }}</p>
    <p>Using v-html directive: <span v-html="rawHtml"></span></p>
</div>

<div v-bind:id="dynamicId"></div>
<button v-bind:disabled="isButtonDisabled">Button</button>

<div v-bind:id="'list-' + id"></div>

<p v-if="seen">现在你看到我了</p>

<a v-bind:href="url">...</a>
<!-- 缩写 -->
<a :href="url">...</a>

<a v-on:click="doSomething">...</a>
<!-- 缩写 -->
<a @click="doSomething">...</a>

<form v-on:submit.prevent="onSubmit">...</form>

<script src="E:\learn\JavaScript\Vue.js\3-Template\template.js"></script>
