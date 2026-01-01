# MLModelCollection

**Class**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A set of Core ML models from a model deployment.

## Declaration

**Platforms:** Mac Catalyst, visionOS

```objc
class MLModelCollection
```

## Overview

Use a model collection to access the models from a Core ML Model Deployment. For example, you can use a model collection to replace one or more of your app’s built-in models with a newer version.

To access the newest model collection from a deployment, call the [beginAccessingModelCollectionWithIdentifier:completionHandler:](https://developer.apple.com/documentation/coreml/mlmodelcollection/beginaccessingmodelcollectionwithidentifier:completionhandler:) type method. Your app can also get a notification when Core ML receives an update to a model collection (see [didChangeNotification](mlmodelcollection/didchangenotification.md)).

## Topics

### Accessing a model collection

- [endAccessing(identifier:)](mlmodelcollection/endaccessing(identifier:).md)
  Terminates access to a model collection.

### Identifying a model collection

- [identifier](mlmodelcollection/identifier.md)
  The name of the model collection, unique to the development team.

- [deploymentID](mlmodelcollection/deploymentid.md)
  The unique identifier of the model collection’s deployment.

### Retreiving models from a collection

- [entries](mlmodelcollection/entries.md)
  A dictionary of model entries keyed to the models’ identifiers.

- [MLModelCollection.Entry](mlmodelcollection/entry.md)
  A model and its identifier within a model collection.

### Registering for model collection updates

- [didChangeNotification](mlmodelcollection/didchangenotification.md)
  The notification the framework sends when it receives an update to a model collection.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
