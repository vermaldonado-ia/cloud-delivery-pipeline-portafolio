# 🚀 Despliegue Básico en AWS Amplify

Este documento describe el proceso de despliegue de una aplicación estática utilizando AWS Amplify, conectando un repositorio GitHub y habilitando despliegue automático en cada cambio sobre la rama principal.

---

## 🎯 Objetivo

Implementar un despliegue continuo simple que permita:

* Publicar una aplicación en la nube
* Automatizar el despliegue mediante integración con GitHub
* Obtener una URL productiva accesible
* Validar el flujo de entrega end-to-end

---

## 🧩 Arquitectura

Repositorio GitHub
↓
AWS Amplify
↓
Build y Deploy automático
↓
Hosting web con URL pública

---

## ⚙️ Pasos realizados

### 1. Creación de la aplicación

Se creó una nueva aplicación en AWS Amplify seleccionando la opción de hosting para aplicación web.

### 2. Conexión con repositorio

Se conectó el repositorio GitHub del proyecto `cloud-delivery-pipeline-portafolio`.

### 3. Selección de rama

Se configuró la rama `main` como rama de producción.

### 4. Configuración de compilación

Para este proyecto estático se utilizó la siguiente configuración:

* Framework: Ninguno
* Build command: vacío
* Output directory: `/`

Esto permite desplegar directamente el archivo `index.html` ubicado en la raíz del repositorio.

### 5. Despliegue

AWS Amplify ejecutó automáticamente:

* clonación del repositorio
* preparación del entorno
* publicación de la aplicación
* generación de URL pública

---

## 🌐 URL de producción

👉 https://main.d28beryienq64n.amplifyapp.com

---

## 🔄 Despliegue automático

Cada vez que se realiza un cambio en la rama `main`, AWS Amplify detecta el nuevo commit y ejecuta automáticamente un nuevo despliegue.

Flujo implementado:

Push a `main`
↓
Amplify detecta cambio
↓
Nuevo build
↓
Nuevo deploy
↓
Actualización del sitio en producción

---

## ✅ Resultado obtenido

* Aplicación publicada en AWS
* URL pública accesible
* Integración activa con GitHub
* Despliegue automático funcionando
* Sitio actualizado tras cambios en `index.html`

---

## 🧠 Valor técnico y profesional

Este despliegue demuestra:

* uso de servicios cloud en AWS
* integración de repositorio con plataforma de hosting
* automatización del proceso de publicación
* implementación práctica de Continuous Deployment
* visibilidad end-to-end desde cambio técnico hasta resultado productivo

---

## 📌 Conclusión

Se implementó un despliegue básico pero real en AWS Amplify, suficiente para demostrar un flujo moderno de entrega continua sobre una aplicación estática. Este enfoque permite exponer el proyecto en un entorno productivo y mantener actualizaciones automáticas a partir de cambios en el repositorio.
