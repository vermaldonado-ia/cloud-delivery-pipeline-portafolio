# 🛡️ Code Quality - Quality Gate

![Quality Gate](https://img.shields.io/badge/Quality%20Gate-Enabled-success)
![Tests](https://img.shields.io/badge/Tests-Pytest-blue)
![Coverage](https://img.shields.io/badge/Coverage-80%25-green)

Este módulo implementa un **Quality Gate práctico** dentro del pipeline CI/CD, asegurando que solo código que cumple estándares mínimos de calidad pueda avanzar hacia despliegue.

Se inspira en herramientas como:

* SonarQube
* Azure DevOps Quality Gates
* GitHub Advanced Security

pero está implementado de forma **ligera y funcional** utilizando GitHub Actions.

---

## 🎯 Objetivo

Implementar un mecanismo automático que permita:

* Detectar errores de forma temprana (Shift Left)
* Validar estándares de desarrollo
* Controlar cobertura de pruebas
* Bloquear cambios defectuosos antes del despliegue

---

## 📐 Rol dentro del pipeline

El Quality Gate actúa como un punto de control obligatorio dentro del flujo de entrega:

Pull Request / Push
↓
CI (Tests + Coverage)
↓
Code Quality (Quality Gate)
↓
Merge controlado
↓
CD Automático (AWS Amplify)

---

## 🔍 Validaciones aplicadas

El Quality Gate se basa en tres pilares:

### ✔ 1. Ejecución de pruebas

* Tests ejecutados con `pytest`
* Validación de funcionalidad del código

---

### ✔ 2. Cobertura de código

* Medición con `pytest-cov`
* Umbral mínimo: **80%**

```bash
pytest --cov=src --cov-fail-under=80
```

Si la cobertura es menor:

⛔ El pipeline falla automáticamente

---

### ✔ 3. Calidad del código (Linting)

* Análisis con `flake8`
* Validación de buenas prácticas y estilo

```bash
flake8 src/
```

Si existen errores críticos:

⛔ El pipeline se detiene

---

## ⚙️ Implementación técnica

El Quality Gate está integrado dentro de GitHub Actions:

* Se ejecuta en cada Pull Request
* Se ejecuta en cada push a `main`
* Forma parte del pipeline CI

Archivo asociado:

```
.github/workflows/ci.yml
```

---

## 🚫 Comportamiento ante fallos

Si alguna validación no se cumple:

* ❌ Tests fallan → no hay merge
* ❌ Coverage bajo → pipeline detenido
* ❌ Errores de linting → pipeline detenido

👉 Esto garantiza que solo código validado avance en el flujo.

---

## 🔍 Equivalencia en entornos reales

Este enfoque replica de forma práctica lo que herramientas enterprise realizan:

| Herramienta              | Equivalente en este proyecto |
| ------------------------ | ---------------------------- |
| SonarQube                | Validación de calidad        |
| Azure DevOps             | Quality Gate                 |
| GitHub Advanced Security | Control automatizado         |

---

## 🧠 Enfoque de diseño

Este módulo no busca replicar completamente herramientas complejas, sino demostrar:

* Cómo implementar control de calidad sin herramientas pesadas
* Cómo integrar validaciones dentro del flujo CI/CD
* Cómo aplicar principios DevOps en escenarios reales

---

## 📚 Aprendizajes clave

* Importancia de validar calidad antes del merge
* Uso de métricas como coverage en pipelines CI
* Integración de testing y linting en automatización
* Control del flujo de entrega mediante Quality Gates

---

## 🚀 Conclusión

Este módulo demuestra cómo implementar un Quality Gate funcional dentro de un pipeline moderno, asegurando calidad continua y alineación con prácticas utilizadas en entornos productivos DevOps.
