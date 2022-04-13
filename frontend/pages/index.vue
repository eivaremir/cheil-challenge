<template>
  <section class="container">
    <b-field>
      <b-switch v-model="filters" :value="true"> Show Filters </b-switch>
    </b-field>

    <div class="columns main-container">
      <aside v-if="filters" class="column filters">
        <h1 class="is-size-3">Filters</h1>
        <div class="filter">
          <span>Category</span>
          <b-field>
            <b-slider v-model="category" :min="1" :max="5" :step="1" ticks>
              <template v-for="val in [1, 2, 3, 4, 5]">
                <b-slider-tick
                  :value="val"
                  :key="'s-tick'.concat(val.toString())"
                  >{{ val }}</b-slider-tick
                >
              </template>
            </b-slider>
          </b-field>
        </div>
        <div class="filter">
          <span>Scoring</span>
          <b-field>
            <b-slider v-model="scoring" :min="1" :max="5" :step="1" ticks>
              <template v-for="val in [1, 2, 3, 4, 5]">
                <b-slider-tick
                  :value="val"
                  :key="'s-tick'.concat(val.toString())"
                  >{{ val }}</b-slider-tick
                >
              </template>
            </b-slider>
          </b-field>
        </div>
        <div class="filter">
          <b-field>
            <b-switch v-model="order" :value="true">
              price {{ order ? 'ascending' : 'descending' }}
            </b-switch>
          </b-field>
        </div>
        <div class="filter-btns">
          <b-button class="filter-btn" type="is-primary" @click="filter"
            >Search</b-button
          >
          <b-button
            class="filter-btn"
            v-if="filtered"
            type="is-danger"
            @click="filtered = false"
            >Clear filters</b-button
          >
        </div>
      </aside>
      <div class="column">
        <h1 class="is-size-3">
          Hotels {{ filtered ? `(${hotels.length}) results found` : '' }}
        </h1>
        <div class="is-mobile hotels-container">
          <div v-for="hotel in hotels" v-bind:key="hotel.hotel_id" class="card">
            <div class="card-image">
              <figure class="image is-4by3">
                <img :src="hotel.thumbnail" alt="Placeholder image" />
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4">{{ hotel.name }}</p>
                  <div class="hotel-scores-container">
                    <p class="is-6">
                      <b-icon
                        icon="star"
                        v-for="star in parseInt(hotel.category)"
                        :key="star + '-' + hotel.hotel_id"
                        class="star"
                      />
                    </p>
                    <p class="is-6">{{ hotel.score }}</p>
                  </div>
                </div>
              </div>

              <div class="content">
                {{ hotel.description }}
                <p>$ {{ hotel.price_per_night }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// import { mapState } from 'vuex'
import axios from 'axios'
// import Card from '~/components/Card'

export default {
  name: 'IndexPage',
  components: {
    // Card,
  },
  data() {
    return {
      hotels: [],
      order: true,
      category: '',
      scoring: [2, 4],
      filters: true,
      filtered: false,
    }
  },
  computed: {
    // ...mapState(['hotels']),
  },
  methods: {
    async setAllHotels() {
      await axios
        .get(process.env.API_HOST + '/api/v1/hotels/')
        .then((response) => {
          // commit('updateHotels', response.data)
          console.log(response.data)
          this.hotels = response.data
        })
    },
    async filter() {
      this.filtered = true
      await axios
        .post(process.env.API_HOST + '/api/v1/hotels/search', {
          category: this.category.toString(),
          score_from: this.scoring[0],
          score_to: this.scoring[1],
          order: !this.order ? 'desc' : 'asc',
        })
        .then((response) => {
          // commit('updateHotels', response.data)
          console.log(response.data)
          this.hotels = response.data
        })
    },
  },
  async mounted() {
    await this.setAllHotels()
  },

  watch: {
    filtered(isFilter) {
      if (!isFilter) {
        this.setAllHotels()
      }
    },
  },
}
</script>
<style>
.filters {
  gap: 15px;
  display: flex;
  flex-direction: column;
}
.main-container {
  display: flex;
  gap: 15px;
  justify-content: space-between;
}
.aside {
  border: 1px solid black;
}
.hotels-container {
  flex-wrap: wrap;
  display: flex;
}

.card {
  margin: 10px;
  width: 45%;
  max-width: 350px;
  min-width: 250px;
}
.card:hover {
  box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.2);
}
.hotel-scores-container {
  display: flex;
  justify-content: space-between;
}
.star {
  color: #d8d82f;
}
.content p {
  margin: 9px 0 0 0;
  font-weight: 600;
}
.b-slider-tick-label {
  top: calc(0.625rem * 0.5 + 5px) !important;
}
.filter-btns {
  display: flex;
  gap: 5px;
  margin-top: 20px;
  flex-wrap: wrap;
}
.filter-btn {
  flex-grow: 1;
}
@media screen and (min-width: 768px) {
  .columns {
    flex-direction: row;
  }
  .filters {
    width: 30%;
    flex: none;
  }
}
@media screen and (max-width: 768px) {
  .columns {
    flex-direction: column;
  }
  .filters {
    width: 100%;
  }
}
</style>
