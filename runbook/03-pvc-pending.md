# Error 05 - PersistentVolumeClaim en estado Pending

## Síntomas

```
oc get pvc
```
Estado:  Pending

## Diagnóstico

StorageClass configurada con:
volumeBindingMode: WaitForFirstConsumer

No había Pod usando el PVC.

## Verificaciones
```
oc describe pvc <nombre>
```

```
oc get storageclass
```
Solución aplicada
Asociar el PVC al Pod en el Deployment.

Una vez el Pod se crea, el PVC cambia a Bound.

Lección aprendida
En OpenShift/Kubernetes, el volumen no se provisiona hasta que un Pod lo solicita (según StorageClass).