# 📊 Evidencia de Gestión del Delivery – Azure DevOps

Este documento presenta la evidencia de uso de Azure DevOps como herramienta de gestión del delivery dentro del proyecto **Cloud Delivery Pipeline**, complementando el flujo técnico implementado con GitHub Actions (CI) y AWS Amplify (CD).

---

## 🎯 Objetivo

Demostrar la capacidad de:

* Gestionar backlog mediante historias de usuario y tareas
* Visualizar el flujo de trabajo con un tablero Kanban
* Mantener trazabilidad entre requerimientos y ejecución técnica
* Simular un entorno de delivery real en contexto empresarial

---

## 🧩 Estructura de trabajo

El trabajo fue organizado en los siguientes niveles:

### 🔷 Epic

* **Implementación de pipeline DevOps cloud**

### 🔹 User Stories

1. **Validar automáticamente la calidad del código**
   Implementación de CI mediante GitHub Actions, incluyendo pruebas y validación de cobertura.

2. **Automatizar el despliegue en entorno cloud**
   Despliegue continuo utilizando AWS Amplify como evidencia de CD real.

3. **Gestionar y dar trazabilidad al delivery del proyecto**
   Uso de Azure DevOps para administrar backlog, tareas y seguimiento del trabajo.

---

### 🔧 Tasks

Cada historia de usuario fue descompuesta en tareas técnicas específicas, permitiendo:

* Control detallado del avance
* Seguimiento del trabajo a nivel operativo
* Organización del esfuerzo por etapa

---

## 📌 Flujo de trabajo (Kanban)

Se configuró un tablero con las siguientes columnas:

* **To Do** → Trabajo pendiente
* **In Progress** → Trabajo en ejecución
* **QA / Testing** → Validación funcional
* **Done** → Trabajo completado

Este flujo permite visualizar claramente el estado de cada historia y su progreso dentro del ciclo de entrega.

---

## 📊 Gestión del avance

El tablero refleja un flujo de trabajo realista:

* Historias completadas con todas sus tareas cerradas
* Historias en progreso con avance parcial
* Historias pendientes en etapa de planificación

Este enfoque permite controlar tanto el avance macro (historias) como el detalle operativo (tasks).

---

## 📸 Evidencia visual

### 🧭 Tablero Kanban

![Board Azure DevOps](../docs/azure-board.png)

---

### 📋 Work Items (Backlog)

![Work Items](../docs/azure-workitems.png)

---

### 🧩 Detalle de User Story

![User Story](../docs/azure-userstory.png)

---

## 💡 Enfoque aplicado

La arquitectura del proyecto separa claramente:

### 🔧 Flujo técnico

* **GitHub Actions** → Integración Continua (CI)
* **AWS Amplify** → Despliegue continuo (CD real)

### 📊 Gestión del delivery

* **Azure DevOps** → Backlog, seguimiento y trazabilidad

Esto permite reflejar un modelo de trabajo alineado con entornos enterprise, donde la ejecución técnica y la gestión del trabajo operan de forma complementaria.

---

## 🧠 Conclusión

El uso de Azure DevOps en este proyecto permite:

* Organizar el trabajo de forma estructurada
* Visualizar el flujo de entrega
* Mantener trazabilidad entre requerimientos y ejecución
* Simular un entorno real de gestión de proyectos TI

Con esto, el portafolio no solo demuestra capacidades técnicas, sino también competencias en gestión del delivery y prácticas ágiles.
