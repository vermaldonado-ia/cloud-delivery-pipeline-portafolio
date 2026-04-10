# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-green)
![Coverage](https://img.shields.io/badge/Coverage-Enforced-red)

Repositorio que demuestra la implementación de un **pipeline de Integración Continua (CI)** utilizando **GitHub Actions**, enfocado en asegurar la calidad del código mediante automatización de validaciones.

---

## 🎯 Objetivo

Implementar un pipeline CI que permita:

- Validar la calidad del código automáticamente  
- Detectar errores de forma temprana  
- Asegurar cobertura mínima de pruebas  
- Establecer un Quality Gate antes de integrar cambios  

---

## ⚙️ Pipeline CI implementado

El pipeline se ejecuta automáticamente en cada:

- `push` a `main`
- `pull request`

### Etapas:

1. Instalación de dependencias  
2. Configuración de entorno Python  
3. Ejecución de pruebas (`pytest`)  
4. Medición de cobertura (`pytest-cov`)  
5. Validación de umbral mínimo (`--cov-fail-under`)  

---

## 🧪 Validación del pipeline

El pipeline fue validado en distintos escenarios reales:

---

### ✅ Ejecución exitosa

- Tests exitosos  
- Cobertura sobre el umbral  
- Pipeline completo OK  

![CI Success](docs/ci-success.png)

---

### ❌ Falla por error funcional

- Error introducido en el código  
- Tests detectan inconsistencia  
- Pipeline falla automáticamente  

![Test Fail](docs/test-fail.png)

---

### ❌ Falla por cobertura insuficiente

- Eliminación de pruebas  
- Coverage bajo el mínimo  
- Activación del Quality Gate  

![Coverage Fail](docs/coverage-fail.png)

---

## 🧠 Enfoque DevOps

Este pipeline implementa control de calidad en múltiples niveles:

- ✔ Validación funcional (tests)  
- ✔ Control de cobertura mínima  
- ✔ Automatización CI  

---

## 📁 Estructura

```bash
cloud-delivery-pipeline-portafolio/
├── .github/workflows/ci.yml
├── app_demo/
├── docs/
├── sonarqube/
└── README.md
