<template>
  <div>
    <template>
    <b-navbar class="is-info">
        <template #brand>
            <b-navbar-item style="font-weight:600" tag="router-link" :to="{ path: '/' }">
                Cheil
            </b-navbar-item>
        </template>
        <template #start>
            <b-navbar-item href="#">
                Hotels
            </b-navbar-item>
            <b-navbar-item href="#">
                Trends
            </b-navbar-item>
            
        </template>

       
    </b-navbar>
</template>


    <!--<section class="main-content columns">
      <aside class="column is-2 section">
        <p class="menu-label is-hidden-touch">General</p>
        <ul class="menu-list">
          <li v-for="(item, key) of items" :key="key">
            <NuxtLink :to="item.to" exact-active-class="is-active">
              <b-icon :icon="item.icon" /> {{ item.title }}
            </NuxtLink>
          </li>
        </ul>
      </aside>-->

      <div class="container column is-10">
        <Nuxt />
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      items: [
        {
          title: 'Home',
          icon: 'home',
          to: { name: 'index' },
        },
        {
          title: 'Inspire',
          icon: 'lightbulb',
          to: { name: 'inspire' },
        },
      ],
    }
  },
  async mounted() {},
}
</script>
<style>
.container{
  margin:20px 15px
}

</style>
