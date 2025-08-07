<template>
  <div style="margin-top: 40px;">
    <h2 style="color: #fff; background-color: #1e3a8a; padding: 10px; border-radius: 6px;">
      Lista de usuarios
    </h2>

    <table v-if="users.length" border="1" cellpadding="10" style="width: 100%; margin-top: 20px; background-color: #111; color: #fff; border-collapse: collapse;">
      <thead>
        <tr style="background-color: #1e3a8a;">
          <th>ID</th>
          <th>Nombre</th>
          <th>Email</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
          <td>
            <button @click="eliminar(user.id)" style="background-color: red; color: white; border: none; padding: 5px 10px; border-radius: 4px;">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else style="color: gray;">No hay usuarios cargados.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const users = ref([])

const cargarUsuarios = async () => {
  const res = await fetch('http://localhost:8000/users')
  users.value = await res.json()
}

const eliminar = async (id) => {
  await fetch('http://localhost:8000/delete-user', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id }),
  })
  users.value = users.value.filter(user => user.id !== id)
}

onMounted(() => {
  cargarUsuarios()
})
</script>
