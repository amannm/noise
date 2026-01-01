# dataPointer

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

A pointer to the multiarray’s underlying memory.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var dataPointer: UnsafeMutableRawPointer { get }
```

## See Also

### Accessing a multiarray’s elements

- [subscript(_:)](subscript(_:).md)

- [pixelBuffer](pixelbuffer.md)
  A reference to the multiarray’s underlying pixel buffer.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
