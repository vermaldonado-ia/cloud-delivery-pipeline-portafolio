# 🚀 Cloud Delivery Pipeline Portafolio

![CI](https://img.shields.io/badge/CI-GitHub_Actions-blue)
![Coverage](https://img.shields.io/badge/Coverage-80%25-green)
![CD](https://img.shields.io/badge/CD-AWS_Amplify-orange)
![Status](https://img.shields.io/badge/Status-Production-success)

💡 Caso práctico de implementación de un pipeline DevOps real, integrando prácticas de calidad, automatización y despliegue continuo en la nube, alineado a flujos utilizados en entornos productivos.

---

## 🌐 Producción

👉 URL del sitio desplegado:
https://main.d28beryienq64n.amplifyapp.com

El despliegue continuo se realiza automáticamente en AWS Amplify, generando un entorno productivo accesible tras cada cambio en la rama principal.

---

## 🎯 Objetivo

Implementar un pipeline que permita:

* Detectar errores de forma temprana (Shift Left)
* Asegurar calidad del código antes del merge
* Validar cobertura de pruebas
* Controlar cambios hacia producción
* Automatizar el despliegue en la nube

---

## 💼 Valor entregado

* Reducción de errores en etapas tempranas mediante CI
* Control de calidad automatizado previo al despliegue
* Flujo de entrega continuo sin intervención manual
* Implementación de un pipeline alineado a prácticas DevOps reales

---

## 📐 Arquitectura del flujo

Dev → Pull Request → CI (Tests + Coverage) → Quality Gate → Merge → CD (AWS Amplify) → Producción

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
↓
Aplicación disponible en producción

---

## 🔄 Integración Continua (CI)

El pipeline ejecuta automáticamente:

* Instalación de dependencias
* Configuración de entorno Python
* Ejecución de pruebas con pytest
* Medición de cobertura con pytest-cov
* Análisis de calidad con flake8

Esto permite validar cada cambio antes de integrarlo a la rama principal, reduciendo riesgos en etapas posteriores del ciclo de entrega.

---

## 🛡️ Code Quality - Quality Gate

Se implementa un Quality Gate práctico inspirado en herramientas enterprise como:

* SonarQube
* Azure DevOps Quality Gates

Validaciones aplicadas:

* ✔ Tests deben pasar
* ✔ Coverage mínimo: 80%
* ✔ Código sin errores de linting

Si alguna condición falla:

⛔ El pipeline se detiene
⛔ No se permite avanzar en el flujo

---

## 🔍 Evidencia real del flujo CI/CD

A continuación se muestra la ejecución real del pipeline y el despliegue en la nube:

---

### ⚙️ GitHub Actions – Pipeline ejecutado

![Pipeline GitHub Actions](docs/github-actions.png)

✔ Ejecución automática tras merge en `main`
✔ Validación de CI completada exitosamente
✔ Integración continua aplicada sobre cada cambio

---

### ☁️ AWS Amplify – Despliegue en producción

![AWS Amplify Deploy](docs/aws-amplify.png)

✔ Despliegue automático tras merge en `main`
✔ Aplicación publicada en entorno cloud productivo
✔ URL accesible públicamente

---

💡 Este flujo demuestra un pipeline end-to-end donde cada cambio validado es automáticamente desplegado en un entorno productivo en la nube.

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

* Se activa tras cada merge a `main`
* Ejecuta build y publicación
* Genera una URL productiva accesible

Esto permite un flujo de entrega continuo, automatizado y alineado a prácticas DevOps modernas.

---

## 📊 Gestión del Delivery con Azure DevOps

Se incorpora trazabilidad del trabajo mediante:

* Backlog priorizado
* User Stories
* Story Points
* Tablero Kanban

👉 Ver detalle: [boards_evidencia.md](./azure_devops/boards_evidencia.md)

Esto permite conectar la gestión del trabajo con la ejecución técnica del pipeline.

---

## ⚠️ Alcance del proyecto

* CI → Implementación real
* Quality Gate → Implementación práctica basada en estándares de la industria
* CD → Implementación real en AWS Amplify
* Gestión → Simulación de entorno organizacional con Azure DevOps

---

## 🧠 Enfoque de Delivery

Este proyecto demuestra cómo estructurar un flujo de entrega que:

* Minimiza riesgos antes del despliegue
* Asegura calidad continua
* Automatiza el ciclo de release
* Permite escalar el modelo a equipos reales
* Integra prácticas DevOps con gestión ágil

---

## 📚 Aprendizajes clave

* Importancia del control de calidad previo al merge
* Uso de métricas como coverage en CI
* Automatización del flujo de entrega end-to-end
* Integración entre prácticas DevOps y gestión ágil

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
* Implementé control de calidad inspirado en prácticas enterprise
* Integré trazabilidad de trabajo con Azure DevOps
* Implementé despliegue continuo en AWS Amplify

El foco fue demostrar la construcción de un flujo de entrega moderno, alineado a prácticas DevOps utilizadas en entornos productivos.

---

## 🚀 Conclusión

Este proyecto refleja la capacidad de diseñar e implementar un pipeline DevOps completo, integrando automatización, control de calidad y despliegue continuo en la nube, permitiendo entregar software de forma segura, repetible y escalable.

---

## 🔗 Enlaces

👉 Portafolio Cloud & DevOps: https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio
👉 CI/CD Pipeline – GitHub Actions: https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions
👉 Demo Cloud – AWS Amplify: https://main.d28beryienq64n.amplifyapp.com

