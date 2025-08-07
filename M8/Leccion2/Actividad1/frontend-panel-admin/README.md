# 🔐 Panel Administrativo - Laboratorio de Seguridad Web

Este proyecto simula un panel administrativo web construido en **Vue.js 3 con Vite** como parte de un laboratorio de análisis de vulnerabilidades y aplicación de técnicas de mitigación. El propósito es reproducir fallas comunes en aplicaciones web modernas, analizar su impacto y proponer soluciones seguras.

---

## 🎯 Objetivo del laboratorio

- Simular vulnerabilidades frecuentes como:
  - Cross-Site Scripting (XSS)
  - CSRF (Cross-Site Request Forgery)
  - Falta de autenticación/autorización
  - Uso de librerías vulnerables
- Implementar una interfaz funcional que permita ejecutar pruebas manuales o automatizadas.
- Servir como base para realizar auditorías, aplicar parches y comparar versiones inseguras vs. seguras.

---

## 📁 Estructura del proyecto

```

frontend-panel-admin/
├── index.html
├── package.json
├── vite.config.js
└── src/
├── main.js
├── App.vue
├── assets/
├── views/
│   └── AdminPanel.vue
└── components/
├── UserSearch.vue         # Simula XSS (Caso 1)
├── ExportButton.vue       # Exportación sin login (Caso 2)
└── UserList.vue           # CSRF en eliminación (Caso 4)

````

---

## ⚙️ Instalación

Requiere Node.js v16+.

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/frontend-panel-admin.git
cd frontend-panel-admin

# Instalar dependencias
npm install
````

---

## ▶️ Ejecutar la app

```bash
npm run dev
```

Abre en tu navegador:

```
http://localhost:5173
```

---

## 🧪 Casos de vulnerabilidad simulados

| Caso | Componente         | Vulnerabilidad simulada                                      |
| ---- | ------------------ | ------------------------------------------------------------ |
| 1    | `UserSearch.vue`   | **XSS** reflejado al insertar scripts en el input            |
| 2    | `ExportButton.vue` | **Endpoint sin autenticación ni control de acceso**          |
| 3    | `main.js`          | Uso de **jQuery obsoleto** vulnerable                        |
| 4    | `UserList.vue`     | **CSRF** en eliminación de usuario sin token de verificación |

---

## 🛠️ Reproducir XSS

1. En el campo de búsqueda, escribe:

```html
<script>alert('XSS')</script>
```

2. Haz clic en "Buscar". El script será ejecutado si no está mitigado.

---

## 🧩 Futuras mejoras

* Añadir backend en FastAPI para interacción real con base de datos.
* Implementar modo "seguro" con todas las vulnerabilidades mitigadas.
* Agregar login y control de roles (RBAC).
* Integrar sistema de tokens CSRF y CSP (Content Security Policy).

---

## 🔐 Advertencia

Este sistema contiene **vulnerabilidades intencionadas** y está diseñado únicamente para fines **educativos y de auditoría controlada**. **No debe utilizarse en producción ni estar expuesto públicamente.**
