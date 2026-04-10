# 🔍 Code Quality - Quality Gate Simulado

![Code Quality](https://img.shields.io/badge/Quality-Gate%20Simulated-blue)
![Linting](https://img.shields.io/badge/Linting-Flake8-blueviolet)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)

Este módulo representa la implementación de un **Quality Gate dentro de un pipeline CI/CD**, simulando el rol de herramientas como **SonarQube** mediante el uso de `flake8`, y complementando la validación con cobertura real de pruebas usando `pytest-cov`.

---

## 🎯 Objetivo

Incorporar una etapa de validación que permita:

* Detectar errores de código de forma temprana
* Asegurar estándares mínimos de calidad
* Validar cobertura de pruebas
* Bloquear el despliegue si no se cumplen los criterios definidos

---

## ⚙️ Rol dentro del pipeline

El flujo implementado es:

```text
CI (Tests + Coverage)
 ↓
Code Quality (flake8)
 ↓
CD (Deploy)
```

El Quality Gate se ubica entre CI y CD, actuando como punto de control obligatorio antes del despliegue.

---

## 🔍 Validaciones implementadas

### 1. Cobertura de pruebas real

Se utiliza `pytest-cov` para medir qué porcentaje del código está cubierto por pruebas automatizadas.

**Resultado actual:**

* Coverage total: **100%**

---

### 2. Errores críticos de calidad

```bash
flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
```

Detecta:

* Errores de sintaxis
* Variables no definidas
* Fallos críticos de ejecución

---

### 3. Calidad y mantenibilidad

```bash
flake8 src --count --max-complexity=10 --max-line-length=88 --statistics
```

Evalúa:

* Complejidad ciclomática
* Formato y legibilidad
* Reglas básicas de mantenibilidad

---

## 🚫 Comportamiento del Quality Gate

El comportamiento implementado es:

* Si los tests fallan → el pipeline se detiene
* Si `flake8` detecta errores → el job `quality` falla
* Si `quality` falla → el despliegue no se ejecuta

Esto se implementa con dependencias entre jobs en GitHub Actions.

```yaml
quality:
  needs: test

deploy:
  needs: quality
```

---

## 🧪 Prueba de validación

Se realizó una prueba controlada introduciendo un error intencional en el código:

```python
def prueba():
    print(variable_no_definida)
```

### Resultado

* ❌ Falla en etapa de calidad
* ⛔ Bloqueo del pipeline
* 🚫 Deploy no ejecutado

---

## 🧠 Alcance actual

Actualmente:

* La ejecución del pipeline en GitHub Actions es real
* La medición de coverage es real
* La validación con `flake8` es real
* El Quality Gate está simulado en su enfoque respecto a SonarQube
* La integración con SonarQube real queda como evolución futura

---

## 🔮 Evolución futura

* Integración con SonarQube o SonarCloud
* Quality Gates avanzados
* Umbral mínimo de coverage
* Métricas de duplicación y deuda técnica

---

## 🏁 Conclusión

Se implementa un **pipeline funcional con validaciones reales de testing, coverage y calidad**, donde el rol del Quality Gate se simula mediante `flake8`, replicando la lógica de control previa al despliegue utilizada en entornos DevOps empresariales.

---
