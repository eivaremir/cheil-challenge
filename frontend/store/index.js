// store/index.js
// import axios from 'axios'

export const state = () => ({
  hotels: [],
})
export const mutations = {
  updateHotels: (state, payload) => {
    state.hotels = payload
  },
}
export const actions = {
  async getHotelsData({ state, commit }) {
    /* if (state.hotels.length) return

    await axios
      .post(process.env.API_HOST + '/api/v1/hotels')
      .then((response) => {
        commit('updateHotels', response.data)
      })
      .catch((error) => {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }
        } else {
          this.errors.push('Algo salio mal, por favor intente de nuevo')
        }
      }) */
  },
}
