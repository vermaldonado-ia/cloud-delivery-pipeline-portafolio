# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)

Repositorio que demuestra la implementación de un **pipeline CI/CD** utilizando **GitHub Actions**, enfocado en la automatización de validaciones, pruebas y simulación de despliegues.

---

## 🎯 Objetivo

Construir un pipeline que permita:

* Validar la calidad del código automáticamente
* Detectar errores de forma temprana
* Asegurar consistencia en el desarrollo
* Simular un flujo de despliegue continuo (CD)
* Generar evidencia trazable del proceso

---

## ⚙️ Continuous Integration (CI)

El pipeline de CI se ejecuta automáticamente en cada `push` y `pull request` hacia la rama `main`.

### 🔧 ¿Qué valida el CI?

* Instalación de dependencias
* Validación del entorno Python
* Ejecución de pruebas automatizadas con `pytest`
* Verificación de calidad de código

### 🔄 Flujo CI

```text
Push / Pull Request
        ↓
Instalación de dependencias
        ↓
Ejecución de pruebas
        ↓
Validación de resultados
```

---

## 🚀 Continuous Deployment (CD) Simulado

Este repositorio incluye una etapa de **Continuous Deployment (CD) simulado**, que representa el flujo de entrega posterior a la validación del CI.

### 🎯 Objetivo

Demostrar cómo un cambio validado puede ser promovido automáticamente hacia una etapa de liberación, manteniendo trazabilidad y automatización del proceso.

---

### ⚙️ Flujo CD

```text
Push a main
   ↓
Pipeline CI (validación de código)
   ↓
Pruebas exitosas
   ↓
CD Simulado
   ↓
Generación de artifact de despliegue
```

---

### 🔧 ¿Qué realiza el CD?

* Ejecuta pruebas antes del despliegue
* Genera una carpeta de release simulada
* Crea un archivo de evidencia (`deployment_log.txt`)
* Publica un artifact descargable

---

### 📦 Evidencia de despliegue

El pipeline genera un artifact que contiene:

* `app_demo/`
* `deployment_log.txt`

El archivo `deployment_log.txt` incluye:

* Fecha de ejecución
* Commit asociado
* Rama de despliegue
* Estado del despliegue

Ejemplo:

```text
Release preparado correctamente
Fecha: Fri Apr 10 ...
Commit: 76e6557...
Branch: main
Estado: Deploy simulado exitoso
```

---

### 🧠 Valor técnico

Este enfoque permite:

* Automatizar la promoción de cambios
* Asegurar calidad antes del despliegue
* Generar evidencia auditable
* Simular un flujo real de entrega continua
* Mantener trazabilidad completa del proceso

---

## 📸 Evidencia visual

### ✅ Ejecución del pipeline CD

![CD Workflow](docs/img/cd_simulado_workflow.png)

---

### 📦 Artifact generado

![CD Artifact](docs/img/cd_simulado_artifact.png)

---

### 📁 Contenido del despliegue simulado

![CD Content](docs/img/cd_simulado_contenido.png)

---

## 🧩 Estructura del proyecto

```text
cloud-delivery-pipeline-portafolio/
├── .github/workflows/
│   ├── ci.yml
│   └── cd.yml
├── app_demo/
│   ├── src/
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
├── docs/
│   └── img/
├── README.md
```

---

## 🚀 Tecnologías utilizadas

* GitHub Actions
* Python
* Pytest
* Git

---

## 📈 Próximos pasos

* Implementar despliegue real en la nube (AWS / Azure)
* Incorporar ambientes (`dev`, `qa`, `prod`)
* Agregar aprobaciones manuales
* Integrar análisis de calidad con SonarQube

---

## 💬 Enfoque profesional

Este repositorio representa un flujo base de CI/CD orientado a buenas prácticas DevOps, donde se prioriza:

* Automatización
* Calidad
* Trazabilidad
* Entrega continua

---

## 👩‍💻 Autor

**Verónica Maldonado Céspedes**
Cloud & DevOps Delivery | Agile | CI/CD

---
