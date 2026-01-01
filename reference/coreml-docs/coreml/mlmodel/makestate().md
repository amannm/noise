# makeState()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLModel](../mlmodel.md)

---

Creates a new state object.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func makeState() -> MLState
```

## Overview

Core ML framework will allocate the state buffers declared in the model.

The allocated state buffers are initialized to zeros. To initialize with different values, use `.withMultiArray(for:)` to get the mutable `MLMultiArray`-view to the state buffer.

```swift
// Create state that contains two state buffers: s1 and s2.
// Then, initialize s1 to 1.0 and s2 to 2.0.
let state = model.makeState()
state.withMultiArray(for: "s1") { stateMultiArray in
    stateMultiArray[0] = 1.0
}
state.withMultiArray(for: "s2") { stateMultiArray in
    stateMultiArray[0] = 2.0
}
```

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
