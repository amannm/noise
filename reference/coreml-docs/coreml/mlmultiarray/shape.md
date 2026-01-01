# shape

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

The multiarray’s multidimensional shape as a number array in which each element’s value is the size of the corresponding dimension.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var shape: [NSNumber] { get }
```

## See Also

### Inspecting a multiarray

- [count](count.md)
  The total number of elements in the multiarray.

- [dataType](datatype.md)
  The underlying type of the multiarray.

- [strides](strides.md)
  A number array in which each element is the number of memory locations that span the length of the corresponding dimension.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
