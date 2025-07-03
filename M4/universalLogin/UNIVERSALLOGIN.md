# Sistema de Autenticación Universal Multicliente con OAuth2 y Control de Acceso

## 1. Objetivo General

Diseñar e implementar una **arquitectura de autenticación universal** capaz de gestionar el inicio de sesión de múltiples aplicaciones cliente (multi-dominio) utilizando distintos proveedores OAuth2 (GitHub, Google, LinkedIn, etc.), centralizando la lógica de autenticación, autorización, gestión de sesiones y emisión de tokens JWT seguros.

## 2. Motivación

En proyectos donde múltiples dominios necesitan autenticación federada, mantener lógica duplicada en cada uno genera riesgos y altos costos. Este sistema permite:

- Centralizar la gestión de usuarios, roles y sesiones
- Unificar la seguridad mediante JWT firmados
- Delegar la autenticación a proveedores externos confiables
- Facilitar el mantenimiento y escalabilidad

## 3. Arquitectura General

### Componentes

| Componente                | Función                                                                |
| ------------------------- | ---------------------------------------------------------------------- |
| **UniversalLoginService** | Backend centralizado que maneja autenticación, OAuth2 y emisión de JWT |
| **Frontend Cliente**      | Aplicación que delega el login al servicio central                     |
| **OAuth2 Provider**       | Proveedor externo (GitHub, Google, LinkedIn, Azure B2C, etc.)          |
| **DB Centralizada**       | Usuarios, sesiones, permisos, relaciones cliente ↔ proveedor           |

## 4. Flujo de Autenticación

### Paso a Paso:

1. Usuario accede a una aplicación cliente (`paginaX.com`)
2. El frontend redirige al endpoint:
   `https://auth.empresa.com/login?client=paginaX.com`
3. El **UniversalLoginService** identifica el cliente y su proveedor OAuth2
4. Se redirige al proveedor correspondiente (GitHub, Google, LinkedIn)
5. El proveedor autentica al usuario y retorna un **authorization code**
6. El servicio intercambia el código por un `access_token`
7. Se consulta el perfil del usuario (email, nombre, etc.)
8. Se registra la sesión en la base de datos
9. Se emite un JWT firmado (RSA) con los claims:

   - `sub`: ID del usuario
   - `aud`: dominio (`paginaX.com`)
   - `roles`: roles asociados al cliente
   - `permissions`: permisos derivados

10. El frontend recibe el token y lo utiliza en sus llamadas protegidas

## 5. Modelo de Datos

### Tabla `clients`

| id  | domain      | provider | client_id | client_secret | redirect_uri       |
| --- | ----------- | -------- | --------- | ------------- | ------------------ |
| 1   | pagina1.com | github   | abc123    | \*\*\*\*      | /callback/github   |
| 2   | pagina2.com | google   | def456    | \*\*\*\*      | /callback/google   |
| 3   | pagina3.com | linkedin | xyz789    | \*\*\*\*      | /callback/linkedin |

### Tabla `users`

Contiene los usuarios autenticados, asociados a sus clientes.

### Tabla `sessions`

Para tracking de sesiones activas y revocación manual.

### Tabla `roles_permissions`

Para autorización basada en dominio (multi-tenant).

## 6. Seguridad

| Mecanismo         | Descripción                                              |
| ----------------- | -------------------------------------------------------- |
| JWT firmado       | Algoritmo RSA256. Public key expuesta en `/public-key`   |
| Expiración tokens | Configurable por dominio (ej: 15 min + refresh opcional) |
| Revocación        | Implementación de listas negras o UUID por sesión        |
| CORS estricto     | Solo orígenes permitidos por dominio                     |
| CSRF protection   | Solo en formularios si se usa flujo híbrido              |
| Logs de auditoría | Por login, sesión, error de token o acceso no autorizado |

## 7. Ventajas

- Centralización de seguridad y control de acceso
- Escalabilidad para nuevos dominios con solo registrar configuración
- Cumplimiento con estándares como OAuth2, OIDC y JWT
- Facilidad de integración con Azure AD B2C, Auth0 u otros IdPs
- Backend desacoplado del frontend

## 8. Stack Tecnológico Recomendado

| Componente      | Tecnología sugerida                  |
| --------------- | ------------------------------------ |
| Backend Auth    | FastAPI o Django Rest Framework      |
| Base de datos   | PostgreSQL                           |
| JWT Management  | `pyjwt`, `Authlib`, `cryptography`   |
| OAuth2 Client   | `Authlib` / `social-auth-app-django` |
| Frontend        | Cualquier stack (React, Vue, etc.)   |
| Infraestructura | Docker, Nginx, HTTPS, API Gateway    |

## 9. Extensiones Futuras

- **Single Logout Cross-Client**
- **Gestión visual de usuarios/roles**
- **Notificaciones o auditoría en tiempo real**
- **ML para detección de sesiones anómalas**
- **Integración con Azure AD B2C / Okta / Keycloak**

## 10. Conclusión

Este diseño propone una solución profesional, escalable y segura para gestionar múltiples clientes y proveedores de identidad en un solo punto de control.
Es perfectamente viable en entornos corporativos, con proyección a SaaS, B2B y B2C.
