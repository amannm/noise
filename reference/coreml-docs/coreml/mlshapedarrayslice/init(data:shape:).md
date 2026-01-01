# init(data:shape:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArraySlice](../mlshapedarrayslice.md)

---

Creates a shaped array with a defined data and shape.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(data: Data, shape: [Int])
```

### Parameters

- **`data`**
  A block of data that initializes the array.

- **`shape`**
  The shape of the array.

## See Also

### Creating a shaped array slice with data

- [init(data:shape:strides:)](init(data:shape:strides:).md)
  Creates a shaped array with defined data, shape, and strides.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
