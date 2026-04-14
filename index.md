# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci_cd.yml/badge.svg)

Proyecto que implementa un **pipeline DevOps completo**, integrando prácticas de **Integración Continua (CI)**, control de calidad (**Quality Gate**), gestión de Pull Request y **despliegue simulado (CD)**, con publicación en **GitHub Pages** como evidencia del flujo de entrega.

---

## 👩‍💻 Sobre este proyecto

Este portafolio fue desarrollado con foco en demostrar cómo estructurar un flujo de entrega moderno bajo principios DevOps, priorizando:

- Automatización  
- Calidad del código  
- Control del flujo de cambios  
- Visibilidad del proceso de entrega  

---

## 🎯 Objetivo

Implementar un pipeline que permita:

- Detectar errores de forma temprana  
- Asegurar calidad del código antes del merge  
- Validar cobertura de pruebas  
- Controlar cambios hacia la rama principal  
- Simular un proceso real de despliegue  

---

## ⚙️ Arquitectura del Pipeline

Flujo implementado:

**Pull Request / Push → CI (Tests + Coverage) → Code Quality (Quality Gate) → Merge controlado → CD Simulado → GitHub Pages**

Este enfoque permite separar claramente:

- Validación técnica  
- Control de calidad  
- Publicación del resultado  

---

## 🔄 Integración Continua (CI)

El pipeline de CI ejecuta automáticamente:

- Instalación de dependencias  
- Validación del entorno Python  
- Ejecución de pruebas con `pytest`  
- Medición de cobertura con `pytest-cov`  

Esto asegura estabilidad del código antes de integrarlo.

---

## 🛡️ Quality Gate (Control de Calidad)

Se implementa un control de calidad con `flake8`, permitiendo:

- Detectar errores críticos  
- Validar estándares de desarrollo  
- Evitar la propagación de deuda técnica  

Actúa como un **punto de control obligatorio antes del merge**.

---

## 🚀 Continuous Deployment (CD) Simulado

Se incluye una etapa de despliegue simulado que:

- Genera un artefacto de release  
- Registra información del despliegue (commit, fecha, branch)  
- Representa un flujo controlado de entrega  

Esto permite modelar un proceso real sin depender de infraestructura productiva.

---

## 🌐 GitHub Pages (Publicación)

El proyecto se encuentra publicado mediante GitHub Pages, lo que permite:

- Exponer el pipeline como un artefacto visible  
- Facilitar la evaluación técnica  
- Mostrar el resultado final del proceso de entrega  

---

## 🧩 Componentes del Proyecto

- CI/CD Pipeline con GitHub Actions  
- Testing automatizado (`pytest`)  
- Coverage (`pytest-cov`)  
- Quality Gate (`flake8`)  
- CD Simulado  
- Publicación en GitHub Pages  

---

## 🧰 Tecnologías utilizadas

- GitHub Actions  
- Python  
- pytest  
- pytest-cov  
- flake8  
- GitHub Pages

---

## 📈 Valor del Proyecto

Este proyecto demuestra:

- Implementación práctica de DevOps  
- Separación de responsabilidades en el pipeline  
- Control de calidad antes de integración  
- Trazabilidad del flujo de entrega  
- Capacidad de exponer soluciones técnicas de forma clara  

---

## 🧠 Enfoque de entrega

Se aplicó un enfoque orientado a **Delivery**, donde:

- CI asegura calidad técnica  
- Quality Gate controla estándares  
- CD representa la entrega  
- GitHub Pages actúa como vitrina del producto  

---

## ✅ Estado Actual

Proyecto **activo y publicado**, con:

- Validaciones de CI operativas  
- Quality Gate implementado  
- Flujo de Pull Request controlado  
- CD simulado funcional  
- Publicación en GitHub Pages  

---

## 🔗 Repositorio

👉 https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio

---
