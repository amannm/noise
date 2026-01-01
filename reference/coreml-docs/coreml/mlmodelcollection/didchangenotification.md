# didChangeNotification

**Type Property**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelCollection](../mlmodelcollection.md)

---

The notification the framework sends when it receives an update to a model collection.

## Declaration

**Platforms:** Mac Catalyst, visionOS

```objc
class let didChangeNotification: NSNotification.Name
```

## Overview

Register your app to get notifications when a model collection update is available by calling [addObserver(forName:object:queue:using:)](https://developer.apple.com/documentation/Foundation/NotificationCenter/addObserver(forName:object:queue:using:)).

```swift
let center = NotificationCenter.default
var token: NSObjectProtocol?

token = center.addObserver(forName: MLModelCollection.didChangeNotification,
                           object: nil,
                           queue: nil) { [unowned self] note in
    guard let modelCollection = note.object as? MLModelCollection else {
        print("Model Collection notification's object is not a model collection")
        return
    }

    // Use updated model collection ...
    self.receivedUpdatedModelCollection(modelCollection)

    // Clean up notification registration.
    center.removeObserver(token!)
}
```

Typically, you register for model collection notifications when your app needs to use the newest models as soon as the collection is available. Your app can always get the newest model collection by calling [beginAccessingModelCollectionWithIdentifier:completionHandler:](https://developer.apple.com/documentation/coreml/mlmodelcollection/beginaccessingmodelcollectionwithidentifier:completionhandler:).

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
