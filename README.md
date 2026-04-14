# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-green)
![Coverage](https://img.shields.io/badge/Coverage-Enforced-orange)

Repositorio que demuestra la implementación de un **pipeline DevOps completo**, incorporando prácticas de Integración Continua (CI), validación de calidad (Quality Gate), control de Pull Request y despliegue simulado (CD).

---

## 🎯 Objetivo

Implementar un pipeline que permita:

- Detectar errores de forma temprana  
- Asegurar calidad del código  
- Validar cobertura de pruebas  
- Controlar cambios hacia producción  
- Simular un flujo real de despliegue  

---

## ⚙️ Arquitectura del Pipeline

Flujo implementado:

Pull Request / Push
↓
CI (Tests + Coverage)
↓
Code Quality (Quality Gate)
↓
Merge a main (controlado)
↓
CD Simulado (Release)


---

## 🔄 Integración Continua (CI)

El pipeline ejecuta automáticamente:

- Instalación de dependencias  
- Configuración de entorno Python  
- Ejecución de pruebas con pytest  
- Medición de cobertura con pytest-cov  

Esto permite validar cada cambio antes de integrarlo a la rama principal.

---

## 🧪 Evidencia: Pipeline exitoso

![CI Success](docs/ci-success.png)

---

## ❌ Evidencia: Falla por pruebas

Se provocó un error intencional en el código para validar que el pipeline detecta fallas reales.

![Test Fail](docs/test-fail.png)

---

## 📊 Evidencia: Falla por cobertura

Se configuró una validación de cobertura mínima, generando una falla controlada del pipeline.

![Coverage Fail](docs/coverage-fail.png)

---

## 🧪 Code Quality (Quality Gate)

Se implementa un control de calidad basado en:

- flake8 (análisis estático)
- validación de cobertura
- ejecución automática en CI

Este módulo actúa como un **Quality Gate simulado**, bloqueando el pipeline si no se cumplen estándares mínimos.

Más detalle en:
👉 `sonarqube/README.md`

---

## 🔐 Control de Pull Request (PR)

Se aplican buenas prácticas DevOps:

- Validación automática en cada PR  
- Bloqueo de merge si el pipeline falla  
- Protección de la rama `main`  

Esto asegura que solo código validado llegue a producción.

---

## 🚀 Continuous Deployment (CD) Simulado

El pipeline incluye una etapa de despliegue que:

- valida nuevamente el código  
- prepara artefacto de release  
- genera carpeta `simulated_release`  

Esto representa un flujo real de despliegue sin necesidad de infraestructura externa.

---

## 🧠 Enfoque DevOps aplicado

Este proyecto demuestra:

- Automatización de validaciones  
- Shift Left Testing  
- Control de calidad integrado  
- Flujo CI/CD completo  
- Manejo de fallos del pipeline  

---

## 🛠️ Tecnologías utilizadas

- Python 3.11  
- pytest  
- pytest-cov  
- flake8  
- GitHub Actions  

---

## 📌 Estado del proyecto

✔ CI implementado  
✔ Quality Gate implementado  
✔ PR controlado  
✔ CD simulado  
⬜ Deploy real (próximo paso)

---

## 🚀 Próximos pasos

- Implementar despliegue real (GitHub Pages o API)
- Integrar herramienta real de análisis (SonarQube)
- Publicar resultados del pipeline

---

## 👩‍💻 Autora

**Verónica Maldonado**  
Ingeniera Civil Informática  
Especialista en Gestión de Proyectos TI | Agile | Cloud | DevOps  
