# 🚀 Cloud Delivery Pipeline Portafolio

![CI/CD Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci_cd.yml/badge.svg)
![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)
![Code Quality](https://img.shields.io/badge/Quality-Gate%20Simulated-blue)
![Test Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)

Repositorio que demuestra la implementación de un **pipeline CI/CD completo** utilizando **GitHub Actions**, incorporando validación automática de calidad de código, medición de cobertura de pruebas y control de despliegue mediante un **Quality Gate simulado**.

---

## 🎯 Objetivo

Construir un pipeline que permita:

* Validar automáticamente la calidad del código
* Detectar errores de forma temprana
* Medir cobertura de pruebas de forma automatizada
* Bloquear despliegues si no se cumplen estándares
* Simular un flujo CI/CD utilizado en entornos empresariales

---

## ⚙️ Arquitectura del Pipeline

El pipeline está compuesto por tres etapas principales:

```text
Push
 ↓
CI (Tests + Coverage)
 ↓
Quality Gate (flake8)
 ↓
CD (Deploy simulado)
```

---

## 🔹 1. Integración Continua (CI)

* Instalación de dependencias
* Validación de entorno Python
* Ejecución de pruebas automatizadas con `pytest`
* Medición de cobertura con `pytest-cov`

---

## 📊 Test Coverage

El pipeline incorpora medición real de cobertura de pruebas mediante `pytest-cov`.

### 🎯 Resultado obtenido

* Cobertura total: **100%**
* Código completamente validado por tests automatizados

### 📸 Evidencia

![Test Coverage](docs/test-coverage.png)

---

## 🔹 2. Code Quality - Quality Gate Simulado

Se implementa una etapa de validación de calidad usando `flake8`, que actúa como un **Quality Gate**.

### 🔍 Validaciones

* Errores críticos de código
* Variables no definidas
* Complejidad excesiva
* Estándares de formato

👉 Si esta etapa falla, el pipeline se detiene automáticamente.

---

## 🚫 Quality Gate en acción

Se realizaron pruebas controladas para validar el comportamiento del pipeline.

### ❌ Caso 1: Falla de calidad

Se introdujo intencionalmente un error (`variable no definida`), provocando:

* Fallo en la etapa de calidad
* Bloqueo del pipeline
* Cancelación del despliegue

#### 📸 Evidencia

![Quality Gate Fail](docs/quality-gate-fail.png)

---

### ✅ Caso 2: Código corregido

Tras corregir el error:

* Tests exitosos
* Validación de calidad aprobada
* Despliegue ejecutado

#### 📸 Evidencia

![Pipeline Success](docs/pipeline-success.png)

---

## 🔹 3. Continuous Deployment (CD) Simulado

* Simulación de despliegue controlado
* Ejecutado solo si CI y Quality pasan correctamente

---

## 🎯 Resultado

El pipeline implementa correctamente un **Quality Gate**:

* Si la calidad falla → el despliegue NO ocurre
* Si la calidad pasa → el pipeline continúa

---

## 🧠 Enfoque técnico

Esta implementación replica el comportamiento de pipelines empresariales donde:

* La calidad del código es obligatoria antes del despliegue
* Se aplican controles automatizados de validación
* Se previenen errores en producción

El Quality Gate simulado representa el rol que cumplen herramientas como **SonarQube** en entornos reales.

---

## 🚀 Valor del Portafolio

Este proyecto demuestra:

* Implementación de CI/CD con GitHub Actions
* Integración de validación de calidad automatizada
* Medición real de cobertura de pruebas
* Control de flujo mediante dependencias entre jobs (`needs`)
* Simulación de despliegue condicionado por calidad
* Enfoque DevOps orientado a calidad y confiabilidad

---

## 📁 Estructura del Proyecto

```text
cloud-delivery-pipeline-portafolio/
├── .github/workflows/
│   ├── ci.yml
│   └── ci_cd.yml
├── app_demo/
│   ├── src/
│   ├── tests/
│   └── requirements.txt
├── docs/
│   ├── test-coverage.png
│   ├── quality-gate-fail.png
│   └── pipeline-success.png
└── README.md
```

---

## 🧩 Próximos pasos

* Integración con SonarQube real
* Implementación de despliegue real (AWS / Azure)
* Gestión de artefactos
* Pipeline multi-entorno (dev / qa / prod)

---

## 💬 Contexto profesional

Este pipeline fue diseñado como parte de un portafolio orientado a roles como:

* Cloud & DevOps Delivery Manager
* Cloud Project Manager
* Platform Delivery Manager

---

## 🏁 Conclusión

Se implementa un pipeline CI/CD completo con control de calidad automatizado y medición de cobertura, demostrando cómo prevenir despliegues de código defectuoso y asegurar estándares antes de liberar cambios.

---
