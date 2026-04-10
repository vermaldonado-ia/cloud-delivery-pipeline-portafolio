# 🔍 Code Quality - SonarQube (Simulado)

Este módulo representa la integración de **análisis de calidad de código** dentro del pipeline CI/CD, utilizando herramientas como **SonarQube** para evaluar mantenibilidad, confiabilidad y buenas prácticas de desarrollo.

---

## 🎯 Objetivo

Incorporar una etapa de **Code Quality** dentro del pipeline, permitiendo:

* Detectar problemas de código de forma temprana
* Reducir deuda técnica
* Asegurar estándares de desarrollo
* Actuar como un **Quality Gate** antes del despliegue

---

## ⚙️ Rol dentro del pipeline

El análisis de calidad se ubica entre CI y CD:

```text
Push
  ↓
CI (tests)
  ↓
Code Quality (SonarQube / Linting)
  ↓
CD (simulado)
```

Esta etapa asegura que solo código validado avance hacia la liberación.

---

## 🔧 Validaciones consideradas

* Análisis estático de código
* Detección de errores potenciales
* Identificación de código duplicado
* Evaluación de mantenibilidad
* Cumplimiento de buenas prácticas

---

## 🧠 Concepto de Quality Gate

El **Quality Gate** define criterios mínimos de calidad que deben cumplirse para continuar el pipeline.

Ejemplo de validaciones:

* Sin errores críticos
* Cobertura mínima de pruebas
* Sin vulnerabilidades
* Nivel aceptable de deuda técnica

Si el código no cumple estas condiciones, el despliegue debería bloquearse.

---

## 🔄 Integración con el pipeline

Actualmente, esta etapa se representa de forma **conceptual / simulada**, complementada con:

* Linting
* Validaciones del pipeline CI
* Buenas prácticas de desarrollo

En una implementación completa, se integraría con SonarQube mediante:

* Análisis automático en cada commit
* Evaluación de métricas de calidad
* Bloqueo del pipeline si falla el Quality Gate

---

## 🚀 Evolución futura

Para llevar esta integración a un entorno real, se podría:

* Configurar un servidor SonarQube
* Integrar SonarScanner en el pipeline CI
* Definir reglas de Quality Gate
* Visualizar métricas en dashboard

---

## 💬 Enfoque

Este módulo demuestra cómo la calidad de código forma parte fundamental del proceso CI/CD, asegurando que el software no solo funcione, sino que también sea mantenible, seguro y escalable.
