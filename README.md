# Proyecto Redes

## Cómo levantar el ambiente
1. Instalar [VirtualBox](https://virtualbox.org) y [ISO Ubuntu 24.04 LTS](https://ubuntu.com/download/desktop)
2. Clonar este repo: `git clone https://github.com/JheffreyUrbano/proyecto-redes.git`
3. Ir a la carpeta: `cd proyecto-rei-2026`


# Endpoints API – Sistema de Requisiciones

Base URL:

http://papadasoftware.com/api/

---

## 1. Requisiciones

### Obtener todas las requisiciones
GET /api/requisiciones/

### Obtener una requisición específica
GET /api/requisiciones/{requino}/

### Crear una nueva requisición
POST /api/requisiciones/

### Actualizar requisición (completa)
PUT /api/requisiciones/{requino}/

### Actualizar requisición (parcial)
PATCH /api/requisiciones/{requino}/

### Eliminar requisición
DELETE /api/requisiciones/{requino}/

---

## 2. Detalles de Requisición

### Obtener todos los detalles
GET /api/detalles/

### Obtener detalles por requisición
GET /api/detalles/?requino={requino}

### Crear detalle (si aplica desde API directa)
POST /api/detalles/

### Eliminar detalle (PK compuesta)
DELETE /api/detalles/eliminar/

Body:
{
  "item": 1,
  "codproducto": "MP-MAD-001",
  "requino": "000001"
}

---

## 3. Logs de Auditoría (log_requisicion)

### Obtener logs por requisición
GET /api/logs/?requino={requino}

### Crear log
POST /api/logs/

Body:
{
  "requisicion": "000001",
  "accion": "CREACION",
  "descripcion": "Se creó la requisición"
}

---

## 4. Productos

### Obtener productos
GET /api/productos/

### Obtener producto específico
GET /api/productos/{codproducto}/

### Crear producto
POST /api/productos/

### Actualizar producto
PUT /api/productos/{codproducto}/

### Eliminar producto
DELETE /api/productos/{codproducto}/

---

## 5. Usuarios

### Login de usuario
POST /api/usuarios/login/

Body:
{
  "usuario": "admin",
  "password": "1234"
}

---

## 6. Notificaciones (Correos)

### Enviar correo
POST /api/notificaciones/enviar/

Body:
{
  "destinatario": "correo@gmail.com",
  "asunto": "Asunto",
  "mensaje": "Contenido del mensaje"
}

---

## 7. Endpoint de prueba (solo desarrollo)

### Eliminar detalle desde navegador (NO PRODUCCIÓN)
GET /api/detalles/eliminar-test/?item={item}&codproducto={codproducto}&requino={requino}

Ejemplo:
GET /api/detalles/eliminar-test/?item=1&codproducto=MP-MAD-001&requino=000001

---

## Notas importantes

- Todos los endpoints están bajo el prefijo `/api/`
- El backend se encuentra en 192.168.100.3:8000 (oculto detrás de Nginx)
- El acceso público se realiza a través de:
  http://papadasoftware.com

---

## Convenciones utilizadas

- `requino`: identificador de requisición
- `codproducto`: identificador del producto
- `item`: número de ítem dentro de la requisición

---

## Seguridad

- No se permite DELETE en logs de auditoría
- El backend no está expuesto directamente
- Nginx actúa como proxy inverso
