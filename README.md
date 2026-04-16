# 🚀 Cloud Delivery Pipeline Portafolio

![CI](https://img.shields.io/badge/CI-GitHub_Actions-blue)
![Coverage](https://img.shields.io/badge/Coverage-80%25-green)
![CD](https://img.shields.io/badge/CD-AWS_Amplify-orange)

Repositorio que demuestra la implementación de un pipeline DevOps completo, integrando prácticas de Integración Continua (CI), control de calidad (Quality Gate), gestión de Pull Request y despliegue continuo real (CD) en la nube.

---

## 🌐 Producción

👉 URL del sitio desplegado:
https://main.d28beryienq64n.amplifyapp.com

El despliegue continuo se realiza automáticamente en AWS Amplify, generando un entorno accesible públicamente tras cada cambio en la rama principal.

---

## 🎯 Objetivo

Implementar un pipeline que permita:

* Detectar errores de forma temprana (Shift Left)
* Asegurar calidad del código antes del merge
* Validar cobertura de pruebas
* Controlar cambios hacia producción
* Automatizar el despliegue en la nube

---

## ⚙️ Arquitectura del Pipeline

Flujo implementado:

Pull Request / Push
↓
CI Pipeline (GitHub Actions)
↓
Code Quality (Quality Gate: pytest + coverage + flake8)
↓
Merge controlado a main
↓
CD Automático (AWS Amplify - Deploy real)

---

## 🔄 Integración Continua (CI)

El pipeline ejecuta automáticamente:

* Instalación de dependencias
* Configuración de entorno Python
* Ejecución de pruebas con pytest
* Medición de cobertura con pytest-cov
* Análisis de calidad con flake8

Esto permite validar cada cambio antes de integrarlo a la rama principal.

---

## 🛡️ Code Quality - Quality Gate

Se implementa un Quality Gate práctico inspirado en herramientas como SonarQube y Azure DevOps.

### 🔍 Validaciones aplicadas:

* ✔ Tests deben pasar
* ✔ Coverage mínimo: 80%
* ✔ Código sin errores de linting

Si alguna condición falla:

⛔ El pipeline se detiene
⛔ No se permite avanzar en el flujo

---

## 🧪 Evidencia del Pipeline

### ✅ Ejecución exitosa

![CI Success](docs/ci-success.png)

### ❌ Fallo por pruebas

![Test Fail](docs/test-fail.png)

### ⚠️ Fallo por cobertura

![Coverage Fail](docs/coverage-fail.png)

---

## ☁️ Despliegue Continuo (CD)

El despliegue se realiza automáticamente en AWS Amplify:

* Se activa al hacer merge en `main`
* Publica el sitio en la nube
* Genera URL accesible públicamente

Esto permite simular un entorno real de producción.

---

## 📊 Gestión del Delivery con Azure DevOps

Se incorpora trazabilidad del trabajo mediante:

* Backlog priorizado
* User Stories
* Story Points
* Tablero Kanban

👉 Ver detalle: [boards_evidencia.md](./azure_devops/boards_evidencia.md)

---

## 🧱 Estructura del Repositorio

* `app_demo/` → Aplicación base para pruebas
* `sonarqube/` → Implementación de Quality Gate práctico
* `.github/workflows/` → Pipeline CI/CD
* `docs/` → Evidencias del pipeline
* `azure_devops/` → Gestión del trabajo

---

## 👩‍💼 Rol en este proyecto

En este proyecto asumí un rol integral de Delivery, donde:

* Diseñé el flujo de CI/CD
* Definí reglas de Quality Gate (coverage, linting)
* Implementé automatización con GitHub Actions
* Simulé control de calidad tipo SonarQube
* Integré trazabilidad de trabajo con Azure DevOps
* Implementé despliegue continuo en AWS Amplify

El foco fue demostrar cómo estructurar un flujo de entrega moderno, alineado a prácticas DevOps.

---

## 🚀 Conclusión

Este proyecto demuestra la implementación de un pipeline de entrega completo, integrando automatización, calidad y despliegue continuo en la nube, alineado a prácticas utilizadas en entornos reales de desarrollo.

---

## 🔗 Enlaces

👉 Repositorio GitHub
👉 Pipeline CI (GitHub Actions)
👉 Sitio en producción (AWS Amplify)
