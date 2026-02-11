# Runbook 01 – ImagePullBackOff

## Escenario
El pod no inicia porque OpenShift no puede descargar la imagen del registro.

---

## Síntomas observados
- `kubectl get pods` o `oc get pods` muestra `ImagePullBackOff`.
- `oc describe pod <nombre-del-pod>` indica un error relacionado con la imagen: “manifest unknown” o “unauthorized”.

---

## Diagnóstico paso a paso

1. Verificar el estado del pod:
```
oc get pods
```
Inspeccionar los eventos y la razón exacta del fallo:

```
oc describe pod <nombre-del-pod>
```
Confirmar que la imagen exista en el registry:
```
podman images
```

Corrección aplicada
Construir la imagen localmente asegurándose de usar el tag correcto:
```
podman build -t <registry>/<project>/openshift-demo:1.1 .
```

Subir la imagen al registry de OpenShift:
```
podman push <registry>/<project>/openshift-demo:1.1
```
Actualizar el deployment para usar la nueva imagen:
```
oc set image deployment/openshift-demo openshift-demo=<registry>/<project>/openshift-demo:1.1
```
Verificar que el pod reinicie correctamente:
```
oc get pods -w
```
Estado final
El pod cambia de ImagePullBackOff a Running.

La aplicación responde correctamente en sus endpoints / y /api.

Aprendizaje
Siempre verificar el tag y la existencia de la imagen en el registry antes de actualizar un deployment.

OpenShift no permite que un pod inicie si la imagen indicada no existe o no es accesible.

Mantener consistencia entre los tags locales y los del registry evita errores repetidos.