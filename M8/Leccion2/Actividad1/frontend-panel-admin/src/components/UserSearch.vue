<template>
  <div style="margin-top: 20px;">
    <h2>Buscar usuario</h2>
    <input v-model="query" placeholder="Ingresa nombre o ID" />
    <button @click="buscar">Buscar</button>

    <div v-if="resultado">
      <p>{{ resultado }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const query = ref('')
const resultado = ref('')

async function buscar() {
  try {
    const res = await fetch(`http://localhost:8000/search?q=${encodeURIComponent(query.value)}`)
    const text = await res.text()

    // Vue escapa automáticamente al usar {{ }} → XSS mitigado
    resultado.value = text
  } catch (err) {
    resultado.value = 'Error al conectar con el backend.'
  }
}
</script>

<style scoped>
input {
  margin-right: 10px;
  padding: 5px;
}
button {
  padding: 6px 10px;
  background-color: #1e3a8a;
  color: white;
  border: none;
  border-radius: 4px;
}
</style>
