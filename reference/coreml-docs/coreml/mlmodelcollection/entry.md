# MLModelCollection.Entry

**Class**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelCollection](../mlmodelcollection.md)

---

A model and its identifier within a model collection.

## Declaration

**Platforms:** Mac Catalyst, visionOS

```objc
class Entry
```

## Topics

### Identifying a model

- [modelIdentifier](entry/modelidentifier.md)
  The name of the model, which is unique to the collection.

### Locating a compiled model file

- [modelURL](entry/modelurl.md)
  The compiled model’s location on the device’s file system.

### Comparing model collection entries

- [isEqual(to:)](entry/isequal(to:).md)
  Returns a Boolean value that indicates whether the two entries are equal.

## See Also

### Retreiving models from a collection

- [entries](entries.md)
  A dictionary of model entries keyed to the models’ identifiers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
