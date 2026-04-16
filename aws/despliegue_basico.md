# 🚀 Despliegue Básico en AWS Amplify

Este documento describe la implementación de un despliegue continuo utilizando AWS Amplify, integrando el repositorio GitHub del proyecto dentro de un flujo CI/CD completo.

---

## 🎯 Objetivo

Implementar un despliegue continuo que permita:

* Publicar una aplicación en la nube
* Automatizar el despliegue mediante integración con GitHub
* Obtener una URL productiva accesible
* Validar el flujo de entrega end-to-end

---

## 📐 Rol dentro del pipeline

Este despliegue corresponde a la etapa final del flujo CI/CD implementado en el repositorio:

Pull Request / Push
↓
CI Pipeline (GitHub Actions)
↓
Code Quality (Quality Gate)
↓
Merge a `main`
↓
CD Automático (AWS Amplify)

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

Se creó una nueva aplicación en AWS Amplify utilizando el servicio de hosting para aplicaciones web estáticas.

---

### 2. Conexión con repositorio

Se conectó el repositorio GitHub del proyecto:

`cloud-delivery-pipeline-portafolio`

---

### 3. Selección de rama

Se configuró la rama `main` como rama de producción.

---

### 4. Configuración de compilación

Para este proyecto estático se utilizó la siguiente configuración:

* Framework: None
* Build command: vacío
* Output directory: `/`

Esto permite desplegar directamente el archivo `index.html` ubicado en la raíz del repositorio.

---

### 5. Despliegue

AWS Amplify ejecuta automáticamente:

* Clonación del repositorio
* Preparación del entorno
* Publicación de la aplicación
* Generación de URL pública

---

## 🌐 URL de producción

👉 https://main.d28beryienq64n.amplifyapp.com

---

## 🔄 Despliegue automático

Cada vez que se realiza un cambio en la rama `main`, AWS Amplify ejecuta automáticamente un nuevo despliegue.

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
* Actualización continua tras cambios en el repositorio

---

## 🧠 Valor técnico y profesional

Este despliegue demuestra:

* Uso de servicios cloud en AWS
* Integración de repositorio con plataforma de hosting
* Automatización del proceso de publicación
* Implementación real de Continuous Deployment
* Integración dentro de un pipeline CI/CD completo

---

## 🚀 Conclusión

Se implementó un despliegue real en AWS Amplify como etapa final del pipeline CI/CD, permitiendo exponer el proyecto en un entorno productivo y mantener actualizaciones automáticas tras cada cambio en la rama principal.
