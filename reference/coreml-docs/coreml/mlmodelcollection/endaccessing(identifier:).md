# endAccessing(identifier:)

**Type Method**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModelCollection](../mlmodelcollection.md)

---

Terminates access to a model collection.

## Declaration

**Platforms:** Mac Catalyst, visionOS

```objc
class func endAccessing(identifier: String) async throws -> Bool
```

### Parameters

- **`identifier`**
  The name of the model collection.

## Overview

Use this method when your app no longer needs access to a model collection.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
