# init(_:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init<C>(_ data: C) throws where C : Collection, C.Element : FixedWidthInteger
```

## Overview

```None
let v:[Int32] = [3, 2, 1]
let m = try MLMultiArray(v)
print(m)
Int32 3 vector
[3,2,1]
```

This initializer will trap if called with data containing FixedWidthInteger elements that cannot be safely converted to Int32, but it is safe to use with wider types so long as the actual data is within range.

```None
let a = try MLMultiArray([Int.max]) // trap!
let b = try MLMultiArray([Int(Int32.max), Int(Int32.min)]) // This is fine.
```

## See Also

### Creating a multiarray

- [init(shape:dataType:)](init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.

- [init(shape:dataType:strides:)](init(shape:datatype:strides:).md)
  Creates the object with specified strides.

- [init(dataPointer:shape:dataType:strides:deallocator:)](init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.

- [init(byConcatenatingMultiArrays:alongAxis:dataType:)](init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.

- [init(pixelBuffer:shape:)](init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.

- [MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
