# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg) ![Coverage](https://img.shields.io/badge/coverage-80%25-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-green)
![Coverage](https://img.shields.io/badge/Coverage-Enforced-orange)

Repositorio que demuestra la implementación de un pipeline DevOps completo, incorporando prácticas de Integración Continua (CI), control de calidad (Quality Gate), gestión de Pull Request y despliegue simulado (CD).

---

## 🎯 Objetivo

Implementar un pipeline que permita:

- Detectar errores de forma temprana  
- Asegurar calidad del código antes del merge  
- Validar cobertura de pruebas  
- Controlar cambios hacia la rama principal  
- Representar un proceso controlado de entrega continua  

---

## ⚙️ Arquitectura del Pipeline

**Pull Request / Push → CI (Tests + Coverage) → Quality Gate → Merge controlado → CD Simulado**

---

## 🔄 Flujo de ejecución

1. Se crea un Pull Request hacia la rama principal  
2. Se ejecuta automáticamente el pipeline de CI  
3. Se validan pruebas y cobertura  
4. Se ejecuta el control de calidad (Quality Gate)  
5. Si todo es exitoso, se permite el merge  
6. Se activa el flujo de despliegue simulado (CD)  

---

## 🔄 Integración Continua (CI)

El pipeline ejecuta automáticamente:

- Instalación de dependencias  
- Configuración de entorno Python  
- Ejecución de pruebas con pytest  
- Medición de cobertura con pytest-cov  

Esto permite validar cada cambio antes de integrarlo a la rama principal.

---

## 🧪 Evidencia del pipeline

### ✔️ Ejecución exitosa
![CI Success](docs/ci-success.png)

### ❌ Falla por pruebas
Se provocó un error intencional para validar detección de fallas reales.

![Test Fail](docs/test-fail.png)

### 📊 Falla por cobertura
Se configuró una cobertura mínima para validar el control del pipeline.

![Coverage Fail](docs/coverage-fail.png)

---

## 🛡️ Code Quality (Quality Gate)

Se implementa un control de calidad basado en:

- flake8 (análisis estático)  
- Validación de cobertura  
- Ejecución automática en CI  

Este módulo actúa como un Quality Gate, bloqueando el pipeline si no se cumplen estándares mínimos.

Más detalle en: 👉 `sonarqube/README.md`

---

## 🔐 Control de Pull Request (PR)

Se aplican buenas prácticas DevOps:

- Validación automática en cada PR  
- Bloqueo de merge si el pipeline falla  
- Protección de la rama main  

Esto asegura que solo código validado avance en el flujo de entrega.

---

## 🚀 Continuous Deployment (CD) Simulado

El pipeline incluye una etapa de despliegue que:

- Revalida el estado del código  
- Prepara artefacto de release  
- Genera carpeta `simulated_release`  

Esto representa un flujo real de entrega sin depender de infraestructura externa.

---

## 🧠 Enfoque DevOps aplicado

Este proyecto demuestra:

- Automatización de validaciones  
- Shift Left Testing  
- Control de calidad integrado  
- Flujo CI/CD completo  
- Gestión de fallos en pipeline  

---

## 🛠️ Tecnologías utilizadas

- Python 3.11  
- pytest  
- pytest-cov  
- flake8  
- GitHub Actions  

---

## 📈 Valor del proyecto

Este enfoque permite:

- Reducir defectos en producción  
- Asegurar calidad continua  
- Mejorar la confiabilidad del proceso de entrega  
- Mantener trazabilidad end-to-end del pipeline  

---

## 📌 Estado del proyecto

- ✔ CI implementado  
- ✔ Quality Gate implementado  
- ✔ PR controlado  
- ✔ CD simulado  
- ⬜ Deploy real (siguiente evolución)  

---

## 🚀 Próximos pasos

- Implementar despliegue real (GitHub Pages o API)  
- Integrar herramienta de análisis avanzada (SonarQube)  
- Publicar métricas del pipeline  

---

## 👩‍💻 Autora

**Verónica Maldonado**  
Ingeniera Civil Informática  
Especialista en Gestión de Proyectos TI | Agile | Cloud | DevOps  
