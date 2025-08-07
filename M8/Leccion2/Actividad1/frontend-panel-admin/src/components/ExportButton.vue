<template>
  <div style="margin-top: 20px;">
    <button @click="exportar">Exportar usuarios (CSV)</button>
    <p v-if="msg">{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('')

async function exportar() {
  try {
    const res = await fetch('http://localhost:8000/admin/users/export')
    const data = await res.text()
    msg.value = 'Exportación exitosa. Datos: ' + data.slice(0, 100) + '...'
  } catch (error) {
    msg.value = 'Error al exportar: ' + error.message
  }
}
</script>
