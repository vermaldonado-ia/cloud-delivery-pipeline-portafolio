# 🔍 Code Quality - Quality Gate Simulado

![Code Quality](https://img.shields.io/badge/Quality-Gate%20Simulated-blue)
![Linting](https://img.shields.io/badge/Linting-Flake8-blueviolet)

Este módulo representa la implementación de un **Quality Gate dentro de un pipeline CI/CD**, simulando el comportamiento de herramientas como **SonarQube** mediante el uso de `flake8`.

---

## 🎯 Objetivo

Incorporar una etapa de validación de calidad que permita:

* Detectar errores de código de forma temprana
* Reducir deuda técnica
* Asegurar estándares mínimos de desarrollo
* Bloquear el despliegue si no se cumplen criterios de calidad

---

## ⚙️ Rol dentro del pipeline

El flujo implementado es:

```text
CI (Tests)
 ↓
Code Quality (flake8)
 ↓
CD (Deploy)
```

El Quality Gate se ubica entre CI y CD, actuando como punto de control obligatorio.

---

## 🔍 Validaciones implementadas

Se utilizan reglas de `flake8` para validar la calidad del código en dos niveles:

---

### 🔹 1. Errores críticos

```bash
flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
```

Detecta:

* Errores de sintaxis
* Variables no definidas
* Fallos críticos de ejecución

👉 Si se detecta alguno → el pipeline falla inmediatamente.

---

### 🔹 2. Calidad y mantenibilidad

```bash
flake8 src --count --max-complexity=10 --max-line-length=88 --statistics
```

Evalúa:

* Complejidad ciclomática
* Estándares de formato
* Legibilidad del código

---

## 🚫 Comportamiento del Quality Gate

El comportamiento implementado es:

* Si `flake8` detecta errores → el job falla
* El pipeline se detiene automáticamente
* El despliegue NO se ejecuta

Esto se logra mediante la configuración de dependencias entre jobs en GitHub Actions:

```yaml
quality:
  needs: test

deploy:
  needs: quality
```

---

## 🧪 Prueba de validación

Se realizó una prueba controlada introduciendo un error en el código:

```python
def prueba():
    print(variable_no_definida)
```

### Resultado

* ❌ Falla en etapa de calidad
* ⛔ Bloqueo del pipeline
* 🚫 Deploy no ejecutado

---

## 🧠 Enfoque aplicado

Este enfoque simula el comportamiento de herramientas empresariales como:

* SonarQube
* Quality Gates corporativos
* Políticas de control de despliegue

---

## 🚀 Valor del módulo

Este componente permite demostrar:

* Control de calidad automatizado
* Integración de validaciones dentro del pipeline CI/CD
* Prevención de errores antes del despliegue
* Gobernanza técnica del código

---

## 🔮 Evolución futura

* Integración con SonarQube real
* Métricas avanzadas de calidad (coverage, duplicación, deuda técnica)
* Dashboards de calidad
* Gates configurables por entorno

---

## 🏁 Conclusión

Se implementa un **Quality Gate simulado funcional**, que bloquea automáticamente el pipeline en caso de incumplimiento de estándares de calidad, replicando prácticas utilizadas en entornos DevOps empresariales.

---
