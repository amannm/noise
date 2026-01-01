# strides

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

An integer array in which each element is the number of memory locations that spans the length of the corresponding dimension.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var strides: [Int] { get }
```

## See Also

### Inspecting a shaped array type

- [shape](shape.md)
  An integer array in which each element represents the size of the corresponding dimension.

- [count](count.md)
  The number of elements in the shaped array’s first dimension.

- [isScalar](isscalar.md)
  A Boolean value that indicates whether the shaped array lacks a shape.

- [scalarCount](scalarcount.md)
  The total number of elements in the shaped array type.

- [scalar](scalar-swift.property.md)
  A computed property that returns the first element when the shape isn’t empty, or sets the shaped array’s underlying scalar type.

- [scalars](scalars.md)
  A computed property that generates a linear array that contains every element, or assigns the elements of an array to the shaped array’s elements.

- [withUnsafeShapedBufferPointer(_:)](withunsafeshapedbufferpointer(_:).md)
  Provides read-only access of the shaped array’s underlying memory to a closure.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
