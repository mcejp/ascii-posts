---
layout: post
render_with_liquid: false
date: 2023-09-28
title: Vue
unlisted: true
---

> Go with Options API if you are not using build tools, or plan to use
> Vue primarily in low-complexity scenarios, e.g. progressive
> enhancement.

### Quickstart with components and no compilation step (v3.x, Composition API)

``` html
<script type="importmap">
{
    "imports": {
    "vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
    }
}
</script>

<script type="module">
import { createApp } from 'vue'

const ExampleComponent = {
  props: {
    msg: String
  },
  template: `
  <h2>{{ msg || 'No props passed yet' }}</h2>
  <p><slot>Default content</slot></p>
  `
}

createApp({
  components: {
      ExampleComponent
  },
}).mount('#app')
</script>

<div id="app">
  <h1>Make me dynamic!</h1>
  <example-component msg="Hello">This is some slot content!</example-component>
</div>
```
